import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def extrair_video_id(url: str) -> str:
    """Extrai o ID de 11 caracteres de URLs padrão ou encurtadas do YouTube."""
    padrao = r"(?:v=|\/|be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(padrao, url)
    return match.group(1) if match else None

def extrair_transcricao(video_id: str) -> str:
    #Busca e consolida a transcrição do vídeo apartir da URL
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id, languages=['pt', 'en'])
        texto_completo = " ".join([item.text for item in transcript_list])
        return texto_completo
    
    except TranscriptsDisabled:
        return "Erro: As legendas estão desativadas para este vídeo."
   
    except NoTranscriptFound:
        return "Erro: Nenhuma legenda foi encontrada para este vídeo nos idiomas suportados (PT/EN)."
   
    except Exception as e:
        return f"Erro ao recuperar a transcrição: {str(e)}"