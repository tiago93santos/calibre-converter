FROM python:3.10-slim

# Instalar dependências do Calibre
RUN apt-get update && apt-get install -y \
    wget xz-utils libgl1 libegl1 libopengl0 libxcb-cursor0 libxkbcommon0 \
    && rm -rf /var/lib/apt/lists/*

# Instalar Calibre
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.py | python -

WORKDIR /app
COPY app.py /app

RUN pip install flask

CMD ["python", "app.py"]
