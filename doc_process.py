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
        first_split_word_prev = " "

        with open (self.file_name, 'r') as text_file:
            for index, line in enumerate(text_file):

                # Split Words from a line for all sorts of processing
                line_word_list      = line.split()

                # Continue to next line for empty lines
                if line_word_list == []:
                    continue

                word_list_length    =len(line_word_list)
                first_split_word    = line_word_list[0]

                # For one word lines, check if they are special tags
                if word_list_length == 1:
                    wrd_status, mod_wrd = self.checkLineTag(first_split_word)
                    if wrd_status == True:
                        line_word_list[0] = mod_wrd

                # Check for bold or italic words in all lines and  all sentences
                for word in line_word_list:
                    wrd_status, mod_wrd = self.checkBITag(word)
                    if wrd_status == True:
                        line_word_list[line_word_list.index(word)] = mod_wrd


                # Check for bullets and lists

                if first_split_word != "-"  and first_split_word_prev == "-":
                    self.html_content.append("</ul>")

                if first_split_word == "-":
                    if first_split_word_prev != "-":
                        self.html_content.append("<ul>")

                    temp_list = line_word_list[1:]
                    temp_list.append(self.tagDict_listing["-"][1])
                    temp_list.insert(0, self.tagDict_listing["-"][0])
                    line_word_list = temp_list

                # print ("AA: ", str(line_word_list))

                status, tags   = self.checkIfHeading(line_word_list[0])
                if status:
                    line_word_list.pop(0)
                    line_word_list.insert(0, tags[0])
                    line_word_list.append(tags[-1])

                html_equivalent = ' '.join(line_word_list)
                self.html_content.append(html_equivalent)

                first_split_word_prev = first_split_word

            try:
                html_rev_list = self.html_content.copy()
                html_rev_list.reverse()
                ul_open_in = html_rev_list.index("<ul>")
                ul_cls_in = html_rev_list.index("</ul>")
                print ("Cls: ", ul_cls_in, "Opn: ", ul_open_in)
                if ul_open_in < ul_cls_in:
                    self.html_content.append("</ul>")
            except:
                pass

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
        self.tagDict_listing    = {"-": ["<li>", "</li>"]}
        self.tagDict_blocks     = {"~~~~": ["<div>", "</div>"]}
        self.tagDict_word       = {"italics": ["<i>", "</i>"], "bold": ["<b>", "</b>"]}
        self.tagDict_line       = {"----": "<br>", "____": "<hr>"}
        self.tagDict_list = [self.tagDict_heading, self.tagDict_listing, self.tagDict_blocks, self.tagDict_word, self.tagDict_line]

    def tagIdentities(self):
        self.tag_identity = {0: "word", 1: "para", 2 : "heading"}

    def checkBITag(self, wrd):

        if (wrd[0]=="_") and (wrd[-1]=="_") and len(set(wrd))!=1:
            status, wrd = True, self.tagDict_word["italics"][0] + wrd[1:-1] + self.tagDict_word["italics"][-1]
        elif (wrd[0]=="*") and (wrd[-1]=="*"):
            status, wrd = True, self.tagDict_word["bold"][0] + wrd[1:-1] + self.tagDict_word["bold"][-1]
        else:
            status, wrd = False, " "

        return status, wrd

    def checkLineTag(self, wrd):
       for elem in self.tagDict_line:
           try:
               return True, self.tagDict_line[wrd]
           except:
               return False, False

    def appendToWebpage(self, webpage_doc):
        with open (webpage_doc, "a") as to_append_file:
            for index, line in enumerate(to_append_file):
                if index == self.line_pointer:
                    to_append_file.write("\n")
                    for content in self.html_content:
                        to_append_file.write(content)
                    break
                else:
                    print ("Line pointer doesn't exist")


if __name__ == '__main__':
    webpage     = "append.html"
    doc2web_obj = DocToWeb("trial_text.txt", 62)
    doc2web_obj.parse_text()
    doc2web_obj.appendToWebpage(webpage)