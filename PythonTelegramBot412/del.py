import sqlite3
import datetime
from myapp import sqltablemode, DirectoryList
import json
import ast


RES = {}
list = DirectoryList.AnimalList()
for j in range(0, len(list)):
    RES[list[j]] = {0}
RES['Other'] = {0}

a = sqltablemode.statistics_values_list()
for i in range(0,len(a)):
    b = a.get('message_'+str(i+1))
    c = b.get('text')

    if c in list:
        a1 = str(RES.get(c))
        a1 = int(a1[1:-1])
        a1+=1
        RES[c]={a1}
    else:
        a1 = str(RES.get('Other'))
        a1 = int(a1[1:-1])
        a1+=1
        RES['Other']={a1}

print({'type' : RES['Cats']})
