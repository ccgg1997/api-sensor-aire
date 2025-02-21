# frontend/bot.py
import streamlit as st
import requests

# URL del endpoint del backend
API_URL = "http://ollama:7869/api/chat"

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

            # Enviamos la solicitud POST al backend
            response = requests.post(API_URL, json=data, timeout=100)
            # response.raise_for_status()  # Lanza excepción si el estatus no es 200-299

            # Asumimos que el backend responde con JSON
            mensaje = response.json()

            # Muestra el resultado en Streamlit
            mensaje = "Hola, soy un mensaje del Backend"
            st.success(f"Mensaje del Backend: {mensaje}")

        except requests.exceptions.ConnectionError:
            st.error("No se pudo conectar con el backend. Verifica que el servidor esté funcionando.")
        except requests.exceptions.Timeout:
            st.error("La solicitud excedió el tiempo de espera.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error inesperado al conectarse al Backend: {e}")

if __name__ == "__main__":
    main()
