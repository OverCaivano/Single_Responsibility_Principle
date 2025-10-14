class GuardadorReporte:
    def guardar(self, contenido, archivo="reporte.txt"):
        with open(archivo, "w") as f:
            f.write(contenido)
