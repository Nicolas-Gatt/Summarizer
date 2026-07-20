import streamlit as st
from utils import extrair_video_id, extrair_transcricao

# Configuração da página web
st.set_page_config(page_title="Summarizer", page_icon="🎥", layout="centered")

st.title("🎥 Summarizer")
st.write("Cole o link do vídeo do YouTube para gerar a transcrição e resumo.")

url_input = st.text_input("Link do vídeo do YouTube", placeholder="Cole o link aqui...")

if st.button("Transcrever", type="primary"):
    if not url_input.strip():
        st.warning("Por favor, insira um link do vídeo do YouTube.")
    else:
        video_id = extrair_video_id(url_input)

        if not video_id:
            st.error("Erro: O link fornecido não é válido. Certifique-se de que é um link do YouTube.")
        else:
            with st.spinner("Buscando transcrição..."):
                transcricao = extrair_transcricao(video_id)

            if transcricao.startswith("Erro:"):
                st.error(transcricao)
            else:
                st.success("Transcrição extraída com sucesso!")
                st.subheader("Transcrição:")
                st.text_area(
                    "Transcrição do vídeo", 
                    value=transcricao, 
                    height=300, 
                    key="transcricao_text_area"
                )
                
                # Botão de download incorporado
                st.download_button(
                    label="Baixar Transcrição (.txt)",
                    data=transcricao,
                    file_name=f"transcricao_{video_id}.txt",
                    mime="text/plain",
                )