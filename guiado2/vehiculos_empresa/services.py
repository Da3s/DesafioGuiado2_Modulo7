from .models import Vehiculo, Chofer, RegistroContabilidad


def crear_vehiculo(pPatente, pMarca, pModelo, pYear):
    vehiculo= Vehiculo(patente= pPatente, marca= pMarca, modelo= pModelo, year= pYear)
    vehiculo.save()
    return vehiculo

def crear_chofer(pRut, pNombre, pApellido, patente):
    obj_vehiculo= Vehiculo.objects.get(pk= patente)
    chofer= Chofer(rut= pRut, nombre= pNombre, apellido= pApellido, vehiculo= obj_vehiculo)
    chofer.save()
    return chofer


def crear_registro_contable(pFecha_compra, pValor, patente):
    obj_vehiculo= Vehiculo.objects.get(pk= patente)
    registro_contable= RegistroContabilidad(fecha_compra= pFecha_compra, valor= pValor, vehiculo= obj_vehiculo)
    registro_contable.save()
    return registro_contable


def deshabilitar_chofer(pRut, pActivo=False):
    chofer= Chofer.objects.get(rut=pRut)
    chofer.activo= pActivo
    chofer.save()
    return chofer


def deshabilitar_vehiculo(pPatente, pActivo=False):
    vehiculo= Vehiculo.objects.get(patente= pPatente)
    vehiculo.activo= pActivo
    vehiculo.save()
    return vehiculo


def habilitar_chofer(pRut, pActivo=True):
    chofer= Chofer.objects.get(rut=pRut)
    chofer.activo= pActivo
    chofer.save()
    return chofer


def habilitar_vehiculo(pPatente, pActivo=True):
    vehiculo= Vehiculo.objects.get(patente= pPatente)
    vehiculo.activo= pActivo
    vehiculo.save()
    return vehiculo


def obtener_vehiculo(pPatente):
    vehiculo= Vehiculo.objects.get(patente= pPatente)
    print(vehiculo)


def obtener_chofer(pRut):
    chofer= Chofer.objects.get(rut=pRut)
    print(chofer)


def asignar_chofer_a_vehiculo(pPatente, pRut):
    vehiculo= Vehiculo.objects.get(patente= pPatente)
    chofer= Chofer.objects.get(rut= pRut)
    vehiculo.chofer= chofer
    vehiculo.save()
    return vehiculo


def imprimir_datos_vehiculos(pPatente):
    vehiculo= Vehiculo.objects.get(patente= pPatente)
    print(vehiculo)


