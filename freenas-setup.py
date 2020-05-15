import argparse
import json
import sys

import requests


class Startup(object):

    def __init__(self, hostname, user, secret):
        self._hostname = hostname
        self._user = user
        self._secret = secret

        self._ep = 'http://%s/api/v1.0' % hostname

    def request(self, resource, method='GET', data=None):
        if data is None:
            data = ''
        r = requests.request(
            method,
            '%s/%s/' % (self._ep, resource),
            data=json.dumps(data),
            headers={'Content-Type': "application/json"},
            auth=(self._user, self._secret),
        )
        if r.ok:
            try:
                return r.json()
            except:
                return r.text

        raise ValueError(r)

    def create_pool(self,poolname,disks):
        self.request('storage/volume', method='POST', data={
            'volume_name': poolname,
            'layout': [
                {'vdevtype': 'stripe', 'disks': disks}, 
            ],
        })

    def create_dataset(self, poolname, datasetname):
        self.request('storage/volume/' + poolname + '/datasets', method='POST', data={
            'name': datasetname,
        })

    def create_cifs_share(self,poolname,datasetname,sharename):
        self.request('sharing/cifs', method='POST', data={
            'cifs_name': sharename,
            'cifs_path': '/mnt/'+poolname+'/'+datasetname,
            'cifs_guestonly': True
        })

    def service_start(self, name):
        self.request('services/services/%s' % name, method='PUT', data={
            'srv_enable': True,
        })

    def run(self):

        # create a new pool using disk ada0, ada1 and ada2
        self.create_pool("puddle",["ada0","ada1","ada2"])

        # Create a dataset names anime in pool tank
        # self.create_dataset("tank","anime")

        # Create a CIFS share called Manga that points to the dataset anime in pool tank
        # self.create_cifs_share("tank","anime","Manga")

        # Start the CIFS/SMB service
        # self.service_start('cifs')
        



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--hostname', required=True, type=str)
    parser.add_argument('-u', '--user', required=True, type=str)
    parser.add_argument('-p', '--passwd', required=True, type=str)

    args = parser.parse_args(sys.argv[1:])

    startup = Startup(args.hostname, args.user, args.passwd)
    startup.run()

if __name__ == '__main__':
    main()
