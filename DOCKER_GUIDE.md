# 🐳 Guía de Docker para Proyectos Python con `uv`

Esta guía contiene los comandos y flujos de trabajo recomendados para desarrollar de forma iterativa en este proyecto.

## 🚀 Comandos Rápidos

Si usas el script `run.sh`, estos son los comandos principales:

- **Construir y Ejecutar (Todo en uno):**
  ```bash
  ./run.sh
  ```
- **Modo Desarrollo (Monta tu código local):**
  ```bash
  ./run.sh dev
  ```
  *Usa este modo cuando solo estés editando archivos `.py` para ver los cambios al instante sin reconstruir la imagen.*

- **Solo Construir:**
  ```bash
  ./run.sh build
  ```

---

## 🛠 Conceptos Clave de Docker

### 1. El ciclo `build` vs `run`
- **Build:** Crea la "foto" (imagen) de tu aplicación con todas sus librerías instaladas. Debes ejecutarlo cada vez que añadas una dependencia con `uv add`.
- **Run:** Crea una instancia (contenedor) a partir de esa foto.

### 2. Uso de Volúmenes (`-v`)
Al usar `-v "$(pwd):/app"`, Docker "sustituye" la carpeta `/app` del contenedor por tu carpeta local. Esto permite:
- Editar código y ejecutarlo al instante.
- Que los archivos creados por el programa (logs, bases de datos) aparezcan en tu PC.

### 3. El Flag `--rm`
Evita el error: *"The container name is already in use"*. Al finalizar el programa, Docker borra el contenedor automáticamente, manteniendo tu sistema limpio.

### 4. Límites de Recursos
Hemos limitado el contenedor a:
- **CPU:** 1.0 (equivalente a 1 núcleo de tu procesador).
- **Memoria:** 512m (evita que un error de código consuma toda la RAM de tu sistema).

---

## 🧹 Limpieza Manual

Si alguna vez necesitas limpiar Docker a fondo:

- **Ver contenedores activos:** `docker ps`
- **Detener un contenedor:** `docker stop mi-test-rpi`
- **Eliminar contenedores detenidos:** `docker container prune`
- **Ver imágenes guardadas:** `docker images`
- **Eliminar imagen de este proyecto:** `docker rmi test-rpi`

---

## 💡 Troubleshooting (Solución de Problemas)

### Permisos de Docker
Si recibes `permission denied`, asegúrate de haber ejecutado:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### uv: not found
Esto ocurre si intentas usar `uv` en el `Dockerfile` sin haberlo instalado primero. Nuestro `Dockerfile` actual ya lo soluciona instalándolo automáticamente.
