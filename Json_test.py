import json
import csv

kw={}
k1={'ku':{'ku1':1},}
kw.update(k1)
print(kw)
kw['ku'].update(({'ku':2}))
print(kw)