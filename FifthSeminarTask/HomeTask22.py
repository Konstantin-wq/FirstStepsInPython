# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

amount_sweets = 2021
max_amount_per_motion = 28
priority = 0


first_player = input('Введите имя первого игрока: ')
second_player = input('Введите имя второго игрока: ')
print(f'Играют {first_player} и {second_player}')

print('Бросим жребий:')
score = random.randint(1, 2)
if score == 1:
    first_player_move = first_player
    second_player_move = second_player
    print(f'Первым ходит {first_player}')
else:
    first_player_move = second_player
    second_player_move = first_player
    print(f'Первым ходит {second_player}')

while amount_sweets > 0:
    if priority == 0:
        amount_per_step = int(
            input(f'{first_player_move} какое количество конфет будете забирать?'))
        if amount_per_step > max_amount_per_motion or amount_per_step > amount_sweets:
            print(f'{first_player_move} у Вас перебор попробуйте другое количество ')
            amount_per_step = int(
                input(f'{first_player_move} какое количество конфет будете забирать?'))
        amount_sweets = amount_sweets - amount_per_step
        priority = priority+1
        if amount_sweets > 0:
            print(f'В игре еще {amount_sweets} конфет')

        else:
            if amount_sweets == 0:
                print("Конфеты кончились")
                priority = priority-1
                break

    if priority == 1:
        amount_per_step = int(
            input(f'{second_player_move} какое количество конфет будете забирать?'))
        if amount_per_step > max_amount_per_motion or amount_per_step > amount_sweets:
            print(f'{second_player_move} у Вас перебор попробуйте другое количество ')
            amount_per_step = int(
                input(f'{second_player_move} какое количество конфет будете забирать?'))
        amount_sweets = amount_sweets - amount_per_step
        priority = priority-1
        if amount_sweets > 0:
            print(f'В игре еще {amount_sweets} конфет')
        else:
            if amount_sweets == 0:
                print("Конфеты кончились")
                priority = priority+1
                break
if priority == 1:
    print(f'{second_player_move} победитель')
if priority == 0:
    print(f'{first_player_move} победитель')
