import requests
import json


class DetectorClient:

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port

    def set_config(self, param, value, iface='detector'):
        url = 'http://%s:%s/%s/api/1.8.0/config/%s' % (self._ip, self._port, iface, param)
        self._request(url, data=json.dumps({'value': value}))

    def send_command(self, command):
        url = 'http://%s:%s/detector/api/1.8.0/command/%s' % (self._ip, self._port, command)
        self._ip, self._port, command
        self._request(url)

    def _request(self, url, data={}, headers={}):
        reply = requests.put(url, data=data, headers=headers)
        assert reply.status_code in range(200, 300), reply.reason

    def monitor_image(self, param):
        url = 'http://%s:%s/monitor/api/1.8.0/images/%s' % (self._ip, self._port, param)
        return requests.get(url, headers={'Content-type': 'application/tiff'}).content
