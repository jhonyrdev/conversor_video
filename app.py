import yt_dlp
import shutil
import os

def download_media(url, format_type):

    if not shutil.which('ffmpeg'):
        print(" ADVERTENCIA: FFmpeg no está instalado.")
    
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    output_template = os.path.join(downloads_folder, '%(title)s.%(ext)s')
    
    if format_type == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_template,
            'noplaylist': True,
            'progress_hooks': [progress_hook],
            'quiet': False,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',  
            }],
        }
    else: 
        ydl_opts = {
            'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
            'merge_output_format': 'mp4',
            'outtmpl': output_template,
            'noplaylist': True,
            'progress_hooks': [progress_hook],
            'quiet': False,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("\n Descarga completada correctamente.")
    except yt_dlp.utils.DownloadError as e:
        print(f"\n Error al descargar el video: {e}")
    except Exception as e:
        print(f"\n Error inesperado: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            percent = downloaded / total * 100
            print(f"\rDescargando: {percent:.2f}% [{downloaded / 1_000_000:.2f} MB de {total / 1_000_000:.2f} MB]", end='')
    elif d['status'] == 'finished':
        print("\n Procesando archivo...")

if __name__ == "__main__":
    print("=" * 50)
    print("  DESCARGADOR DE VIDEOS Y AUDIO")
    print("=" * 50)
    print("\nSeleccione el formato de descarga:")
    print("  1. MP4 (Video con audio)")
    print("  2. MP3 (Solo audio)")
    print()
    
    opcion = input("Ingrese su opción (1 o 2): ").strip()
    
    if opcion == '1':
        format_type = 'mp4'
        print("\n Seleccionado: Video MP4 con audio")
    elif opcion == '2':
        format_type = 'mp3'
        print("\n Seleccionado: Audio MP3")
    else:
        print("\n Opción inválida. Usando MP4 por defecto.")
        format_type = 'mp4'
    
    print()
    url = input("Ingrese la URL del video: ").strip()
    
    download_media(url, format_type)
