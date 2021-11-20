from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL

from config import config
from validaciones import *

app = Flask(__name__)
# CORS(ap
CORS(app)

conexion = MySQL(app)





@cross_origin

## Metodos get para tabla toldos

@app.route('/toldos', methods=['GET'])
def listar_costos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT toldos.id_toldo, toldos.nombre_toldo, toldos.id_producto, productos_proveedores.descripcion_producto, productos_proveedores.precio_unitario, toldos.cantidad, toldos.id_inc FROM toldos INNER JOIN productos_proveedores ON toldos.id_producto = productos_proveedores.id_producto;"
        cursor.execute(sql)
        datos = cursor.fetchall()
        costos = []
        for fila in datos:
            if len(fila)>1:

                fila = {'id_toldo': fila[0], 'nombre_toldo': fila[1], 'id_producto': fila[2], 'descripcion_producto': fila[3], 'precio_unitario': str(fila[4]),  'cantidad': str(fila[5]), 'id_inc': fila[6]}
                costos.append(fila)
        
        return jsonify({"toldos": costos})
    
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})



@app.route('/toldos/<descripcion>', methods=['GET'])
def leer_curso(id_toldo):
    try:
        toldo = buscar_toldo(id_toldo)
        if toldo != None:
            return jsonify({'toldo': toldo, 'mensaje': "toldo encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "toldo no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

## Metodos get para tabla productos_proveedores




## Metodos post para tabla toldos

@app.route('/insertartoldo', methods=['POST'])
def registrar_toldo():
     
    print(request.json)
    if (validar_id(request.json['id_toldo']) and validar_nombre_toldo(request.json['nombre_toldo']) and validar_cantidad(request.json['cantidad']) and validar_id_producto(request.json['id_producto'])):
        try:
            toldos = buscar_toldo(request.json['id_toldo'], request.json['id_producto'])
            produ = buscar_toldo_nombre(request.json['id_toldo'], request.json['nombre_toldo'])
            print(toldos)
            print(produ)

            if toldos == "ya existe" or produ == "el nombre no corresponde":
                return jsonify({'mensaje': "Código ya existe, no se puede duplicar.", 'exito': False})
            else:
                cursor = conexion.connection.cursor()
                sql = """INSERT INTO toldos (id_toldo, nombre_toldo, id_producto, cantidad) 
                VALUES ('{0}', '{1}', '{2}',  '{3}')""".format(request.json['id_toldo'], request.json['nombre_toldo'], request.json['id_producto'], request.json['cantidad'])
                print(sql)
                cursor.execute(sql)
                conexion.connection.commit()  # Confirma la acción de inserción.
                return jsonify({'mensaje': "Costo registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})



def buscar_toldo(id_toldo, id_producto):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM toldos WHERE id_toldo = '{0}' and id_producto = '{1}'".format(id_toldo, id_producto)
        print(sql)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos == None:
            return jsonify({"exito": True})
        else:
            return "ya existe"
    except Exception as ex:
        raise ex


def buscar_toldo_nombre(id_toldo, nombre_toldo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT nombre_toldo FROM toldos WHERE id_toldo = '{0}'".format(id_toldo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        print(nombre_toldo)
        if datos != None:
            print(datos)
            if datos[0] == nombre_toldo:
                return jsonify({"exito": True})
            else:
                 return "el nombre no corresponde"
        else:
            return jsonify({"exito":True})
    except Exception as ex:
        raise ex


@app.route('/login', methods=['POST'])
def login():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM usuarios WHERE contrasena = '{1}' and usuario = '{0}'".format(request.json["usuario"], request.json["contrasena"])
        print(sql)
        cursor.execute(sql)
        datos = cursor.fetchone()
        print(datos)
        if datos != None:
            return jsonify({"datos": "321rte980"})
        else:
           return jsonify({"datos": "datos invalidos"})
    except Exception as ex:
        raise ex


## Metodos delete para tabla toldos
@app.route('/eliminartoldo/<id_inc>', methods=['DELETE'])
def eliminar_toldo(id_inc):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM toldos WHERE id_inc = '{0}'".format(id_inc)
        print(sql)
        cursor.execute(sql)
        cursor.connection.commit()
        return jsonify({"toldo eliminado": id_inc})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})




## Metodos get precio para tabla toldos

@app.route('/precio/<nombre_toldo>', methods=['GET'])
def get_toldo(nombre_toldo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT toldos.id_toldo, toldos.nombre_toldo, toldos.id_producto, productos_proveedores.descripcion_producto, productos_proveedores.precio_unitario, toldos.cantidad, toldos.id_inc FROM toldos INNER JOIN productos_proveedores ON toldos.id_producto = productos_proveedores.id_producto WHERE toldos.nombre_toldo LIKE '%{0}%';".format(nombre_toldo)
        print(sql)
        cursor.execute(sql)
        datos = cursor.fetchall()
        print(datos)
        componentes = []
        for fila in datos:
            fila = {'id_toldo': fila[0], 'nombre_toldo': fila[1], 'id_producto': fila[2], 'descripcion_producto': fila[3], 'precio_unitario': str(fila[4]),  'cantidad': str(fila[5]), 'id_inc': fila[6]}

            componentes.append(fila)
        print(componentes)
        precio = buscar_precio(componentes)
        return jsonify({"Toldo": componentes, "Precio": precio})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})


def buscar_precio(componentes):
    precio_toldo = 0
    try:
        for n in componentes:
            precio = float(n["precio_unitario"])
            cantidad = float(n["cantidad"])
            resultado = precio * cantidad
            precio_toldo = precio_toldo + resultado
        return precio_toldo
    except:
        return precio_toldo
    
### metodos get para sacar productos por proveedor y po nombre

@app.route('/proveedor/<proveedor>', methods=['GET'])
def get_proveedor(proveedor):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM productos_proveedores WHERE proveedor = '{0}';".format(proveedor)
        print(sql)
        cursor.execute(sql)
        datos = cursor.fetchall()
        print(datos)
        productos = []
        for fila in datos:
            if len(fila)>1:
                fila = {'id_producto': fila[0], 'proveedor': fila[1], 'precio_unitario': str(fila[2]), 'descripcion_producto': fila[3], 'Calificacion': str(fila[4])}
                productos.append(fila)
        return jsonify({"Productos": productos})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})
