from tkinter import * 

class ONP:
    
    def __init__(self, equasion) -> None:
        self.equasion = equasion




class Window:
    
    def __init__(self) -> None:
        self.rootWindow = Tk()
        self.rootWindow.geometry("367x409")
        self.rootWindow.resizable(0, 0)
        self.rootWindow.title("Calculator")
        self.drawWindow()
        self.rootWindow.mainloop()
        
    def drawWindow(self):
        
        self.buttonWidth = 5
        self.buttonHeight = 2
        
        self.historyWindow = Text(self.rootWindow, width=43, height=5, font=("Sans", 10), padx=10, pady=10)
        self.historyWindow.grid(row=0, column=0, columnspan=5)
        
        self.screenWindow = Text(self.rootWindow, width=20, height=1, font=("Sans", 20), padx=10, pady=10)
        self.screenWindow.grid(row=1, column=0, columnspan=5)
        
        self.backspaceButton = Button(self.rootWindow, text="<<", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.clearScreen())
        self.backspaceButton.grid(row=2, column=0)
        
        self.leftparButton = Button(self.rootWindow, text="(", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("("))
        self.leftparButton.grid(row=2, column=1)
        
        self.rightparButton = Button(self.rootWindow, text=")", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText(")"))
        self.rightparButton.grid(row=2, column=2)
        
        self.modButton = Button(self.rootWindow, text="MOD", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText(" mod "))
        self.modButton.grid(row=2, column=3)
        
        self.piButton = Button(self.rootWindow, text="Pi", width=self.buttonWidth, height=self.buttonHeight)
        self.piButton.grid(row=2, column=4)
        
        self.sevenButton = Button(self.rootWindow, text="7", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("7"))
        self.sevenButton.grid(row=3, column=0)
        
        self.eightButton = Button(self.rootWindow, text="8", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("8"))
        self.eightButton.grid(row=3, column=1)
        
        self.nineButton = Button(self.rootWindow, text="9", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("9"))
        self.nineButton.grid(row=3, column=2)
        
        self.divideButton = Button(self.rootWindow, text="/", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("/"))
        self.divideButton.grid(row=3, column=3)
        
        self.sqrtButton = Button(self.rootWindow, text="Sqrt", width=self.buttonWidth, height=self.buttonHeight)
        self.sqrtButton.grid(row=3, column=4)
        
        self.fourButton = Button(self.rootWindow, text="4", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("4"))
        self.fourButton.grid(row=4, column=0)
        
        self.fiveButton = Button(self.rootWindow, text="5", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("5"))
        self.fiveButton.grid(row=4, column=1)
        
        self.sixButton = Button(self.rootWindow, text="6", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("6"))
        self.sixButton.grid(row=4, column=2)
        
        self.multiplyButton = Button(self.rootWindow, text="*", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("*"))
        self.multiplyButton.grid(row=4, column=3)
        
        self.powerButton = Button(self.rootWindow, text="x^2", width=self.buttonWidth, height=self.buttonHeight)
        self.powerButton.grid(row=4, column=4)
        
        self.oneButton = Button(self.rootWindow, text="1", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("1"))
        self.oneButton.grid(row=5, column=0)
        
        self.twoButton = Button(self.rootWindow, text="2", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("2"))
        self.twoButton.grid(row=5, column=1)
        
        self.threeButton = Button(self.rootWindow, text="3", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("3"))
        self.threeButton.grid(row=5, column=2)
        
        self.minusButton = Button(self.rootWindow, text="-", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("-"))
        self.minusButton.grid(row=5, column=3)
        
        self.equalButton = Button(self.rootWindow, text="=", width=self.buttonWidth, height=self.buttonHeight * 2 + 1)
        self.equalButton.grid(row=5, column=4, rowspan=2)
        
        self.zeroButton = Button(self.rootWindow, text="0", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("0"))
        self.zeroButton.grid(row=6, column=0)
        
        self.pointButton = Button(self.rootWindow, text=",", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("."))
        self.pointButton.grid(row=6, column=1)
        
        self.percentButton = Button(self.rootWindow, text="%", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("%"))
        self.percentButton.grid(row=6, column=2)
        
        self.plusButton = Button(self.rootWindow, text="+", width=self.buttonWidth, height=self.buttonHeight, command=lambda: self.addText("+"))
        self.plusButton.grid(row=6, column=3)

    def addText(self, str):
        actual = self.screenWindow.get('1.0', 'end-1c')
        actual += str
        self.screenWindow.delete('1.0', 'end')
        self.screenWindow.insert('1.0', actual)
        
    def clearScreen(self):
        self.screenWindow.delete('1.0', 'end')

w = Window()