import datetime
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from productos.models import InstitucionFinanciera, Departamento, Servicio
from ventas.models import PlanesConcretados
from .forms import ReporteForm
from django.template.loader import get_template
from django.db.models import Q
from .make_report_pdf import render_to_pdf


class ReporteView(LoginRequiredMixin, View):

    def desdeInstitucion(self,queryset, datos):
        departamentos = {}
        for institucion in queryset:
            if not datos.get(institucion.idServicio.idDepartamento.idInstitucion.nombre) :
                #print("institucion:{}".format(institucion.idServicio.idDepartamento.idInstitucion.nombre))
                #Ahora se obtienen todos los departamentos pertenecientes a la institucion indicada
                departamentos = self.desdeDepartamento(queryset.filter(idServicio__idDepartamento__idInstitucion__nombre = institucion.idServicio.idDepartamento.idInstitucion.nombre ))
                #Se agrega el diccionario de departamentos con planes al diccionario de las instituciones
                #print("DEPTOS: {}".format(departamentos))
                datos[institucion.idServicio.idDepartamento.idInstitucion.nombre] = departamentos


    def desdeDepartamento(self, queryset):
        planes = {}
        departamentos = {}

        for elem in queryset:
            if not elem.idServicio.idDepartamento.nombre in departamentos:
                #print("depto: {}".format(elem.idServicio.idDepartamento.nombre))
                #Se llama al metodo que devuelve el conjunto de planes para cada departamento
                planes = self.desdePlan(queryset.filter(idServicio__idDepartamento__nombre = elem.idServicio.idDepartamento.nombre))
                #Se contruye el diccionario con el nombre del departamento y sus PLANES
                #print("PLANES: {}".format(planes))
                departamentos[elem.idServicio.idDepartamento.nombre] = planes
                planes = {}

        return departamentos

    def desdePlan(self, queryset):
        planes = {}
        plan = []
        datos = []
        for p in queryset:
            datos.append(p.numeroPoliza)
            datos.append(p.formaPago)
            datos.append(p.plazoAnos)
            datos.append(p.valorPlan)
            plan.append(datos)
            datos = []

        planes[p.idServicio.nombrePlan] = plan

        return planes



    def post(self, request, *args, **kwargs):
        #form = ReporteForm(request.POST)
        #print("FORM: {}".format(form))
        #se valida que el id de la Institucionfinanciera se encuentre en sessions
        #template = get_template('reportes/reporte.html')
        template = 'reportes/reporte.html'
        pInicial = self.request.POST.get('periodoInicial')
        pFinal = self.request.POST.get('periodoFinal')
        print("Periodos: {} - {}".format(pInicial, pFinal))
        datos = {}

        if self.request.session.has_key('institucion'):
            inst = self.request.session['institucion']
            if(inst == "0"):
                #se Obtiene el query set que trae todos los planes de todas las instituciones financieras pertenecientes al asesor indicado, en la fecha solicitada
                queryset = PlanesConcretados.objects.filter(Q(idAsesor=request.user.id), Q(fechaContratacion__range=[pInicial,pFinal]))
                self.desdeInstitucion(queryset, datos)
                # se define el nivel de que el usuario selecciono para ver como se organizan las graficas
                nivel = "Institucion Todos"
            else:
                if(self.request.session.has_key('departamento')):
                    deptos = self.request.session['departamento']
                    if(deptos == "0"):
                        queryset = PlanesConcretados.objects.filter(Q(idAsesor=request.user.id), Q(fechaContratacion__range=[pInicial,pFinal])).filter(idServicio__idDepartamento__idInstitucion = inst)
                        #print("NOMBRE INST: {}".format(queryset[0].idServicio.idDepartamento.idInstitucion.nombre))
                        #datos[queryset[0].idServicio.idDepartamento.idInstitucion.nombre] = self.desdeDepartamento(queryset)
                        self.desdeInstitucion(queryset,datos)
                        #print("Datos: {}".format(datos))
                        # se define el nivel de que el usuario selecciono para ver como se organizan las graficas
                        nivel = "Departamentos Todos"

                    else:
                        plan = self.request.POST.get('plan')
                        #print("deptos: {}".format(deptos))
                        if(plan == "0"):
                            #pk_depto = departamentos.objects.get("")
                            queryset = PlanesConcretados.objects.filter(Q(idAsesor=request.user.id), Q(fechaContratacion__range=[pInicial,pFinal])).filter(idServicio__idDepartamento__idDepartamento = deptos).filter(idServicio__idDepartamento__idInstitucion = inst)
                            #queryset1 = PlanesConcretados.objects.filter(idAsesor=request.user.id, idServicio__idDepartamento__idInstitucion = inst, idServicio__idDepartamento__idDepartamento = deptos).values()
                            #print("QUERySET!: {}".format(qset))
                            #for x in qset:
                            #    print("NOMBRE INST: {}".format(x.idServicio.idDepartamento.idInstitucion.nombre))
                            #    print("NOMBRE DEPTO: {}".format(x.idServicio.idDepartamento.nombre))
                                #datos[x.idServicio.idDepartamento.idInstitucion.nombre] = {x.idServicio.idDepartamento.nombre : self.desdePlan(qset)}
                            self.desdeInstitucion(queryset,datos)
                            print("Datos X: {}".format(datos))
                            # se define el nivel de que el usuario selecciono para ver como se organizan las graficas
                            nivel = "Planes Todos"
                        else:
                            queryset = PlanesConcretados.objects.filter(Q(idAsesor=request.user.id), Q(fechaContratacion__range=[pInicial,pFinal])).filter(idServicio__idDepartamento__idInstitucion = inst).filter(idServicio__idDepartamento__idDepartamento = deptos).filter(idServicio = plan)
                            #for p in queryset:
                                #datos[p.idServicio.idDepartamento.idInstitucion.nombre] = {p.idServicio.idDepartamento.nombre : self.desdePlan(queryset)}
                            self.desdeInstitucion(queryset, datos)
                            print("Datos Y: {}".format(datos))
                            # se define el nivel de que el usuario selecciono para ver como se organizan las graficas
                            nivel = "Plan Especifico"
                #datos = {}

        else:
            print("No se encontro el valor de la institucion")

        print("\n\n______________________")
        print("DATOS: {}\n\n".format(datos))
        for inst in datos.keys():
            print(inst)
            deptos = datos[inst]
            print("deptos: {}".format(deptos))
            for d in deptos.keys():
                print("\t " + d)
                planes = deptos[d]
                for p in planes.keys():
                    print("\t\t " + p)
                    datos = planes[p]
                    for d in datos:
                        for dat in d:
                            print("\t\t\tdat: {}".format(dat))
                        print("\n")
        print("\n\n______________________")

        context = {
            "datos":datos,
            "nivel": nivel,
            "asesor": request.user,
        }
        return render(request,template, context)

        '''#la redenderizacion se hace en un html
        html = template.render(context)
        #La renderizacion de hace a un render_to_pdf
        pdf = render_to_pdf('reportes/reporte.html', context)
        print("PDF: {}".format(pdf))
        if pdf:
            response = HttpResponse(pdf, content_type = 'application/pdf')
            #print("USER: {}".format(request.user))
            filename = "Reporte_%s.pdf" %(request.user)
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("nor found")'''


