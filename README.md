# Split de Folha de Pagamento por Funcionário

Este projeto é uma aplicação web simples construída com Streamlit que permite dividir um arquivo PDF de demonstrativo de pagamento em PDFs individuais por funcionário e compactá-los em um arquivo ZIP para download.

## Funcionalidades

- Upload de arquivo PDF de demonstrativo de pagamento
- Extração automática do nome do funcionário a partir do texto de cada página
- Geração de arquivos PDF de uma página para cada funcionário
- Compactação de todos os PDFs em um único arquivo ZIP

## Instalação

```bash
# Clone este repositório
git clone <URL-do-repositório>
cd <nome-do-repositório>

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install streamlit pymupdf
```

## Uso

```bash
streamlit run main.py
```

1. No navegador, faça o upload do PDF de demonstrativo.
2. Clique em "Gerar e Baixar ZIP" para obter os PDFs individuais em um arquivo ZIP.

## Estrutura do projeto

- `main.py`: script principal com a aplicação Streamlit.
- `README.md`: documentação do projeto.

## Dependências

- [Streamlit](https://streamlit.io/)
- [PyMuPDF (fitz)](https://pypi.org/project/PyMuPDF/) 