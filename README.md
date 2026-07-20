# Summarizer

Uma aplicação web em **Python** desenvolvida com **Streamlit** que extrai automaticamente legendas e transcrições de vídeos do YouTube a partir da URL, oferecendo visualização instantânea em texto e opção de download.

---

## 🚀 Funcionalidades

* **Extração Inteligente de URLs:** Identifica e extrai o ID de vídeos do YouTube de forma robusta, suportando links padrão e formatos encurtados.
* **Suporte a Múltiplos Idiomas:** Prioriza legendas em português (`pt`) com fallback automático para o inglês (`en`).
* **Interface Web Intuitiva:** Desenvolvida com Streamlit para uma experiência de usuário limpa, rápida e responsiva.
* **Exportação de Dados:** Permite visualizar o texto extraído e baixar o conteúdo diretamente como um arquivo `.txt`.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **Streamlit** (Framework para interface web)
* **youtube-transcript-api** (Extração de legendas)

---

python3 -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\Activate.ps1

pip install -r requirements.txt

streamlit run app.py
