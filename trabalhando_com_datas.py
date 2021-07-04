from datetime import datetime, timedelta

# Documentação:
# https://docs.python.org/2/library/datetime.html

data = datetime(2021, 1, 30, 10, 53, 20)  # ano mês dia minuto segundo
print(data)
print(data.strftime('%d/%m/%y'))
print(data.strftime('%d/%m/%Y'))

# Criando uma data através de uma string
data1 = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(data)
# Pegar o timestamp = contagem de segundos desde 01/01/1900
print(data.timestamp())

# Fazer a data através de um timestamp
data2 = datetime.fromtimestamp(data1.timestamp())
print(data2)

# strptime(str, format)
# objetodedata.strftime(formato)
# timestamp
# Crar uma data fromtimestamp()

# Fazer calculo com datas você deve criar um delta
# Adicinando 5 dias a uma data com o timedelta

data = data + timedelta(days=5, seconds=59)
data = data + timedelta(seconds=2*60*60)
print(data)

# Comparar datas, somar, subtrair

d1 = datetime.strptime('05/07/1987 15:30:14', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('05/07/2021 15:30:14', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif.total_seconds())
print(dif.days)
print(d1.time())
