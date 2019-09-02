#!/usr/bin/env python

# Quick script to check your Dell asset's warranty status
# Just drop your service tag as parameters for the script and go.

import sys
import requests

APIKEY = 'd676cf6e1e0ceb8fd14e8cb69acd812d'
URL = 'https://api.dell.com/support/v2/assetinfo/warranty/tags.json?svctags={0}&apikey=' + APIKEY


def get_warr_from_dell(svctag):
    res = requests.get(URL.format(svctag))

    if res.status_code != 200:
        sys.stderr.write('[%s] Caught %i as the response code.\n' % (svctag, res.status_code))
        sys.stderr.write('[%s] Unable to get details for given service tag.\n'
                         % svctag)
        return False

    fault = res.json['GetAssetWarrantyResponse']['GetAssetWarrantyResult']['Faults']
    if fault is not None:
        sys.stderr.write("[%s] Failed to find details. Sure it's a valid TAG?\n" % svctag)
        return False

    asset = res.json['GetAssetWarrantyResponse']['GetAssetWarrantyResult']['Response']['DellAsset']
    model = asset['MachineDescription']
    ent = asset['Warranties']['Warranty']
    shipped = asset['ShipDate']

    print('Service Tag:        ', svctag)
    print(' Model:             ', model)
    print(' Shipped:           ', shipped, '\n')
    print('{0:<20} {1:>15}'.format(*('Warranty Ends', 'ServiceLevelDescription')))
    for warr in [(d['EndDate'], d['ServiceLevelDescription']) for d in ent]:
        print('{0:<20} {1:>15}'.format(*warr))


# https://gist.github.com/teroka/0720274b87b77fe7171f

if __name__ == '__main__':
    get_warr_from_dell(sys.argv[1])
    sys.exit()
