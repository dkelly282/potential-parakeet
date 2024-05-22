
#Average BP score calculator
print("This program calculates the overall average from a number of BP readings\n")
sys_readings = 0
dia_readings = 0

number = (int(input('How many BP readings do you want to enter? ')))

for i in range(number):
    
    print(f'\nReading number:{i + 1}')
    
    sys_readings += int(input('Enter systolic reading ' ))
    dia_readings += int(input('Enter diastolic reading ' ))

average_sys = int(sys_readings/number)
average_dia = int (dia_readings/number)

print(f'Average systolic reading is: {average_sys}')
print(f'Average diastolic reading is: {average_dia}')