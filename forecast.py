def check_temp(temp):
    if temp < 15:
        print('Wear a jacket')
    elif temp >= 15 and temp <= 35:
        print('pack a jacket')
    elif temp >= 35:
        print('Please leave your jacket at home otherwise you will be sufficated.')
print(check_temp(10))
print(check_temp(15))
print(check_temp(20))
print(check_temp(25))
print(check_temp(30))
print(check_temp(35))
print(check_temp(40)) #last test