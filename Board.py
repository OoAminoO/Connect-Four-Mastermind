from math import inf
from tkinter import *
import time
import Utils

from Main import firstTurnIsSelected
from Main import userDropPiece


defColor  = "#F2F2F2"     # background of the Board


window = Tk()
def showBoard(window) :
    window.title("Connect Four")
    window.configure(background = defColor)
    window.geometry('650x550')


def displayTurnButtons(window) :
    btnUserFirst = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgUserStarts)
    btnUserFirst.place(x = 215, y = 200)
    btnAIFirst = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgAIStarts)
    btnAIFirst.place(x = 215, y = 200 + 60 + 30)
    btnUserFirst.configure(command = lambda : firstTurnIsSelected(btnUserFirst, btnAIFirst, Utils.userPiece))
    btnAIFirst.configure(command = lambda : firstTurnIsSelected(btnUserFirst, btnAIFirst, Utils.AIPiece))


def displayLabelTurn():
    if Utils.turn == Utils.userPiece:
        Utils.lblTurn.config(image = imgUserTurn)
    elif Utils.turn == Utils.AIPiece:
        Utils.lblTurn.config(image = imgAITurn)

def displayWinner(winner):
    Utils.lblTurn.destroy()
    if winner == -1:
        Utils.lblWinner = Label(window, border = 0, bg = defColor, image = imgUserWon)
    elif winner == 1:
        Utils.lblWinner = Label(window, border = 0, bg = defColor, image = imgAIWon)
    elif winner == 0:
        Utils.lblWinner = Label(window, border = 0, bg = defColor, image = imgTie)
    Utils.lblWinner.place(x = 225 ,y = 453)

# ------------- Hover Begins ------------- #
# When mouse hover on one of the 42 buttons
def putHover(x) :
    # x is the column number over which the mouse hovers
    # notColored is the list of button numbers within the column
    #    which are not occupied
    notColored = [number for number in range(x, x + 6) if Utils.overallPosition[number] == 0]
    for number in notColored :
        Utils.btnList[number].config(image = imgHoverPiece)
        
# When mouse leaves one of the 42 buttons
def delHover(x) :
    notColored = [number for number in range(x, x + 6) if Utils.overallPosition[number] == 0]
    for number in notColored :
        Utils.btnList[number].config(image = imgEmptyPiece)

