# Descargador de Videos y Audio

Aplicación para descargar videos y audio de YouTube y otras plataformas compatibles con yt-dlp.

## Requisitos Previos
### 1. Python
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 2. FFmpeg (OBLIGATORIO)
Esta aplicación **requiere FFmpeg** para funcionar correctamente.

#### Instalación de FFmpeg en Windows:

**Opción 1: Usando Chocolatey (recomendado)**
```bash
choco install ffmpeg
```

**Opción 2: Descarga manual**
1. Descarga FFmpeg desde: https://ffmpeg.org/download.html
2. Extrae el archivo ZIP
3. Agrega la carpeta `bin` a las variables de entorno PATH del sistema
4. Reinicia la terminal

**Verificar instalación:**
```bash
ffmpeg -version
```

## Instalación

1. Clona o descarga este repositorio
2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv .venv
```

3. Activa el entorno virtual:
```bash
.venv\Scripts\activate
```

4. Instala las dependencias:
```bash
pip install yt-dlp
```

## Uso

1. Ejecuta la aplicación:
```bash
python app.py
```

2. Selecciona el formato de descarga:
   - **1** para video MP4 (1080p con audio)
   - **2** para audio MP3 (320kbps)

3. Ingresa la URL del video que deseas descargar

4. El archivo se descargará automáticamente en tu carpeta de **Descargas**

## Formatos Disponibles

### MP4 (Video)
- Calidad: Hasta 1080p
- Formato de salida: MP4

### MP3 (Audio)
- Calidad: 320kbps
- Formato de salida: MP3

## Notas

- Los archivos descargados se guardan en tu carpeta de Descargas del sistema

## Solución de Problemas

**Error: FFmpeg no está instalado**
- Asegúrate de haber instalado FFmpeg correctamente
- Verifica que FFmpeg esté en el PATH del sistema

**Error al descargar**
- Verifica que la URL sea válida
- Algunos videos pueden estar restringidos geográficamente
- Asegúrate de tener conexión a internet
