# 🗂️ Organizador de Arquivos com Interface Gráfica

Um projeto em Python que organiza arquivos locais por categoria e data de modificação, com seleção por interface gráfica e filtro por palavra-chave.

## ✨ Funcionalidades

- 📂 **Organização automática** por tipo de arquivo (imagens, vídeos, documentos, etc.)
- 🗓️ **Agrupamento por data** de modificação (ano e mês)
- 🔍 **Filtro por palavra-chave**
- 🖱️ **Interface gráfica** para seleção de arquivos e entrada de filtro (`tkinter`)
- 📊 **Barra de progresso** com `tqdm`
- 📁 Cria uma pasta chamada `organizado/` no mesmo diretório do script com todos os arquivos organizados

## 📌 Tecnologias utilizadas

- Python 3
- `tkinter` para interface gráfica
- `shutil` e `os` para manipulação de arquivos e diretórios
- `tqdm` para barra de progresso
- `uuid` para evitar nomes duplicados

## 📥 Como usar

1. Certifique-se de ter o Python 3 instalado.
2. Instale o `tqdm` se necessário:
   ```bash
   pip install tqd

   #"Aquilo que não é bem organizado, deve ser classificado." – (não foi o Schopenhauer, mas poderia ter sido)"
