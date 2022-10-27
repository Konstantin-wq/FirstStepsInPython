

from tkinter import *


game_window = Tk()
game_window.title('Крестики - нолики')
game_window.geometry('350x350')
player1 = Label(game_window, text="Player1 : X")
player1.grid(row=0, column=1)
player2 = Label(game_window, text="player2 : O")
player2.grid(row=0, column=2)

game_field = Canvas(game_window, width=300, height=300,
                    bg='azure')  # создаем объект-холст
game_field.place(x=25, y=25)
for i in range(0, 9):
    x = i//3*100
    y = i % 3*100
    game_field.create_rectangle(
        x, y, x+100, y+100, width=3)  # создаем прямоугольники

table_position = [None] * 9
win = None
win_combinatios = [(0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6)]






def drawing_X(col, row):
    x = 10 + 100*col
    y = 10+100*row
    game_field.create_line(x, y, x+80, y+80, width=6, fill='red')
    game_field.create_line(x, y+80, x+80, y, width=6, fill='red')


def drawing_O(col,row):
    x = 10+100*col
    y = 10+100*row
    game_field.create_oval(x,y,x+80,y+80,width=6,outline='blue')

def click_X(event):
    column = event.x // 100
    row = event.y //100
    i = column + row*3
    if table_position[i] is None:
        table_position[i] = 'X'
        drawing_X(column,row)
    else:
        click_X
    print(table_position)
    if win_check():
        ending()
    else:    
        click_0
    
    

def click_0(event):
    column = event.x // 100
    row = event.y //100 
    i = column + row*3
    if table_position[i] is None:
        table_position[i] = '0'
        drawing_O(column,row)
    else:
        click_0
    print(table_position)          
    if win_check():
        ending()
    else:
        click_X


def win_check():   
    global win
    current_game_comb = []  
   
    for i in win_combinatios:
        current_game_comb.append([table_position[i[0]],table_position[i[1]],table_position[i[2]]])
    if ['X']*3 in current_game_comb:
        win = 'Победил Player1'
    elif['0']*3 in current_game_comb:
        win = 'Победил Player2'
    elif None not in current_game_comb:
        win = 'Ничья'
        
    return win

def ending():
    print(f'Победил {win}')    








game_field.bind('<Button-1>', click_X)
game_field.bind('<Button-3>', click_0)

game_window.mainloop()



