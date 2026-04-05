import json
from datetime import datetime

def genertate_report(results, correlations):
    """
    Construye la estructura del reporte en memoria.

    Parámetros:
    - results: lista de resultados del scanner
    - correlations: correlaciones detectadas

    Retorna:
    - dict listo para exportar a JSON
    """
    
    # Contadores de riesgo 
    summary = {
        "total": len(results),
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }
    
    for r in results:
        summary[r["risk"]] += 1
        
    report = {
        "generated_at": datetime.utcnow().isoformat(),
        "summary": summary,
        "details": results,
        "correlations": correlations
    }
    
    return report


def save_json_report(report_data, output_path):
    """
    Guarda el reporte en un archivo JSON.

    Parámetros:
    - report_data: estructura generada por generate_report
    - output_path: ruta del archivo de salida
    """
    
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4)
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el reporte: {e}")