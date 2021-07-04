# https://ffmpeg.org/documentation.html
# Download para windows>:  https://ffmpeg.org/download.html
"""
ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf23 -preset ultrafast -c:a aac
-b:a 320k -c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""
import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'


codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = r'C:\Users\leleu\Videos\Family Guy Season 1 - Complete'
caminho_destino = r'C:\Users\leleu\Videos_convertidos'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.avi'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        arquivo_saida = f'{caminho_destino}\\{nome_arquivo}_NOVO{ext_arquivo}'

        comando = \
            f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda}'\
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio}'\
            f'{debug} {map_legenda} "{arquivo_saida}"'
        
        #print(comando)
        os.system(comando)
        #print('Arquivos convertidos com sucesso!')
        