@app.route('/producto/<descripcion_producto>', methods=['GET'])
def get_producto(descripcion_producto):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM productos_proveedores WHERE descripcion_producto = '{0}';".format(descripcion_producto)
        print(sql)
        cursor.execute(sql)
        datos = cursor.fetchall()
        print(datos)
        productos = []
        for fila in datos:
            if len(fila)>1:
                fila = {'id_producto': fila[0], 'proveedor': fila[1], 'precio_unitario': str(fila[2]), 'descripcion_producto': fila[3], 'Calificacion': str(fila[4])}
                productos.append(fila)
        return jsonify({"Productos": productos})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

## Metodos para la tabla de proveedores


## metodo get

@app.route('/productos', methods=['GET'])
def listar_productos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * from productos_proveedores"
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos = []
        for fila in datos:
            if len(fila)>1:
                fila = {'id_producto': fila[0], 'proveedor': fila[1], 'precio_unitario': str(fila[2]), 'descripcion_producto': fila[3], 'Calificacion': str(fila[4])}
                productos.append(fila)
        return jsonify({"productos": productos})
    
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

def buscar_producto(descripcion_producto, proveedor):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM productos_proveedores WHERE descripcion_producto = '{0}' and proveedor = '{1}'".format(descripcion_producto, proveedor)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            return jsonify({"exito": True})
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/insertarproducto', methods=['POST'])

def registrar_producto():
     
    print(request.json)
    if (validar_nombre_toldo(request.json['proveedor']) and validar_cantidad(request.json['precio_unitario']) and validar_id_producto(request.json['descripcion_producto'])):
        try:
            productos = buscar_producto(request.json['descripcion_producto'], request.json['proveedor'])
            print(productos)
            if productos != None:
                return jsonify({'mensaje': "Código ya existe, no se puede duplicar.", 'exito': False})
            else:
                cursor = conexion.connection.cursor()
                sql = """INSERT INTO productos_proveedores (proveedor, precio_unitario, descripcion_producto, calificacion) 
                VALUES ('{0}', '{1}', '{2}', '{3}')""".format(request.json['proveedor'], request.json['precio_unitario'], request.json['descripcion_producto'], request.json["Calificacion"])
                cursor.execute(sql)
                conexion.connection.commit()
                return jsonify({'mensaje': "Producto registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return jsonify({'mensaje': "Parámetros inválidos...", 'exito': False})


## Metodos delete para tabla toldos

@app.route('/eliminarproducto/<id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
    try:
        cursor = conexion.connection.cursor()
        sql = "DELETE FROM productos_proveedores WHERE id_producto = '{0}'".format(id_producto)
        cursor.execute(sql)
        cursor.connection.commit()
        return jsonify({"toldo eliminado": id_producto})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})







## Metodos put para tabla producto

@app.route('/modificarproducto/<id_producto>', methods=['PUT'])
def modificar_producto(id_producto):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE productos_proveedores SET precio_unitario = '{1}',  descripcion_producto = '{2}', proveedor = '{3}', Calificacion = '{4}' WHERE id_producto = '{0}'".format(id_producto, request.json["precio_unitario"], request.json["descripcion_producto"], request.json["proveedor"], request.json["Calificacion"])
        print(sql)
        cursor.execute(sql)
        cursor.connection.commit()
        return jsonify({"producto modificado": id_producto})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

## Metodos put para tabla toldos

@app.route('/modificartoldo/<id_inc>', methods=['PUT'])
def modificar_toldo(id_inc):
    try:
        cursor = conexion.connection.cursor()
        sql = "UPDATE toldos SET cantidad = '{1}',  id_producto = {'{2}' WHERE id_inc = '{0}'".format(id_inc, request.json["cantidad"], request.json["id_producto"])
        cursor.execute(sql)
        cursor.connection.commit()
        return jsonify({"toldo modificado": id_inc})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})








def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
