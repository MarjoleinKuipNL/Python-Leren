temperature = 90
graden_celcius  = (temperature - 32) / 1.8
if temperature < 60:
    print('Bring a jacket')
    print('graden_celcius = ', graden_celcius)
else:
    print('Don\'t bring a jacket')
    print('graden_celcius = ', round(graden_celcius))