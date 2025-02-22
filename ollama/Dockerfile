FROM ollama/ollama:latest

WORKDIR /ollama

RUN nohup ollama serve & \
    sleep 5 && \
    ollama pull llama3
