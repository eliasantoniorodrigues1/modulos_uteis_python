# os e shutil
# shutil.move(old_file_path, new_file_path)  # Move e renomeia
# os.remove(new_file_path)
# shutil.copy(caminho_original, caminho_novo)  # Copia os arquivos
import os
import shutil

# Caminho do windows adicionar um r no caminho do windows
# para que ele não tente executar as barras invertidas

caminho_original = r'C:\Users\leleu\Imagens'
caminho_novo = r'C:\Users\leleu\Imagens_2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasa {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        if '.jpg' in file:
            # shutil.move(old_file_path, new_file_path)  # Move e renomeia
            # os.remove(new_file_path)
            shutil.copy(caminho_original, caminho_novo)  # Copia os arquivos

            print(old_file_path, new_file_path)

