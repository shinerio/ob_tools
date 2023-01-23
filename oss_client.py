# -*- coding: utf-8 -*-
import os
import oss2


class oss_client(object):
    def __init__(self):
        self.oss_path = os.environ.get('oss_path')
        auth = oss2.Auth(os.environ.get('oss_ak'), os.environ.get('oss_sk'))
        self.bucket = oss2.Bucket(auth, os.environ.get('oss_endpoint'), os.environ.get('oss_bucket'))

    def put(self, file_path):
        os_path, file_name = os.path.split(file_path)
        os_name = self.oss_path + file_name
        # Upload
        with open(file_path, 'rb') as f:
            return self.bucket.put_object(os_name, f.read()).resp.response.url

