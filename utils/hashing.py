import hashlib

def calculate_sha256(file_path):
    """
    Calcula el hash SHA-256 de un archivo.
    Sirve para verificar integridad y detectar duplicados.
    """
    
    sha256 = hashlib.sha256()
    
    with open(file_path, "rb") as f:
        
        # Lee el archivo en bloques para no cargar todo en memoria
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
            
    return sha256.hexdigest()