print('Celsius to Fahrenheit', '\n')
print('Celsius','\t','Fahrenheit')
print('-------------------------')
for celsius in range(0, 20):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, '\t','|','\t' ,fahrenheit)