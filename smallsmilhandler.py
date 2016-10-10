#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.list = []
        self.dicc = {"root-layout": ["width", "height", "background-color"],
                     "region": ["id", "top", "bottom", "left", "right"],
                     "img": ["src", "region", "begin", "dur"],
                     "audio": ["src", "begin", "dur"],
                     "textstream": ["src", "region"]}

    def startElement(self, name, attrib):
        if name in self.dicc:
            dicc = {}
            for item in self.dicc[name]:
                dicc[item] = attrib.get(item, "")
            diccname = {name: dicc}
            self.list.append(diccname)

    def get_tags(self):

        return self.list

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
