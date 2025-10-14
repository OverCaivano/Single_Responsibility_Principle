import json

class GeneradorReporte:
    def generar(self, resultado, formato="texto"):
        if formato == "texto":
            return f"El promedio es: {resultado}"
        elif formato == "json":
            return json.dumps({"promedio": resultado})
        else:
            return "Formato no soportado."
