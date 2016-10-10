#!/usr/bin/python3
# -*- coding: utf-8 -

import sys
import json
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve


class KaraokeLocal(SmallSMILHandler):
    def __init__(self, documento):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(documento))
        self.Lista = cHandler.get_tags()

    def do_local(self):
        for line in self.Lista:
            for n in line:
                for kR in line[n]:
                    if line[n][kR][0:7] == "http://":
                        urlretrieve(line[n][kR])

    def to_json(self, File, File_Name=""):
        if File_Name:
            File = File_Name
        json_file = open(File, "w")
        json.dump(self.Lista, json_file, separators=(',', ': '), indent=4)
        json_file.close()

    def __str__(self):
        list = ""
        for line in self.Lista:
            for n in line:
                list = list + n
                for kR in line[n]:
                    list = list + "\t" + kR + ' = ' + '"' + line[n][kR] + '"'
                list += "\n"
        print(list)

if __name__ == "__main__":
    try:
        documento = sys.argv[1]
        Doc = KaraokeLocal(documento)
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")

    Doc_Json = sys.argv[1][:-5] + ".json"
    Doc.__str__()
    Doc.to_json(Doc_Json)
    Doc.do_local()
    Doc.to_json(Doc_Json, "local.json")
Doc.__str__()