# Assign Hover rules to the 42 buttons
def settingHover(buttonList) :
    counter = 0
    for buttonNumber in buttonList.keys() :
        buttonList[buttonNumber].bind("<Enter>", lambda event, buttonNumber = buttonNumber : putHover((buttonNumber//7) * 7))
        buttonList[buttonNumber].bind("<Leave>", lambda event, buttonNumber = buttonNumber : delHover((buttonNumber//7) * 7))
        buttonList[buttonNumber].configure(command = lambda buttonNumber = buttonNumber : userDropPiece((buttonNumber//7) * 7))
        counter += 1
        counter = counter % 7
# ------------- Hover Ends ------------- #




def createButtons():
    firstCellX = 105
    firstCellY = 50


    #----------------------------------------------- First row begins
    btn5 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn5.place(x = firstCellX + 65 * 0, y = firstCellY)

    btn12 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn12.place(x = firstCellX + 65 * 1, y = firstCellY)

    btn19 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn19.place(x = firstCellX + 65 * 2, y = firstCellY)

    btn26 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn26.place(x = firstCellX + 65 * 3, y = firstCellY)

    btn33 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn33.place(x = firstCellX + 65 * 4, y = firstCellY)

    btn40 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn40.place(x = firstCellX + 65 * 5, y = firstCellY)

    btn47 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn47.place(x = firstCellX + 65 * 6, y = firstCellY)

    Utils.btnList[5], Utils.btnList[12], Utils.btnList[19], Utils.btnList[26] = btn5, btn12, btn19, btn26
    Utils.btnList[33], Utils.btnList[40], Utils.btnList[47] = btn33, btn40, btn47
    #----------------------------------------------- First row ends


    
    #----------------------------------------------- Second row begins
    btn4 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn4.place(x = firstCellX + 65 * 0, y = firstCellY + 65)

    btn11 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn11.place(x = firstCellX + 65 * 1, y = firstCellY + 65)

    btn18 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn18.place(x = firstCellX + 65 * 2, y = firstCellY + 65)

    btn25 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn25.place(x = firstCellX + 65 * 3, y = firstCellY + 65)

    btn32 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn32.place(x = firstCellX + 65 * 4, y = firstCellY + 65)

    btn39 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn39.place(x = firstCellX + 65 * 5, y = firstCellY + 65)

    btn46 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn46.place(x = firstCellX + 65 * 6, y = firstCellY + 65)

    Utils.btnList[4], Utils.btnList[11], Utils.btnList[18], Utils.btnList[25] = btn4, btn11, btn18, btn25
    Utils.btnList[32], Utils.btnList[39], Utils.btnList[46] = btn32, btn39, btn46
    #----------------------------------------------- Second row ends


    
    #----------------------------------------------- Third row begins
    btn3 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn3.place(x = firstCellX + 65 * 0, y = firstCellY + 65 * 2)

    btn10 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn10.place(x = firstCellX + 65 * 1, y = firstCellY + 65 * 2)

    btn17 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn17.place(x = firstCellX + 65 * 2, y = firstCellY + 65 * 2)

    btn24 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn24.place(x = firstCellX + 65 * 3, y = firstCellY + 65 * 2)

    btn31 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn31.place(x = firstCellX + 65 * 4, y = firstCellY + 65 * 2)

    btn38 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn38.place(x = firstCellX + 65 * 5, y = firstCellY + 65 * 2)

    btn45 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn45.place(x = firstCellX + 65 * 6, y = firstCellY + 65 * 2)

    Utils.btnList[3], Utils.btnList[10], Utils.btnList[17], Utils.btnList[24] = btn3, btn10, btn17, btn24
    Utils.btnList[31], Utils.btnList[38], Utils.btnList[45] = btn31, btn38, btn45
    #----------------------------------------------- Third row ends


    
    #----------------------------------------------- Fourth row begins
    btn2 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn2.place(x = firstCellX + 65 * 0, y = firstCellY + 65 * 3)

    btn9 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn9.place(x = firstCellX + 65 * 1, y = firstCellY + 65 * 3)

    btn16 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn16.place(x = firstCellX + 65 * 2, y = firstCellY + 65 * 3)

    btn23 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn23.place(x = firstCellX + 65 * 3, y = firstCellY + 65 * 3)

    btn30 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn30.place(x = firstCellX + 65 * 4, y = firstCellY + 65 * 3)

    btn37 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn37.place(x = firstCellX + 65 * 5, y = firstCellY + 65 * 3)

    btn44 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn44.place(x = firstCellX + 65 * 6, y = firstCellY + 65 * 3)

    Utils.btnList[2], Utils.btnList[9], Utils.btnList[16], Utils.btnList[23] = btn2, btn9, btn16, btn23
    Utils.btnList[30], Utils.btnList[37], Utils.btnList[44] = btn30, btn37, btn44
    #----------------------------------------------- Fourth row ends


    
    #----------------------------------------------- Fifth row begins
    btn1 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn1.place(x = firstCellX + 65 * 0, y = firstCellY + 65 * 4)

    btn8 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn8.place(x = firstCellX + 65 * 1, y = firstCellY + 65 * 4)

    btn15 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn15.place(x = firstCellX + 65 * 2, y = firstCellY + 65 * 4)

    btn22 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn22.place(x = firstCellX + 65 * 3, y = firstCellY + 65 * 4)

    btn29 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn29.place(x = firstCellX + 65 * 4, y = firstCellY + 65 * 4)

    btn36 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn36.place(x = firstCellX + 65 * 5, y = firstCellY + 65 * 4)

    btn43 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn43.place(x = firstCellX + 65 * 6, y = firstCellY + 65 * 4)

    Utils.btnList[1], Utils.btnList[8], Utils.btnList[15], Utils.btnList[22] = btn1, btn8, btn15, btn22
    Utils.btnList[29], Utils.btnList[36], Utils.btnList[43] = btn29, btn36, btn43
    #----------------------------------------------- Fifth row ends


    
    #----------------------------------------------- Sixth row begins
    btn0 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn0.place(x = firstCellX + 65 * 0, y = firstCellY + 65 * 5)

    btn7 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn7.place(x = firstCellX + 65 * 1, y = firstCellY + 65 * 5)

    btn14 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn14.place(x = firstCellX + 65 * 2, y = firstCellY + 65 * 5)

    btn21 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn21.place(x = firstCellX + 65 * 3, y = firstCellY + 65 * 5)

    btn28 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn28.place(x = firstCellX + 65 * 4, y = firstCellY + 65 * 5)

    btn35 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn35.place(x = firstCellX + 65 * 5, y = firstCellY + 65 * 5)

    btn42 = Button(window, border = 0, cursor = "hand2", bg = defColor, image = imgEmptyPiece)
    btn42.place(x = firstCellX + 65 * 6, y = firstCellY + 65 * 5)

    Utils.btnList[0], Utils.btnList[7], Utils.btnList[14], Utils.btnList[21] = btn0, btn7, btn14, btn21
    Utils.btnList[28], Utils.btnList[35], Utils.btnList[42] = btn28, btn35, btn42
    #----------------------------------------------- Sixth row ends
    
    
    Utils.lblTurn = Label(window, border = 0, bg = defColor)
    Utils.lblTurn.place(x = 250 ,y = 462)
    displayLabelTurn()




showBoard(window)
Utils.imgAIPiece = PhotoImage(file = "Graphics/AIPiece.png")
Utils.imgUserPiece = PhotoImage(file = "Graphics/userPiece.png")
Utils.imgAIPieceStar = PhotoImage(file = "Graphics/AIPieceStar.png")
Utils.imgUserPieceStar = PhotoImage(file = "Graphics/userPieceStar.png")
imgEmptyPiece = PhotoImage(file = "Graphics/emptyPiece.png")
imgHoverPiece = PhotoImage(file = "Graphics/hoverPiece.png")
imgUserTurn = PhotoImage(file = "Graphics/userTurn.png")
imgAITurn = PhotoImage(file = "Graphics/AITurn.png")
imgUserStarts = PhotoImage(file = "Graphics/userStarts.png")
imgAIStarts = PhotoImage(file = "Graphics/AIStarts.png")
imgAIWon = PhotoImage(file = "Graphics/AIWon.png")
imgUserWon = PhotoImage(file = "Graphics/userWon.png")
imgTie = PhotoImage(file = "Graphics/Tie.png")
displayTurnButtons(window)
window.mainloop()







