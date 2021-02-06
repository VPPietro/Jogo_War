#INPUT!
entrada = str(input('digite a hora (HHMMSS, formato 24h e somente numeros!) '))
hora = int(entrada[0:2])
minuto = int(entrada[2:4])
segundo = int(entrada[4:6])
#hora = int(input('digite a hora atual (formato 24h): '))
#minuto = int(input('digite o minuto atual (m) '))
#segundo = int(input('digite o segundo atual(s) '))
#input de variavel, sera possivel de melhor forma?

#confirmacao
print(f'a hora atual: {str(hora).zfill(2)}:{str(minuto).zfill(2)}:{str(segundo).zfill(2)}')

#entrada de duração do procedimento
duracao = int(input('digite quanto tempo de duração do procedimento (s): '))

#calculo e print
hora = hora * 3600
minuto = minuto * 60
duracao = duracao + int(hora) + int(minuto) + int(segundo)
print(f'horario de termino: {str(duracao // 3600).zfill(2)}:{str((duracao % 3600) // 60).zfill(2)}:{str((duracao % 3600) % 60).zfill(2)}')
print('yeah modafocka')

