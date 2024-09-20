#!/usr/bin/env python
import yaml
import numpy as np
with open('../models/rims.yml',mode='r') as fp:
    rims = yaml.safe_load(fp)
print('Rim models loaded.')
for key,val in rims.items():
    print("{}:".format(key))
    print("  Brand:      {}".format(val['brand']))
    print("  Name:       {}".format(val['name']))
    print("  Size:       {}".format(val['size']))
    print("  Material:   {}".format(val['material']))
    print("  Weight:     {} g".format(val['weight']))
    print("  ERD:        {} mm".format(val['erd']))
    print("  Int. width: {} mm".format(val['id']))
    print("  Ext. width: {} mm".format(val['od']))
    print("  Height:     {} mm".format(val['h']))
    print("  OSB:        {} mm".format(val['osb']))
