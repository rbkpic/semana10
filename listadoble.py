"""
cabeza = None
cola = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["anterior"] = cola
        cola["siguiente"] = nuevo
        cola = nuevo

agregar_final("Inicio")
agregar_final("Catálogo")
agregar_final("Contacto")

def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["siguiente"] else "\n")
        actual = actual["siguiente"]

def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" ↔ " if actual["anterior"] else "\n")
        actual = actual["anterior"]

mostrar_adelante()
mostrar_atras()

def agregar_inicio(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)
    if cabeza is None:
        cabeza = cola = nuevo
    else:
        nuevo["siguiente"] = cabeza
        cabeza["anterior"] = nuevo
        cabeza = nuevo

agregar_inicio("Bienvenida")
mostrar_adelante()
mostrar_atras()

def eliminar(dato):
    global cabeza, cola
    actual = cabeza
    while actual is not None and actual["dato"] != dato:
        actual = actual["siguiente"]
    if actual is None:
        return False

    anterior = actual["anterior"]
    siguiente = actual["siguiente"]
    if anterior is None:
        cabeza = siguiente
    else:
        anterior["siguiente"] = siguiente
    if siguiente is None:
        cola = anterior
    else:
        siguiente["anterior"] = anterior
    return True

print("Eliminado:", eliminar("Catálogo"))
mostrar_adelante()
mostrar_atras()
"""

def buscar(dato, cabeza, cola):
    if cabeza is None or cola is None:
        return False
    
    nodoactual_cabeza = cabeza
    nodoactual_cola = cola
    
    while nodoactual_cabeza is not None and nodoactual_cola is not None:
        if nodoactual_cabeza['dato'] == dato or nodoactual_cola['dato'] == dato:
            return True
            
        if nodoactual_cabeza is nodoactual_cola or nodoactual_cabeza['siguiente'] is nodoactual_cola:
             if nodoactual_cabeza['dato'] == dato or nodoactual_cola['dato'] == dato:
                 return True
             break
        
        nodoactual_cabeza = nodoactual_cabeza['siguiente']
        nodoactual_cola = nodoactual_cola['anterior']

    return False

def insertar_despues(referencia, dato):
    if referencia is None:
        return False, cola
    
    nodo_actual = referencia
    
    while nodo_actual is not None:
        if nodo_actual['dato'] == referencia:
            nuevo_nodo = {'dato': dato, 'siguiente': None, 'anterior': None}
            
            nodo_siguiente = nodo_actual['siguiente']
            
            nuevo_nodo['anterior'] = nodo_actual
            nuevo_nodo['siguiente'] = nodo_siguiente
            nodo_actual['siguiente'] = nuevo_nodo
            
            if nodo_siguiente is not None:
                nodo_siguiente['anterior'] = nuevo_nodo
            else:
                cola = nuevo_nodo
                
            return True, cola 
            
        nodo_actual = nodo_actual['siguiente']
        
    return False, cola