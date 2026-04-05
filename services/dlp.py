def evaluate_dlp(risk, findings):
    """
    Evalúa si una imagen debe ser permitida, advertida o bloqueada.

    Parámetros:
    - risk: nivel de riesgo (LOW, MEDIUM, HIGH)
    - findings: lista de hallazgos

    Retorna:
    - dict con decisión DLP
    """
    
    decision = {
        "action": "ALLOW", 
        "reasons": [],
        "requires_sanitization": False
    }
    
    # 🔴 Riesgo alto → bloquear
    if risk == "HIGH":
        decision["action"] = "BLOCK"
        decision["requires_sanitization"] = True
    
    # 🟡 Riesgo medio → advertir
    elif risk == "MEDIUM":
        decision["action"] = "WARN"
        
    # 🟢 Riesgo bajo → permitir
    else:
        decision["action"] = "ALLOW"
        
    # Agregar razones basadas en hallazgos específicos
    for f in findings:
        if f["rule"] == "GPS_DATA":
            decision["reasons"].append("Contiene datos de ubicación (GPS)")
        
        if f["rule"] == "DEVICE_INFO":
            decision["reasons"].append("Contiene información del dispositivo")
            
        if f["rule"] == "TIME_INCONSISTENCY":
            decision["reasons"].append("Posible edición detectada")
            
    return decision