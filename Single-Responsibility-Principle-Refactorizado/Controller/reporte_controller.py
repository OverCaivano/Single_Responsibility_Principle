
from Service.procesador_service import ProcesadorDatos
from Service.generador_service import GeneradorReporte
from Dao.fuente_datos_dao import FuenteDatos
from Dao.almacenamiento_dao import GuardadorReporte

class ReporteController:
    def __init__(self):
        self.fuente = FuenteDatos()
        self.procesador = ProcesadorDatos()
        self.generador = GeneradorReporte()
        self.guardador = GuardadorReporte()

    def ejecutar_reporte(self):
        datos = self.fuente.obtener_datos()
        datos_procesados = self.procesador.procesar_datos(datos)
        reporte = self.generador.generar(datos_procesados)
        self.guardador.guardar(reporte)
        print("Reporte generado y guardado correctamente.")
