# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiUserinfo(models.Model):
    user_type = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_userinfo'


class PhysicalMachine(models.Model):
    ipmi = models.CharField(max_length=255, blank=True, null=True)
    local_ip = models.CharField(max_length=255, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    local_netmask = models.CharField(max_length=255, blank=True, null=True)
    local_gateway = models.CharField(max_length=255, blank=True, null=True)
    local_mac = models.CharField(max_length=255, blank=True, null=True)
    public_ip = models.CharField(max_length=255, blank=True, null=True)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    sn = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    gsd_id = models.CharField(max_length=255, blank=True, null=True)
    rg_id = models.CharField(max_length=255, blank=True, null=True)
    cabinet_location = models.CharField(max_length=255, blank=True, null=True)
    cpu_core_total = models.CharField(max_length=255, blank=True, null=True)
    cpu_model = models.CharField(max_length=255, blank=True, null=True)
    mem_total = models.CharField(max_length=255, blank=True, null=True)
    nic_num = models.CharField(max_length=255, blank=True, null=True)
    nic_model = models.CharField(max_length=255, blank=True, null=True)
    gpu_num = models.CharField(max_length=255, blank=True, null=True)
    gpu_model = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physical_machine'


class VirtualMachine(models.Model):
    pm = models.ForeignKey(PhysicalMachine, models.DO_NOTHING, blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    local_ip = models.CharField(max_length=255, blank=True, null=True)
    local_netmask = models.CharField(max_length=255, blank=True, null=True)
    local_gateway = models.CharField(max_length=255, blank=True, null=True)
    local_mac = models.CharField(max_length=255, blank=True, null=True)
    public_ip = models.CharField(max_length=255, blank=True, null=True)
    public_netmask = models.CharField(max_length=255, blank=True, null=True)
    public_gateway = models.CharField(max_length=255, blank=True, null=True)
    publicmac = models.CharField(max_length=255, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    region_type = models.CharField(max_length=255, blank=True, null=True)
    gsd_id = models.IntegerField(blank=True, null=True)
    os_type = models.CharField(max_length=255, blank=True, null=True)
    region_storage_id = models.IntegerField(blank=True, null=True)
    region_storage_addr = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    reboot_status = models.IntegerField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    line = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    physical_host = models.CharField(max_length=255, blank=True, null=True)
    physical_ip = models.CharField(max_length=255, blank=True, null=True)
    cpu_core_total = models.CharField(max_length=255, blank=True, null=True)
    mem_total = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'virtual_machine'
