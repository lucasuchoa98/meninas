# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:49:54 2019

@author: Lucas
"""
import xarray as xr

prec_d = "prec_daily_UT_Brazil_v2.2_20000101_20091231.nc"
prequi = xr.open_dataset(prec_d)
prec = prequi["prec"]
print(prec.values)
precipitalista = []
for m in prec.values:
    precipitalista.append(m)