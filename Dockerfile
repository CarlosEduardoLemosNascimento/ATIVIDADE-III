# Usar uma imagem oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos e instalá-los
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação
COPY app/ .

# Definir o comando de inicialização
CMD ["python", "main.py"]
