# utils/utils.py
from PIL import Image
import io

def resize_and_compress_image(image, size=(800, 800)):
    try:
        image.seek(0)
        img = Image.open(io.BytesIO(image.read()))
        img.thumbnail(size, Image.LANCZOS)  # Utiliza thumbnail para mantener la proporción
        
        # Crear un buffer en memoria para guardar la imagen redimensionada
        img_io = io.BytesIO()
        img.save(img_io, format=img.format, optimize=True, quality=85)
        img_io.seek(0)
        
        return img_io
    except Exception as e:
        print(f"Error al redimensionar y comprimir la imagen: {e}")
        return None
