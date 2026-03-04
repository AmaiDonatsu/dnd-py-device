# Usamos la imagen oficial de Python 3.12 (slim para que sea ligera)
FROM python:3.12-slim

# Instalamos curl y certificados necesarios
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Descargamos e instalamos uv directamente desde el script oficial
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod +x /install.sh && /install.sh && rm /install.sh

# Añadimos el directorio de binarios de uv al PATH
ENV PATH="/root/.local/bin/:$PATH"
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de configuración de uv
COPY pyproject.toml uv.lock* ./

# Instalamos las dependencias del proyecto
# --frozen: asegura que se use exactamente lo que está en el lockfile
RUN uv sync --frozen --no-cache

# Copiamos el código de la aplicación
COPY . .

# Ejecutamos la aplicación con uv run
CMD ["uv", "run", "hello.py"]
