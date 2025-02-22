# frontend/bot.py
import streamlit as st
import requests

# URL del endpoint del backend
API_URL = "http://ollama:11434/api/chat"
# API_URL = "http://ollama:11434"

def main():
    # Configura la página (opcional)
    st.set_page_config(page_title="Frontend: Consumiendo API Flask", layout="centered")
    
    st.title("Frontend: Consumiendo API Flask")
    st.write("Presiona el botón para obtener el mensaje del backend:")
    
    if st.button("Obtener Mensaje"):
        try:
            data = {
                "model": "llama3",
                "messages": [
                    {
                        "role": "user",
                        "content": "¿Cómo estás?"
                    }
                ],
                "stream": False
            }

    
            # response = requests.get(API_URL)
            
            response = requests.post(API_URL, json = data, timeout=10000)
            mensaje = response.text

            # mensaje = "Hola, soy un mensaje del Backend"
            st.success(f"Mensaje del Backend: {mensaje}")

        except Exception as e:
            st.error("No se pudo conectar con el backend. Verifica que el servidor esté funcionando." +str(e))
        except requests.exceptions.Timeout:
            st.error("La solicitud excedió el tiempo de espera.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error inesperado al conectarse al Backend: {e}")

# def main():
#     API_URL = "http://localhost:7869"
#     response = requests.get(API_URL)
#     print(response.text)

if __name__ == "__main__":
    main()
