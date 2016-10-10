#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve
import json
import sys

def Create_JSON(list):
    with open(sys.argv[1][:-5]+".json",'w') as outfile:
        json.dump(list,outfile,indent=4,separators=(',' , ': '))
    
def show(document):
    list=""
    for line in document:
        for name in line:
            list = list + name #+ "\t"            
            for keepR in line[name]:
                list = list + "\t" + keepR + ' = ' + '"' + line[name][keepR] + '"'
            list += "\n"
    print(list)
                

def downl(document):
    for line in document:
        for name in line:
            for keepR in line[name]:
                if line[name][keepR][0:7] == "http://":
                    print(line[name][keepR])                    
                    urlretrieve(line[name][keepR])
                    
                
                
                

if __name__ == "__main__":

    document = sys.argv[1]
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(document))
    print(cHandler.get_tags())
    show(cHandler.get_tags())
    downl(cHandler.get_tags())
    Create_JSON(cHandler.get_tags())
