print('Что надеть, учитывая погодные условия?')
isRain = None
temperature = int(input('Сколько градусов на улице?\n'))
rainFall = None
if 20 <= temperature <= 30:
    isRain = input("Есть ли дождь?: ") == "да"
    if isRain:
        print('Футболку, шорты и дождевик')
    else:
        print('Футболку и шорты')
else:
    if temperature > 0:
        isRain = input("Есть ли дождь?: ") == "да"
        if isRain:
            rainFall = input("Сильный ли дождь?: ") == "да"
            if rainFall:
                print('Пальто, резиновые сапоги и зонт')
            else:
                print('Пальто и дождевик')
        else:
            print('Пальто')
    else:
        print('Пуховик')
