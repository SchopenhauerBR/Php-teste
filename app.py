import sys
print("🔍 Python usado:", sys.executable)
import os
import shutil
import time
from tkinter import Tk, filedialog
from tqdm import tqdm
import uuid

# Caminho base
caminho_base = os.path.join(os.getcwd(), "organizado")
os.makedirs(caminho_base, exist_ok=True)

# Upload local
Tk().withdraw()
from tkinter import simpledialog

# Pergunta a palavra-chave com interface gráfica
filtro = simpledialog.askstring("Filtro", "digite uma palavra-chave para filtrar os arquivos (ou deixe em braco para todos): ")
filtro = filtro.lower() if filtro else ""
arquivos_selecionados = filedialog.askopenfilenames(title="Selecione os arquivos")

# Categorias
tipos = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Vídeos': ['.mp4'],
    'Músicas': ['.mp3'],
    'PDFs': ['.pdf'],
    'Planilhas': ['.xls', '.xlsx', '.csv'],
    'Documentos': ['.doc', '.txt', '.docx', '.pptx'],
    'Compactados': ['.zip', '.rar'],
    'Outros': []
}
contador = {categoria: 0 for categoria in tipos}


# Organiza
for caminho_arquivo in tqdm(arquivos_selecionados, desc="Organizando"):
    nome_arquivo = os.path.basename(caminho_arquivo)
    if filtro and filtro not in nome_arquivo.lower():
        continue

    extensao = os.path.splitext(nome_arquivo)[1].lower()
    destino = next((cat for cat, ext in tipos.items() if extensao in ext), 'Outros')

    data_mod = os.path.getmtime(caminho_arquivo)
    pasta_data = time.strftime("%Y-%m", time.localtime(data_mod))
    pasta_destino = os.path.join(caminho_base, destino, pasta_data)
    os.makedirs(pasta_destino, exist_ok=True)

    novo_nome = nome_arquivo
    caminho_final = os.path.join(pasta_destino, novo_nome)

    if os.path.exists(caminho_final):
        novo_nome = f"{uuid.uuid4().hex}_{nome_arquivo}"
        caminho_final = os.path.join(pasta_destino, novo_nome)

    shutil.copy2(caminho_arquivo, caminho_final)
    contador[destino] += 1

# Relatório
print("\n📊 Relatório:")
for categoria, qtd in sorted(contador.items(), key=lambda x: x[1], reverse=True):
    print(f"  {categoria}: {qtd} arquivo(s)")

print(f"\n📁 Arquivos organizados em: {caminho_base}")