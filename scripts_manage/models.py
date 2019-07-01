from django.db import models


class scripts_info(models.Model):
    id = models.AutoField(primary_key=True)
    script_id = models.IntegerField('脚本ID', null=False, default=0, db_index=True)
    script_name = models.CharField('脚本名称', max_length=100, null=False, default='')
    script_langue = models.SmallIntegerField('脚本语言，1：SHELL 2:PYTHON', null=False, default=0)
    script_type = models.SmallIntegerField('脚本类型,1:ARCHIVE 2:ETL 3:BACKUP', null=False, default=0)
    script_env = models.IntegerField('脚本对应环境, 1：PRO_ENV 2:script_env 3.TEST_ENV', null=False, default='')
    script_path = models.CharField('脚本上传路径', max_length=300, null=False, default='')
    script_desc = models.CharField('脚本描述', max_length=300, null=False, default='')
    create_time = models.DateTimeField('脚本创建时间', null=False, default='2012-12-12 12:12:12')
    update_time = models.DateTimeField('脚本修改时间', null=False, default='2012-12-12 12:12:12')




