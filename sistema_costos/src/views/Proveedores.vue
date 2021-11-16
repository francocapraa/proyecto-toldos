<template>
<div>
    <div class="row">
      <div class="col-md-12">
        <h1>Toldos</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="container">
        <formularioproducto  :productos="productos" @add-producto="agregarProducto" />
        <tablaProveedores :productos="productos" 
        @delete-producto="eliminarproducto" 
        @actualizar-producto="actualizarproducto"
        @proveedor-buscar="proveedor_buscar"
        @producto-buscar="producto_buscar"
        @limpiar-datos="getData"/>
        </div>
        </div>
      </div>
</div>
</template>
<script>

import axios from "axios"
import TablaProveedores from '../components/Tabla_proveedores.vue'
import formularioproducto from '../components/formulario_prov.vue'
//import https from "https"
export default {
  name: "Proveedores",
  components: {
    TablaProveedores,
    formularioproducto,
  },
  data() {
    return {
      productos: [],
    }
  },
 //   },
    created() {
      this.getData();
      },


methods: {
async agregarProducto(producto) {
  try {
      const response = await axios.post("http://localhost:5000/insertarproducto", producto);
      console.log(response)
      var result =  response["data"]
      var msg = result["mensaje"]
      console.log(msg)
          if ( result["mensaje"] == "Producto registrado."){
              this.productos= [...this.productos, { ...producto}];
          }
        } 
  catch (error) {
        console.log(error);
      }

},
//
eliminarproducto(id_producto){
  try{
    var link = "http://localhost:5000/eliminarproducto/" + id_producto
    
    axios.delete(link)
     .then(response => {
         console.log(response);
     });
  this.productos = this.productos.filter(
    producto => producto.id_producto !== id_producto

  );
  }
  catch (error) {
        console.log(error);
      }

},
actualizarproducto(id_producto, productoActualizado) {
      try{
      var link = "http://localhost:5000/modificarproducto/" + id_producto
      const response = axios.put(link, productoActualizado);
      console.log(response)
      this.productos = this.productos.map(producto => producto.id_producto === id_producto ? productoActualizado : producto)
      }
      catch (error) {
        console.log(error);
      }
},

async getData() {
      try {
        const response = await axios.get("http://localhost:5000/productos");
        console.log(response.data)
        this.productos = response.data["productos"];
        console.log(this.productos)
      } catch (error) {
        console.log(error);
      }

},
async proveedor_buscar(proveedor){ 
      try {
        var link = "http://localhost:5000/proveedor/" + proveedor
        const response = await axios.get(link);
        console.log(response.data)
        this.productos = response.data["Productos"]
      } catch (error) {
        console.log(error);
      }
},

async producto_buscar(producto){
  try {
        var link = "http://localhost:5000/producto/" + producto
        const response = await axios.get(link);
        console.log(response.data)
        this.productos = response.data["Productos"]
      } catch (error) {
        console.log(error);
      }

}
},
}

</script>

<style>
button {
  background: #009435;
  border: 1px solid #009435;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
