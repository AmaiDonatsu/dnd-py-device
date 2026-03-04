#!/bin/bash

# Configuración
IMAGE_NAME="test-rpi"
CONTAINER_NAME="mi-test-rpi"

# Función para mostrar ayuda
show_help() {
    echo "Uso: ./run.sh [opciones]"
    echo "Opciones:"
    echo "  build    Fuerza la reconstrucción de la imagen Docker"
    echo "  run      Ejecuta el contenedor (usa la imagen actual)"
    echo "  dev      Ejecuta montando el código local (ideal para desarrollo)"
    echo "  all      Construye y ejecuta (por defecto)"
}

# Lógica principal
case "$1" in
    build)
        echo "--- Construyendo imagen $IMAGE_NAME ---"
        docker build -t $IMAGE_NAME .
        ;;
    run)
        echo "--- Ejecutando $IMAGE_NAME ---"
        docker run --rm --name $CONTAINER_NAME --memory="512m" --cpus="1.0" $IMAGE_NAME
        ;;
    dev)
        echo "--- Modo Desarrollo: Montando volumen local ---"
        docker run --rm -v "$(pwd):/app" --name $CONTAINER_NAME --memory="512m" --cpus="1.0" $IMAGE_NAME
        ;;
    help)
        show_help
        ;;
    *)
        echo "--- Construyendo y Ejecutando ---"
        docker build -t $IMAGE_NAME . && 
        docker run --rm --name $CONTAINER_NAME --memory="512m" --cpus="1.0" $IMAGE_NAME
        ;;
esac
