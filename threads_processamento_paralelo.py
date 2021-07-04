# Executando processamento paralelo no Python.
# Faz com o que o programa faça várias coisas ao mesmo tempo.
# Muito último para trabalhar com interface gráfica. Quando você clicar em
# um botão ele pode travar a tela, nesse caso você pode jogar ele em uma thread
# e deixar o programa rodando sem travar.


from time import sleep
from threading import Thread

"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 2)
t2.start()

t3 = MeuThread('Thread 3', 3)
t3.start()

for i in range(20):
    print(i)
    sleep(1)

# print('Hello')
# for i in range(10):
#    print(i)
#   sleep(.5)
#print('World')

"""


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=('Olá mundo 1', 5))
t.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
