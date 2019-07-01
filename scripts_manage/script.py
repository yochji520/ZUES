import time
from common.logs import LogtoLog
from scripts_manage.models import scripts_info
import random


class Script(object):
    def __init__(self, **scriptdict):
        self.scriptdict = scriptdict

    @classmethod
    def register_script(self,scriptdict):
        serverid = ""
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            serverid += ch
        script = scripts_info()
        script.script_id = int(serverid)
        script.script_name = scriptdict['script_name']
        script.script_langue = scriptdict['script_langue']
        script.script_type = scriptdict['script_type']
        script.script_env = scriptdict['script_env']
        script.script_path = scriptdict['script_path']
        script.script_desc = scriptdict['script_desc']
        script.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        script.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log = LogtoLog().getlog()
        try:
            script.save()
        except Exception as err:
            log.error("数据库操作异常", err)
        except ConnectionError as err:
            log.error("数据库连接异常，请查看数据库服务是否正常运行或者网络是否存在异常", err)

    @classmethod
    def scripts_list(self):
        from common.logs import LogtoLog
        logging = LogtoLog().getlog()
        try:
            script_list = scripts_info.objects.all().order_by('script_id').values()
            scriptlist_dict = list(script_list)
            return scriptlist_dict
        except ConnectionError as err:
            logging.error(err)

    @classmethod
    def script_details(self, scriptid):
        from common.logs import LogtoLog
        logging = LogtoLog().getlog()
        try:
            script_info = scripts_info.objects.filter(script_id=scriptid)
            return script_info
        except ConnectionError as err:
            logging.error("数据库无法连接%s" + err)
        except Exception as err:
            logging.error("数据库操作失败，%s", err)

    @classmethod
    def script_del(self, scriptid):
        """
        :param scriptid:待删除的脚本信息script_id
        :return:
        """
        from common.logs import LogtoLog
        logging = LogtoLog().getlog()
        try:
            del_res = scripts_info.objects.filter(script_id=scriptid).delete()
            if del_res[0] == 1:
                return 200
            else:
                return 10011
        except ConnectionError as err:
            logging.error("数据库无法连接，%s", err)
        except Exception as err:
            logging.error("数据库操作失败，%s", err)
