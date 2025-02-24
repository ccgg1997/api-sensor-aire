# frontend/bot.py
import streamlit as st
import requests

# URL del endpoint del backend
# API_URL = "http://ollama:11434/api/chat"
API_URL = "http://nuevo_contenedor:11434/api/chat"
# API_URL = "http://ollama:11434"

def main():
    st.set_page_config(page_title="Frontend: TU ASISTENTE PERSONAL", layout="centered")
    
    st.title("Frontend: Respondiendo preguntas sobre la calidad del aire")
    pregunta = st.text_area("Escribe tu pregunta aquí:", height=100)
    st.write("Presiona el botón para obtener una respuesta.")
    
    pregunta = f"Eres un experto en sensores de calidad del aire, tu nombre DeepFahrenheit y eres un asistente sobre el monitoreo en tiempo real de la calidad del aire (proximamente disponible). por ahora solo puedes responder preguntas generales sobre calidad del aire y sensores. Si te preguntan algo diferente, responde no respondas y solo escribe MI ESPECIALIDAD SON LOS SENSORES. Si te saludan, saluda y di quien eres. Esta es la pregunta: {pregunta}"
    
    if st.button("Obtener Mensaje"):
        try:
            data = {
                "model": "llama3",
                "messages": [
                    {
                        "role": "user",
                        "content": pregunta
                    }
                ],
                "stream": False
            }

    
            # response = requests.get(API_URL)
            
            response = requests.post(API_URL, json = data, timeout=10000)
            mensaje = response.text

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
