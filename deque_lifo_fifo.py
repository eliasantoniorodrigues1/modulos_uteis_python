# Trabalhando com LIFO e FIFO
""""
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que estão adicionados um sobre o outro

Fila (queue) - FIFO - first in, first ou.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)

Filas pode ter efeitos colaterais em desempenho, porque a cada item alterado, todos serão modificados.

"""

# Conceito de Pilha com listas:
# livros = list()
#
# livros.append('Livro 1')  # 1ª
# livros.append('Livro 2')  # 2ª
# livros.append('Livro 3')  # 3ª
# livros.append('Livro 4')  # 4ª
# livros.append('Livro 5')  # 5ª
# print(livros)
#
# livro_removido = livros.pop()  # 5ª
# livro_removido = livros.pop()  # 4ª
# livro_removido = livros.pop()  # 3ª
#
# print(livros, livro_removido)


# Fila - FIFO (first in, first out)
# Estrutura de dados de auto desempenho estão dentro da biblioteca collections
from collections import deque

fila = deque()
fila.append('Joãzinho')
fila.append('Maria')
fila.append('Elias')
fila.append('Jose')
fila.append('Marcos')

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

print(fila)

# Você pode adicionar um valor máximo para a lista e toda vez que for adicionado um novo elemento
# O elemento mais antigo é removido da fila.
fila2 = deque(maxlen=5)
fila2.extend([1, 2, 3, 4, 5])
fila2.append(6)
print(fila2)
# fila2.insert(2, 'Elias')
# extendleft fura a fila, inserindo os elementos a esquerda da fila.
# fila2.rotate -> rotaciona dois elementos da lista pelo quantidade de elementos
# fila2.reverse -> inverte a fila

