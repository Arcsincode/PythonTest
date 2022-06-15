import json
import csv

kw={}
k1={'ku':{'ku1':1},}
kw.update(k1)
print(kw)
kw['ku'].update(({'ku':2}))
print(kw)

jkw1=json.dumps(kw)
print(jkw1)
kw2=json.loads(jkw1)
print(kw2)
kw2["ku"].update({'url':'aabbbcc'})
print(kw2)
jkw1=json.dumps(kw2)
print(jkw1)