#!/usr/bin/env python
import yaml
import numpy as np
with open('../models/rims.yml',mode='r') as fp:
    rims = yaml.safe_load(fp)
for key,val in rims.items():
    print(val['name'])
