class PalindromeRecognizer:
    def __init__(self,fileName):
        self.fileReader = open(fileName,"r")

    def recognize(self):
        try:
            #reading statement from file
            for rawSentence in  self.fileReader:
              if rawSentence != "\n":
                #formatting the statement for identification
                formattedSentence = ''.join(r.lower() for r in rawSentence if r.isalnum())
                #comparing the string by revrsing using extended slicing
                if formattedSentence[::-1] == formattedSentence:
                    print rawSentence+"palindrome"+"\n"
                else:
                    print rawSentence+"not a palindrome"+"\n"
            self.fileReader.close()
        except:
            print "Error : Incorrect file name or path"

if __name__ == '__main__':
    pr = PalindromeRecognizer(str(raw_input("Enter the file name:")))
    pr.recognize()

