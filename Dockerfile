
# imagem base
FROM python:3.6.7

# cria o diretório /app no container e faz cd para dentro dele
WORKDIR /app

# copia todo o conteúdo do diretório onde está o Dockerfile para dentro do diretório /app no container
ADD . /app

# instala as dependências do projeto
RUN pip install -r requirements.txt

# roda a aplicação app
CMD [ "python", "app.py"]