class GeneracionServicios(View):

    def post(self, request, *args, **kwargs):
        plan = {}
        print(request.POST.get("departamento"))
        depto = request.POST.get("departamento")
        #print("DEPTO: {}".format(depto))

        #se sube a la sesion el id del departamento
        request.session['departamento'] = depto

        if(request.is_ajax()):
            if(depto == "0"):
                print("Todos")
                x = ["Todos"]
                plan["planes"] = x
                return JsonResponse(plan, safe=False)
            else:
                print("Departamento especifico")
                plan["planes"] = list(Servicio.objects.filter(idDepartamento__pk=depto).values_list('nombrePlan', 'idServicio'))
                plan["planes"].insert(0,("----------","-1"))
                plan["planes"].insert(1,("Todos","0"))
                #print("PLANES: {}".format(plan))
                return JsonResponse(plan, safe=False)

    def get(self, request, *args, **kwargs):
        template = "reportes/ventas.html"
        departamento = ReporteForm()
        print("Departamento***: {}".format(departamento))
        context = {
            "form":departamento
        }
        return render(request, template, context)

class GeneracionDepartamentos(View):

    def post(self, request, *args, **kwargs):
        print(request.POST.get("institucion"))
        inst = request.POST.get("institucion")
        #print("Intitucion: {}".format(inst))
        depto = {}

        if(inst != ''):
            #se sube a la sesion el id de la Institucionfinanciera
            request.session['institucion'] = inst

            #Varifica si la peticion que llego fue hecha a traves de un ajax
            if(request.is_ajax()):
                if(inst == "0"):
                    print("Todas")
                    x = ["Todos"]
                    depto["deptos"] = x
                    return JsonResponse(depto, safe=False)
                else:
                    #print("Institucion Especifica")
                    depto["deptos"] = list(Departamento.objects.filter(idInstitucion__pk=inst).values_list('nombre', 'idDepartamento'))
                    depto["deptos"].insert(0,("----------", "-1"))
                    depto["deptos"].insert(1,("Todos","0"))
                    return JsonResponse(depto, safe=False)
        else:
            return JsonResponse(depto, safe=False)

    def get(self, request, *args, **kwargs):
        template = "reportes/ventas.html"
        institucion = ReporteForm()
        print("Type: {}".format(type(institucion)))
        #print("Institucion: {}".format(institucion))
        context = {
            "form":institucion
        }
        return render(request, template, context)
