from django.http import JsonResponse

from GestionDeCitas.models import Medico, Paciente
from Software2.Methods import GenerarHorarioCitas

def get_medicos(request):
    especialidad = request.GET["especialidad"] 
    medicos =  Medico.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if especialidad:
        medicos= Medico.objects.filter(Especialidad=especialidad)    
    for medico in medicos:
        nombre= "%s %s %s %s" %(e.PrimerNombre, e.SegundoNombre, e.PrimerApellido, e.SegundoApellido)
        options+='<option value="%s">%s</option>' % (
            nombre, nombre)
    response = {}
    response['medico'] =options
    return JsonResponse(response)
       
def get_horarios(request):
    medico = request.GET["medico"] 
    medicos =  Medico.objects.none()
    options = '<option value="" selected="selected">---------</option>'


    if nombre:

        medicoElegido =[]
        temporal=[]
        for e in medico:
            if(e==' '):
                medicoElegido.append(temporal)
                temporal=[]
            else:
                temporal.append(e)
    #EliminarSimbolos(str(medicoElegido))

    medicoBD = Medico.objects.filter (
        PrimerNombre=medicoElegido[0],
        SegundoNombre=medicoElegido[1],
        PrimerApellido=medicoElegido[2],
        SegundoApellido=medicoElegido[3]
        )
    
    horarioLlegada = medicoBD[0].HorarioLlegada
    horarioSalida = medicoBD[0].HorarioSalida

    horarios = GenerarHorarioCitas(horarioLlegada, horarioSalida)

    for horario in horarios:
        options+='<option value="%s">%s</option>' % (
            horario,horario)
    
    response = {}
    response['horarios'] =options
    return JsonResponse(response)
      