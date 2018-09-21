import csv



class DocToWeb():

    def __init__(self, file_n, line_pointer):
        self.line_pointer = line_pointer
        self.file_name = file_n
        self.tagDictionary()
        print ("Processing the document")

    def parse_text(self):
        # Start parsing the text document sequentially
        self.html_content = []
        wrd_status = False
        with open (self.file_name, 'r') as text_file:
            for index, line in enumerate(text_file):

                line_word_list = line.split()
                # Continue to next line for empty lines
                if line_word_list == []:
                    continue
                if len(line_word_list) == 1:
                    wrd_status, mod_wrd = self.checkLineTag(line_word_list[0])

                    if wrd_status == True:
                        line_word_list[0] = mod_wrd

                if wrd_status == False:
                    for word in line_word_list:
                        wrd_status, mod_wrd = self.checkBITag(word)
                        if wrd_status == True:
                            line_word_list[line_word_list.index(word)] = mod_wrd

                # print ("AA: ", str(line_word_list))

                status, tags   = self.checkIfHeading(line_word_list[0])
                if status:
                    line_word_list.pop(0)
                    line_word_list.insert(0, tags[0])
                    line_word_list.append(tags[-1])

                html_equivalent = ' '.join(line_word_list)
                self.html_content.append(html_equivalent)

        for lines in self.html_content:
            print (lines)

    def checkIfHeading(self, str):
        try:
            tags_to_append = self.tagDict_heading[str]
            return True, tags_to_append
        except:
            return  False, []

    def checkTagType(self, symbol):
        for index, dictnry in enumerate(self.tagDict_list):
            try:
                return index, dictnry[symbol]
            except:
                continue
            finally:
                return -1, -1

    def tagDictionary(self):

        self.tagDict_heading    = {">": ["<h1>", "</h1>"], ">>": ["<h2>", "</h2>"], ">>>": ["<h3>", "</h3>"]}
        self.tagDict_para       = {"-": "<ul>", "~~~~": ["<div>", "</div>"]}
        self.tagDict_word       = {"italics": ["<i>", "</i>"], "bold": ["<b>", "</b>"]}
        self.tagDict_line       = {"----": "<br>", "____": "<hr>"}

        self.tagDict_list = [self.tagDict_word, self.tagDict_para, self.tagDict_heading]

    def tagIdentities(self):
        self.tag_identity = {0: "word", 1: "para", 2 : "heading"}

    def checkBITag(self, wrd):

        if (wrd[0]=="_") and (wrd[-1]=="_") and len(set(wrd))!=1:
            status, wrd = True, self.tagDict_word["italics"][0] + wrd + self.tagDict_word["italics"][-1]
        elif (wrd[0]=="*") and (wrd[-1]=="*"):
            status, wrd = True, self.tagDict_word["bold"][0] + wrd + self.tagDict_word["bold"][-1]
        else:
            status, wrd = False, " "

        return status, wrd

    def checkLineTag(self, wrd):
       for elem in self.tagDict_line:
           try:
               return True, self.tagDict_line[wrd]
           except:
               return False, False

if __name__ == '__main__':
    doc2web_obj = DocToWeb("trial_text.txt", 5)
    doc2web_obj.parse_text()