from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View

class ReporteVentas(View):

    def cabecera(self,pdf):
        # Utilizamos el archivo logo_django.png que esta guardado en la carpeta media/imagenes
        archivo_imagen = (settings.MEDIA_ROOT+'/images/vive/a.png')
        # Definimos el tamano de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 70, preserveAspectRatio=True)

        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 18)
        # Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"VIVE TU FUTURO")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE VENTAS")

    def get(self, request, *args, **kwargs):
        # Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        # La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        # Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        # Llamo al metodo cabecera donde estan definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        # Con show page hacemos un corte de pagina para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
