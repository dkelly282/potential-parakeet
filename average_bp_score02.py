
#Average BP score calculator

sys_readings = []
dia_readings = []

number = (int(input('How many bp readings do you want to enter?')))

for i in range(number):
    
    print(f'Reading number:{i + 1}')
    
    sys_readings.append(int(input('Enter systolic reading ' )))
    dia_readings.append(int(input('Enter diastolic reading: ')))

average_sys = (int(sum(sys_readings)/number))
average_dia = (int(sum(dia_readings)/number))

print(f'Average systolic reading is: {average_sys}')
print(f'Average diastolic reading is: {average_dia}')

   






