hora = input('Digite uma quantidade em horas: ')
hora = int(hora)
minuto = input('Digite uma quantidade em minutos: ')
minuto = int(minuto)
segundo = input('Digite uma quantidade em segundos: ')
segundo = int(segundo)

total_segundos = ((hora * 60) * 60) + (minuto * 60) + segundo
print(f'Total de segundos: {total_segundos}')
