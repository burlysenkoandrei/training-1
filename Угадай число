import random
print ('я загадал число от 1 до 50. Попробуй угадать.У тебя 6 попыток')
win = 0
lose = 0
while True:
    x=random.randint(1,50)
    for i in range(6):
        y=int(input(f'Попытка {i+1}. Введите число'))
        if x > y:
            print('Больше')
        elif x < y:
            print('Меньше')
        else:
            print('Верно!!!')
            win = win+1
            break
    else: 
        print (f'Не угадал(( Число было {x}')
        lose = lose+1
    answer = input(f'Текущий счет: {win} побед {lose} поражений. Хотите сыграть еще раз? (да/нет): ')
    if answer.lower() == "нет":
        break 
    elif answer.lower() != "да":
        input("Не понял. Повторите пожалуйста (да/нет):")
