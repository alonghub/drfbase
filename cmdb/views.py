from rest_framework.views import APIView
from rest_framework import serializers
from cmdb import models
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
class VirtualMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VirtualMachine
        fields = "__all__"
        depth = 1


class VirtualMachineSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = models.VirtualMachine
        fields = "__all__"
        depth = 0


class VirtualMachineView(APIView):
    # authentication_classes = []
    # permission_classes = []
    def get(self, request, *args, **kwargs):
        """
        获取虚拟机信息
        :param request: hostname/local_ip/gsd_id
        :param args:
        :param kwargs:
        :return: VirtualMachine单条记录
        """
        req = request.query_params.dict()
        if 'hostname' in req:
            vm_info = models.VirtualMachine.objects.filter(hostname=req['hostname']).first()
        elif 'local_ip' in req:
            vm_info = models.VirtualMachine.objects.filter(local_ip=req['local_ip']).first()
        else:
            return JsonResponse({'msg': 'Please check your params'})

        if vm_info:
            ser = VirtualMachineSerializer(instance=vm_info, many=False).data
        else:
            ser = {}
        return JsonResponse(dict(ser))


class PhysicalMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhysicalMachine
        fields = '__all__'
        depth = 1


class PhysicalMachineSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = models.PhysicalMachine
        fields = ['hostname']
        depth = 1


class PhysicalMachineView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        获取物理机信息
        :param request: hostname/local_ip/ipmi
        :param args:
        :param kwargs:
        :return: PhysicalMachine单条记录
        '''
        req = request.query_params.dict()
        if 'hostname' in req:
            pm_info = models.PhysicalMachine.objects.filter(hostname=req['hostname']).first()
        elif 'local_ip' in req:
            pm_info = models.PhysicalMachine.objects.filter(local_ip=req['local_ip']).first()
        elif 'all' in req:
            pm_info = models.PhysicalMachine.objects.all()
            ser = PhysicalMachineSerializerV2(instance=pm_info, many=True).data
            return HttpResponse(json.dumps(ser))
        else:
            return JsonResponse({'msg': 'please check your params.'})

        if pm_info:
            vm_info = models.VirtualMachine.objects.filter(pm=pm_info)
            ser = PhysicalMachineSerializer(instance=pm_info, many=False).data
            ser["vm_info"] = list(vm_info.values())
        else:
            ser = {}
        return JsonResponse(ser)


class VirtualMatchPhysicalView(APIView):
    def post(self, request, *args, **kwargs):
        '''
        同步指定区域的物理机和虚拟机对应关系(外键:vm表的pm_id = pm表的id)
        :param request: {"rg_id": 105, "nv_num": 4}  # 区域ID和显卡数量
        :param args:
        :param kwargs:
        :return:
        '''
        req = request.data
        step = req['nv_num']

        pm_data = models.PhysicalMachine.objects.filter(rg_id=req["region_id"]).order_by('hostname')
        pm_ser = PhysicalMachineSerializer(instance=pm_data, many=True).data
        vm_data = models.VirtualMachine.objects.filter(region_id=req["region_id"]).order_by('hostname')
        vm_ser = VirtualMachineSerializerV2(instance=vm_data, many=True).data
        vm_all = [vm_ser[i:i + step] for i in range(0, len(vm_ser), step)]

        item_count = 0
        for vm_group in vm_all:
            for vm_info in vm_group:
                vm_info['pm'] = pm_ser[item_count]['id']
                vm_id = models.VirtualMachine.objects.filter(gsd_id=vm_info['gsd_id']).first()
                vm_info_add_pm = VirtualMachineSerializerV2(instance=vm_id, data=dict(vm_info))
                if vm_info_add_pm.is_valid():
                    vm_info_add_pm.save()
            item_count += 1
        return HttpResponse("OK")
