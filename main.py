import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

listar_arquivos = os.listdir(caminho)

locais = {
    "documentos": [".docx", ".doc"],
    "pdfs": [".pdf"],
    "videos": [".mp4"],
    "imagens": [".jpg", "png"],
    "planilhas": [".xlsx"]
}

for arquivo in listar_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")