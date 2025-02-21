FROM ollama/ollama:latest

WORKDIR /ollama

# COPY ./ /app/
# RUN ollama run llama3
# COPY . .

RUN nohup ollama serve & \
    sleep 5 && \
    ollama pull llama3

# Definimos el comando final para cuando el contenedor se ejecute
# CMD ["ollama", "serve"]