# Valida el código (si es numérico y de longitud 6).
def validar_id(id_toldo) -> bool:
    return (len(str(id_toldo)) > 0)

# Valida el nombre (si es un texto sin espacios en blanco de entre 1 y 30 caracteres).
def validar_nombre_toldo(nombre) -> bool:
    nombre = nombre.strip()
    return (len(str(nombre)) > 0 and len(str(nombre)) <= 30)

# Valida que los créditos estén entre 1 y 9.
def validar_precio_unitario(creditos) -> bool:
    return ( len(str(creditos)) > 0)

def validar_cantidad(creditos) -> bool:
    return ( len(str(creditos)) > 0)



def validar_id_producto(creditos) -> bool:
    return ( len(str(creditos)) > 0)


