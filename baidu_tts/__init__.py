# coding: utf-8

import time
from uuid import uuid4
from urllib import quote

import requests


class Buffer(object):
    def __init__(self, content, content_type, content_length):
        self.content = content
        self.content_type = content_type
        self.content_length = content_length

    def read(self):
        return self.content

    def write(self, fp):
        with open(fp, 'wb') as f:
            f.write(self.read())


class BaiduTTS(object):

    def __init__(self, api_key, secret_key):
        self.cache = {}
        self.api_key = api_key
        self.secret_key = secret_key

    def fetch_access_token(self):
        url = 'https://openapi.baidu.com/oauth/2.0/token'
        key = 'access_token'
        res = self.cache.get(key)
        if res and res['expire_time'] > time.time():
            return res['data']
        resp = requests.get(
            url,
            params={
                'grant_type': 'client_credentials',
                'client_id': self.api_key,
                'client_secret': self.secret_key
            }
        )
        jsn = resp.json()
        access_token = jsn['access_token']
        expires_in = jsn['expires_in']
        self.cache[key] = {
            'expire_time': time.time() + expires_in - 20,
            'data': access_token
        }
        return access_token

    def say(self, text, lang='zh', raw=False):
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        url = 'http://tsn.baidu.com/text2audio'
        access_token = self.fetch_access_token()
        resp = requests.post(url, data={
            'tex': quote(text),
            'lan': lang,
            'tok': access_token,
            'ctp': 1,
            'cuid': uuid4().hex
        })

        try:
            resp.json()
            return
        except ValueError:
            if raw:
                return resp
            return Buffer(
                resp.content, resp.headers['content-type'],
                int(resp.headers['content-length'])
            )
