import yaml
import os
from common.logs import LogtoLog


def create_dir(script_dir):
    """
    :param base_script_dir:放置脚本基础目录
    :return:
    """
    logging = LogtoLog().getlog()
    if os.path.exists(script_dir) is False:
        try:
            os.makedirs(script_dir)
            return True
        except FileExistsError as err:
            logging.info("目录已存在，创建失败,%s", err)
    else:
        return True


def handle_uploaded_file(f, fliename, dirpath):
    """
    :param f: 上传的文件
    :param p: 文件类型，用于创建文件目录
    :return:
    """
    if create_dir(dirpath):
        fp = dirpath + '/' + str(fliename)
        with open(fp, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
