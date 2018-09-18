import csv



class DocToWeb():


    def __init__(self, file_n, line_pointer):
        self.line_pointer = line_pointer
        self.file_name = file_n
        print ("Processing the document")

    def parse_text(self):

        with open (self.file_name, 'r') as text_file:

            for index, line in enumerate(text_file):
                if (index+1) >= self.line_pointer:
                    line_word_list = line.split()
                    tagType = self.checkTagType(line_word_list[0])



    def checkTagType(self, symbol):

        self.tagDict[symbol]

    def tagDictionary(self):

        self.tagDict = {">>>":"p", "*":"b", }
