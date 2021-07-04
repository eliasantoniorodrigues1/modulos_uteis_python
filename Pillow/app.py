import os  # Biblioteca para caminhar nos diretorios
from PIL import Image  # Biblioteca para tratamento de imagens


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe.')

    for root, dir, files in os.walk(main_images_folder):
        for file in files:
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            # converted_tag = '_REDIM'

            new_file = file_name + extension
            new_file_full_path = os.path.join(root.replace('Original', 'Hikivision'), new_file)

            # if converted_tag in new_file_full_path:
            #     os.remove(new_file_full_path)
            # continue

            # Evitando que seja gerado duplicidade
            # if converted_tag in new_file_full_path:
            #     continue

            # Abrindo a imagem com Pillow
            img_pillow = Image.open(file_full_path)
            width, height = img_pillow.size
            # Definindo a nova altura e nova largura
            new_height = round(new_width * height / width)

            # Redimensionando a imagem
            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS
            )
            # Salva imagem redimensionada com o exif (Dados detalhados da imagem)
            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=100,
                # exif=img_pillow.info['exif']  # As minhas imagens não possuem exif
                )
            new_image.close()
            img_pillow.close()
            print(f'{new_file_full_path} arquivo redimensionado com sucesso!')


if __name__ == '__main__':
    imagens_originais = 'D:/Projetos/17 - Programação/Projetos/resolucao_fotos_aec\Fotos Foracesso\Original'
    main(imagens_originais, new_width=310)
    # dimensões 310 x 400 96 dpi 24 bits de produndidade e 80 pixels entre púpilas.
