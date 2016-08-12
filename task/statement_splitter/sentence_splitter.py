import re

class SentenceSplitter:

    def __init__(self,fileName):
        self.fileReaderObj = open(fileName,"r")
        self.enderRegex = r".|\?|!"
        self.identifierRegex = r"((([^A-Z]+[a-z0-9]+)|([A-Z0-9]+[^a-z]+))([\)|}|\]]?[\"|']?)(\.|\?|!)+)([\)|}|\]]?[\"|']?) ([\(|{|\[]?[\"|']?[A-Z]+)"


    def sentenceSplitter(self):
        try:
            for line in self.fileReaderObj:

                #check if line is empty
                if line != "\n":

                    #format the the text by removing unwanted whitespaces
                    line = line.strip()
                    line = re.sub(" +"," ",line)

                    #create list of words based on whitespaces
                    wordList = line.split(" ")

                    #process
                    for word in wordList:

                        #position of the word in the list
                        pos = wordList.index(word)

                        if pos != len(wordList) - 1:
                            #create a string from using the position for regex comparision
                            curr_line = wordList[pos] + " " + wordList[pos + 1]

                            #search for end of the statement by .,?,!
                            if re.search(self.enderRegex,curr_line):

                                #regex comparision for end of the statement
                                if re.match(self.identifierRegex, curr_line):
                                        print " ".join(wordList[:pos+1])
                                        wordList = wordList[pos+1:]
                        else:
                            print " ".join(wordList[:pos+1])+"\n"


            self.fileReaderObj.close()

        except:
            print "Error : invalid file name or path"

if __name__ == "__main__":
    ss = SentenceSplitter("text.txt")
    ss.sentenceSplitter()
