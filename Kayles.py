from tkinter import *
from tkinter import messagebox

#general setup
window = Tk()
window.geometry('900x400')
window.configure(bg='grey')

#initializing counter and player variables
turn_counter = 0
counter = 0

player = True

#enables all buttons
def enable():
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)
    b8.config(state=NORMAL)
    b9.config(state=NORMAL)

#disables buttons that are not adjacent to the currently chosen button
def disable_non_adj(b):
    if b == b1:
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
    if b == b2:
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
    if b == b3:
        b1.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
    if b == b4:
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
    if b == b5:
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
    if b == b6:
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
    if b == b7:
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b9.config(state=DISABLED)
    if b == b8:
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)

    if b == b9:
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)


#enables all the buttons and resets all the text
def reset():
    global turn_counter, counter, player
    turn_counter = 0
    counter = 0
    player = True
    enable()
    b1['text'] = '1'
    b2['text'] = '2'
    b3['text'] = '3'
    b4['text'] = '4'
    b5['text'] = '5'
    b6['text'] = '6'
    b7['text'] = '7'
    b8['text'] = '8'
    b9['text'] = '9'


#uses the turn counter to switch to the other player
def switch():
    global player, turn_counter
    turn_counter = 0
    if player == True:
        player = False
    elif player == False:
        player = True
    print("player : ", player)
    enable()


#checks if a button has been clicked and disables the adjacent buttons
#checks if there is a winner and if the button selected is valid
def b_click(b):
    global counter, turn_counter
    if turn_counter == 0:
        disable_non_adj(b)
    print("Turn counter : ", turn_counter)


    check_winner()

    if b['text'] != '-':
        b['text'] = '-'
        turn_counter += 1
        counter += 1

    if turn_counter == 2:
        turn_counter = 0
        switch()
        print("counter : ", counter)

        
#checks if the counter's value is 8, if it is then the player won
#displays message box displaying the winning player
def check_winner():
    if counter == 8:
        if player:
            messagebox.showinfo("Kayle's Game", "PLAYER ONE WON")
        if not player:
            messagebox.showinfo("Kayle's Game", "PLAYER TWO WON")


#creating and placing the buttons and the main label
explanation = Label(window, text="WELCOME TO KAYLE'S GAME\n"
                                 "Rules : A player is able to remove one or two adjacent tokens\n"
                                 "The last player to remove a token wins\n", font="none 14 bold")
explanation.place(x=200, y=20)

switch_btn = Button(window, text="Switch", font='none 15 bold', height=2, width=8, command=switch)
switch_btn.place(x=400, y=300)

reset_btn = Button(window, text="Reset", font='none 15 bold', height=2, width=8, command=reset)
reset_btn.place(x=700, y=300)

b1 = Button(window, text="1", font='none 15 bold', height=4, width=8, command=lambda: b_click(b1))
b2 = Button(window, text="2", font='none 15 bold', height=4, width=8, command=lambda: b_click(b2))
b3 = Button(window, text="3", font='none 15 bold', height=4, width=8, command=lambda: b_click(b3))
b4 = Button(window, text="4", font='none 15 bold', height=4, width=8, command=lambda: b_click(b4))
b5 = Button(window, text="5", font='none 15 bold', height=4, width=8, command=lambda: b_click(b5))
b6 = Button(window, text="6", font='none 15 bold', height=4, width=8, command=lambda: b_click(b6))
b7 = Button(window, text="7", font='none 15 bold', height=4, width=8, command=lambda: b_click(b7))
b8 = Button(window, text="8", font='none 15 bold', height=4, width=8, command=lambda: b_click(b8))
b9 = Button(window, text="9", font='none 15 bold', height=4, width=8, command=lambda: b_click(b9))
b1.place(x=0, y=200, anchor='w')
b2.place(x=100, y=200, anchor='w')
b3.place(x=100 * 2, y=200, anchor='w')
b4.place(x=100 * 3, y=200, anchor='w')
b5.place(x=100 * 4, y=200, anchor='w')
b6.place(x=100 * 5, y=200, anchor='w')
b7.place(x=100 * 6, y=200, anchor='w')
b8.place(x=100 * 7, y=200, anchor='w')
b9.place(x=100 * 8, y=200, anchor='w')

#looping the program
window.mainloop()
