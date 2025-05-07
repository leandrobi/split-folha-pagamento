# streamlit_app.py

import streamlit as st
import re
import io
import zipfile
import fitz  # PyMuPDF

def sanitize(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def extract_name(text: str) -> str:
    m = re.search(r'Func\.\:\s*\d+\s*-\s*(.+)', text)
    if m:
        return m.group(1).strip()
    for line in text.splitlines():
        if line.isupper() and len(line.split()) >= 2:
            return line.strip()
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return "page"

def main():
    st.title("Split de Folha de Pagamento")

    st.write("""
    Este app não armazena e não manda nenhum dado recebido para o servidor.
    As informações são processadas para e somente pelo usuário da sessão.
    """)

    # Mês e ano lado a lado
    col1, col2 = st.columns(2)
    with col1:
        month = st.number_input("Mês (1–12)", 1, 12, 4, format="%d")
    with col2:
        year  = st.number_input("Ano (>=2000)", 2000, 2100, 2025, format="%d")
    prefix = f"{month:02d}{year}"

    uploaded = st.file_uploader("👆 Faça upload do PDF de demonstrativo", type="pdf")
    if not uploaded:
        return

    if st.button("Gerar e Baixar ZIP"):
        pdf_bytes = uploaded.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        name_counts = {}

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zf:
            for i in range(doc.page_count):
                page = doc.load_page(i)
                text = page.get_text("text")
                raw_name = extract_name(text)
                base_name = sanitize(raw_name)

                # evita duplicatas
                cnt = name_counts.get(base_name, 0) + 1
                name_counts[base_name] = cnt
                body = f"{base_name}.pdf" if cnt == 1 else f"{base_name}_{cnt}.pdf"
                filename = f"{prefix}_{body}"

                # gera PDF de uma página
                new_doc = fitz.open()
                new_doc.insert_pdf(doc, from_page=i, to_page=i)
                pdf_out = new_doc.write()

                # adiciona ao ZIP
                zf.writestr(filename, pdf_out)

        zip_buffer.seek(0)
        st.download_button(
            label="📦 Baixar todos os PDFs em ZIP",
            data=zip_buffer,
            file_name=f"{prefix}_payslips.zip",
            mime="application/zip"
        )

if __name__ == "__main__":
    main()
