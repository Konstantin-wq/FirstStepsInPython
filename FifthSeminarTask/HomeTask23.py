# Создайте программу для игры в ""Крестики-нолики""


print('Играем в крестики - нолики')
first_player = input('Первый игрок, введите ваше имя ')
second_player = input('Второй игрок, введите ваше имя ')

board = list(range(1, 10))

def draw_table(board):
    print('-' * 13)
    for i in range(3):
        print("|", board[0 + i*3], "|",
              board[1 + i*3], "|", board[2 + i*3], "|")
        print('-'*13)

win_combinatios = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]



game_end = False
while game_end == False:
    draw_table(board)
    
    print(f'Ходит {first_player}')
    elem = 'X'
    step = int(input(f'{first_player} сделайте ход '))    
    table_position = board.index(step)
    board[table_position] = elem
    draw_table(board)

    print(f'Ходит {second_player}')   
    elem = '0'
    step = int(input(f'{second_player} сделайте ход '))   
    table_position = board.index(step)
    board[table_position] = elem
    draw_table(board) 
    
    win = ''
    for i in win_combinatios:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O" 
    if win != '':
        game_end = True
    else:
        game_end = False

print(f'Игра окончена, победил {win}')
    