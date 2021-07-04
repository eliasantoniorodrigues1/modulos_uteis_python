# Documentação:
# https://pythonhosted.org/PyPDF2/
# Exemplos de uso:
# http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
# Caminho dos pdfs:
# D:\Cursos\Luiz_Otavio_Miranda\Python\Modulos\trabalhandopdf\pdf
# pip install pypdf2
import PyPDF2
import os

caminho = r'D:\Cursos\Luiz_Otavio_Miranda\Python\Modulos\trabalhandopdf\pdf'

# Unindo arquivos PDFs
"""
novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho):
    for file in files:
        caminho_completo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo, 'rb')
        novo_pdf.append(arquivo_pdf)


with open(f'{caminho}\\novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""

# Separando arquivos PDFs
with open(f'{caminho}\\novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'D:\\Cursos\\Luiz_Otavio_Miranda\\Python\\Modulos\\trabalhandopdf\\novos_pdfs\\{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
