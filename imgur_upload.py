#!/usr/bin/env python2 
import requests

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Upload an image to imgur.')
    parser.add_argument('client_id', type=str, help='Your imgur OAuth 2.0 Client-ID')
    parser.add_argument('image', type=argparse.FileType('rb'))
    args = parser.parse_args()

    r = requests.post('https://api.imgur.com/3/image.json',
        verify=False,  # For whatever reason, this uses the imgur.com cert
        params={'type': 'file'},
        files={'image': args.image},
        headers={'Authorization': "Client-ID " + args.client_id})
    j = r.json()

    if j['success']:
        print j['status'], j['data']['id'], j['data']['deletehash']
    else:
        print j['status'], j['data']['error']
        sys.exit(1)


if __name__ == '__main__':
    main()
