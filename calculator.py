from tkinter import *



def speak(text, language='en'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()


# This class inherit from Frame
class App:
    def __init__(self):

        self.display = StringVar()
        self.entry = Entry(root, relief=FLAT, textvariable=self.display, justify='right', font="Arial 20", bd=15, bg='orange')
        self.entry.pack(side=TOP)
        self.entry.focus()
        self.entry.bind("<Key>", lambda e: self.store(e))
        self.entry.bind("<Return>", lambda e: self.calc(e))
        self.entry.bind("<Delete>", lambda e: self.display.set(0))
        self.entry.bind("<BackSpace>", lambda e: self.display.set(0))

        self.temp = "" # store de single numbers
        self.numeri = []
        self.operator = ""
        self.result = 0


    def store(self, key):
        if key.char in "0123456789":
            print("Ho aggiunto un digit")
            self.temp += key.char
        if key.char in "+-*/":
            if self.operator != "":
                print("qui vuol dire che già c'e 2+3 e ora se faccio 2+3+ non faccio vedere il + ma calcolo il risultato 2+3 quindi self.calc(key)")
                self.operator = key.char
                self.calc(key)
                
            else:
                print("SE l'operatore è = '' vuol dire che ")
                print("abbiamo cliccato un operatore")
                print("aggiungo l'operatore")
                self.operator = key.char


    def calc(self, key):
        print("Calcolo il risultato...")
        self.store(key)
        self.numeri.append(int(self.temp))
        print(self.numeri, self.operator)
        match self.operator:
            case "+":
                self.result += self.numeri[0] + self.numeri[1]
            case "-":
                self.result += self.numeri[0] - self.numeri[1]
        print(self.result)
        self.numeri = []
        self.numeri.append(self.result)
        print("Nella lista ora c'è solo il risultato:", self.numeri)
        print("azzero operatore e numero temporaneo")
        self.operator = ""
        self.display.set(self.result)
        self.temp = ""



if __name__ == '__main__':
    root = Tk()
    App()
    root.mainloop()
