from PIL import Image
import io

def resize_and_compress_image(image, output_path, size=(800, 800)):
    try:
        image.seek(0)
        img = Image.open(io.BytesIO(image.read()))
        img .thumbnail(size, Image.LANCZOS)
        img.save(output_path, optimize=True, quality=85)
    except Exception as e:
        print(f"Error al redimensionar y comprimir la imagen: {e}")
