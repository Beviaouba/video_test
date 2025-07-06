from qiniu import Auth,put_data,put_file
from django.conf import settings


class Qiniu:

    def __init__(self, bucket_name, base_url):
        self.bucket_name = bucket_name
        self.base_url = base_url
        self.q = Auth(settings.QINIU_AK, settings.QINIU_SK)

    def put(self,name,path):
        token = self.q.upload_token(self.bucket_name,name)
        ret,info = put_file(token,name,path)
        if 'key' in ret:
            remote_url = 'http://'+'/'.join([self.base_url,ret['key']])
            return remote_url


video_qiniu = Qiniu(settings.QINIU_VIDEO, settings.QINIU_VIDEO_URL)

