# Reglas de detección de riesgos
def detect_gps(metadata):
    if metadata.get("GPSLatitude") and metadata.get("GPSLongitude"):
        return {
            "type": "CRITICAL",
            "type": "GPS_DATA",
            "message": "La imagen contiene coordenadas GPS (posible fuga de ubicacion)"
        }
    return None

# Reglas adicionales
def detect_software(metadata):
    software = metadata.get("Software", "")
    suspicious = ["Photoshop", "GIMP", "Lightroom"] 
    
    for s in suspicious:
        if s.lower() in software.lower():
            return {
                "type": "MEDIUM",
                "type": "EDITING_SOFTWARE",
                "message": f"Imagen editada con {s}"
            }
    return None

# Regla para detectar fecha de creación (puede ser un riesgo si se filtra)
def detect_timestamp(metadata):
    if metadata.get("CreateDate"):
        return {
            "type": "LOW",
            "rule": "TIMESTAMP",
            "message": "La imagen contiene fecha de creación"
        }
    return None   

def detect_time_inconsistency(metadata):
    """
    Detecta si la fecha de creación y modificación no coinciden.
    Esto puede indicar que la imagen fue editada.
    """
    
    create_date = metadata.get("CreateDate")
    modify_date = metadata.get("ModifyDate")
    
    if create_date and modify_date and create_date != modify_date:
        return {
            "type": "MEDIUM",
            "rule": "TIME_INCONSISTENCY",
            "message": "Inconsistencia en fechas: CreateDate y ModifyDate no coinciden (posible edición)"
        }
        
    return None

def detect_device_info(metadata):
    """
    Detecta si la fecha de creación y modificación no coinciden.
    Esto puede indicar que la imagen fue editada.
    """
    
    make = metadata.get("Make")
    model = metadata.get("Model")
    
    if make and model:
        return {
            "type": "LOW",
            "rule": "DEVICE_INFO",
            "message": f"Información del dispositivo: {make} {model}"
        }
        
    return None

def detect_missing_metadata(metadata):
    """
    Detecta si falta metadata clave.
    Puede indicar que fue eliminada intencionalmente.
    """
    
    if not metadata.get("CreateDate") and not metadata.get("GPSLatitude"):
        return {
            "type": "MEDIUM",
            "rule": "MISSING_METADATA",
            "message": "Falta metadata clave (CreateDate, GPSLatitude), (posible sanitización o manipulación)"
        }
    
    return None

RULES = [
    detect_gps,
    detect_software,
    detect_timestamp,
    detect_time_inconsistency,
    detect_device_info,
    detect_missing_metadata
]