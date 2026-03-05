# 🐳 Guía de Docker para Proyectos Python con `uv` (Windows)

Esta guía contiene los comandos y flujos de trabajo recomendados para desarrollar de forma iterativa en este proyecto usando Windows.

## 🚀 Comandos Rápidos

Si usas el script `run.bat`, estos son los comandos principales desde PowerShell o Símbolo del sistema (CMD):

- **Construir y Ejecutar (Todo en uno):**
  ```cmd
  .\run.bat
  ```
- **Modo Desarrollo (Monta tu código local):**

  ```cmd
  .\run.bat dev
  ```

  _Usa este modo cuando solo estés editando archivos `.py` para ver los cambios al instante sin reconstruir la imagen._

- **Solo Construir:**
  ```cmd
  .\run.bat build
  ```

---

## 🛠 Conceptos Clave de Docker

### 1. El ciclo `build` vs `run`

- **Build:** Crea la "foto" (imagen) de tu aplicación con todas sus librerías instaladas. Debes ejecutarlo cada vez que añadas una dependencia con `uv add`.
- **Run:** Crea una instancia (contenedor) a partir de esa foto.

### 2. Uso de Volúmenes (`-v`)

Al usar `-v "%cd%:/app"`, Docker "sustituye" la carpeta `/app` del contenedor por tu carpeta local en Windows. Esto permite:

- Editar código y ejecutarlo al instante.
- Que los archivos creados por el programa (logs, bases de datos) aparezcan en tu PC.

### 3. El Flag `--rm`

Evita el error: _"The container name is already in use"_. Al finalizar el programa, Docker borra el contenedor automáticamente, manteniendo tu sistema limpio.

### 4. Límites de Recursos

Hemos limitado el contenedor a:

- **CPU:** 1.0 (equivalente a 1 núcleo de tu procesador).
- **Memoria:** 512m (evita que un error de código consuma toda la RAM de tu sistema).
  _Nota: En Windows, Docker Desktop maneja sus propios límites globales para todos los contenedores en su configuración (Settings > Resources)._

---

## 📊 Monitoreo de Recursos

Para ver cuánta CPU y Memoria (RAM) está consumiendo el contenedor en tiempo real, usa este comando en tu terminal:

```cmd
docker stats mi-test-rpi
```

_(Presiona `Ctrl+C` para salir)._

> **Tip:** También puedes abrir la interfaz gráfica de **Docker Desktop**, ir a la pestaña "Containers", hacer clic sobre el contenedor `mi-test-rpi` y revisar la pestaña "Stats".

---

## 🧹 Limpieza Manual

Si alguna vez necesitas limpiar Docker a fondo, puedes ejecutar estos comandos en PowerShell/CMD o usar la interfaz gráfica de **Docker Desktop**:

- **Ver contenedores activos:** `docker ps`
- **Detener un contenedor:** `docker stop mi-test-rpi`
- **Eliminar contenedores detenidos:** `docker container prune`
- **Ver imágenes guardadas:** `docker images`
- **Eliminar imagen de este proyecto:** `docker rmi test-rpi`

---

## 💡 Troubleshooting (Solución de Problemas)

### Permisos y Docker Desktop

A diferencia de Linux, en Windows normalmente no verás problemas de `permission denied` si estás usando **Docker Desktop**.

- Asegúrate de que Docker Desktop esté **abierto y en ejecución** (busca el ícono de la ballena en la barra de tareas).
- Si usas WSL2 (Windows Subsystem for Linux) como backend de Docker Desktop, asegúrate de tenerlo habilitado en las configuraciones de Docker.

### Rutas en volúmenes (`dev` mode)

Si tienes problemas con el modo `dev` (`.\run.bat dev`), asegúrate de ejecutar el comando desde la raíz del proyecto para que la variable `%cd%` (current directory) apunte correctamente a la ubicación de tus archivos. En PowerShell, también puedes escribir `cmd /c run.bat dev` en caso de problemas con variables de entorno.

### uv: not found

Esto ocurre si intentas usar `uv` en el `Dockerfile` sin haberlo instalado primero. Nuestro `Dockerfile` actual ya lo soluciona instalándolo automáticamente.
