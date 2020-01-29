import json
from collections import OrderedDict

score = OrderedDict()


score["number2"] = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
score["iot"] = {0:100,1:95,2:92,3:85,4:75,5:88,6:94,7:76,8:68,9:79}
score["ml"] = {0:90,1:84,2:82,3:72,4:56,5:68,6:54,7:96,8:78,9:69}
score["python"] = {0:65,1:78,2:100,3:69,4:56,5:66,6:85,7:76,8:67,9:89}

with open('words.json','w',encoding='utf-8') as make_file:
      json.dump(score, make_file, ensure_ascii=False, indent='\t')
