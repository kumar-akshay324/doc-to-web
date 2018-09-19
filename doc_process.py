import csv



class DocToWeb():

    def __init__(self, file_n, line_pointer):
        self.line_pointer = line_pointer
        self.file_name = file_n
        self.tagDictionary()
        print ("Processing the document")

    def parse_text(self):

        with open (self.file_name, 'r') as text_file:
            for index, line in enumerate(text_file):
                if (index+1) >= self.line_pointer:
                    line_word_list = line.split()
                    tagType = self.checkTagType(line_word_list[0])

    def checkTagType(self, symbol):

        for index, dictnry in enumerate(self.tagDict_list):
            try:
                return dictnry[symbol]
            except:
                continue

    def tagDictionary(self):

        self.tagDict_inline = {">": ["<h1>", "</h1>"], ">>": ["<h2>", "</h2>"], ">>>": ["<h3>", "</h3>"]}
        self.tagDict_para   = {"____": "<br>", "-": "<ul>", "----": ["<div>", "</div>"]}
        self.tagDict_word   = {"_abc_": ["<i>", "</i>"], "*abc*": ["<b>", "</b>"]}

        self.tagDict_list = [self.tagDict_para, self.tagDict_inline, self.tagDict_word]

    def checkBold(self, stra, strb):
        if (str == "*") and (strb=="*"):
            return True

    def checkItalics(self, stra, strb):
        if (str == "_") and (strb=="_"):
            return True