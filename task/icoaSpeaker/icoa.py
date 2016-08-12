import pyttsx,os,time

class ICOASpeech:
    def __init__(self):
        #icoa code words dict
        self.icoaDict    =   {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
                             'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',
                             'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',
                             'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
                             'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
                             'z':'zulu'}

    #icoa speech executer
    def speakIcoa(self,text,textTime=1,icoaTime=2):
            text = text.lower()

            #identification of platform
            platform = os.name

            #for windows
            if platform == 'nt':
                for word in text:
                    for letter in word:
                        if letter.isalpha():
                            #execute the speech by pyttsx
                            engine = pyttsx.init()
                            engine.say(self.icoaDict[letter])
                            engine.runAndWait()
                            time.sleep(textTime)
                    time.sleep(icoaTime)
            #for linux
            if platform == 'posix':
                for word in text:
                    for letter in word:
                        if letter.isalpha():
                            #execute the speech by pyttsx
                            engine = pyttsx.init()
                            engine.say(self.icoaDict[letter])
                            engine.runAndWait()
                            time.sleep(textTime)
                    time.sleep(icoaTime)
            #for mac os
            if platform == 'mac':
                for word in text:
                    for letter in word:
                        if letter.isalpha():
                            #execute by os, say command
                            os.system('say'+self.icoaDict[letter])
                            time.sleep(textTime)
                    time.sleep(icoaTime)


if __name__ == "__main__":
 icoa = ICOASpeech()
 icoa.speakIcoa("Hello techspawn")

