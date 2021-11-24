
<template>
<div class=".col-sm-6 .col-md-5 .col-lg-6">
  <div id="formularioproducto">
    <form @submit.prevent="enviarFormularioproducto">
      <br>
      <br>
      <legend>Agregar un nuevo producto</legend>
              <div class="container">
                <div class="row">
                  <div class="col-md-4">
                      <div class="form-group">
                          <label>Descripcion del producto</label>
                              <input v-model="producto.descripcion_producto" type="text" class="form-control"/>
                      </div>
                  </div>
          
              <div class="col-md-4">
                      <div class="form-group">
                          <label>Proveedor</label>
                              <input v-model="producto.proveedor" type="text" class="form-control"/>
                      </div>
              </div>
          
              <div class="col-md-4">
                  <div class="form-group">
                    <label>Precio unitario</label>
                      <input v-model="producto.precio_unitario" type="number" step="any" class="form-control"/>
            </div>
          </div>
                        <div class="col-md-4">
                  <div class="form-group">
                    <label>Calificacion</label>
                      <input v-model="producto.Calificacion" type="text" class="form-control"/>
            </div>
          </div>
         
              <button type="button" class="btn btn-secondary btn-lg btn-block"  @click="enviarFormularioproducto">Añadir producto</button>
            
        <div class="container">
          <div class="row">
            <div class="col-md-12">
              <div
                v-if="error && procesando"
                class="alert alert-danger"
                role="alert"
              >
                Debes rellenar todos los campos!
              </div>
              <div v-if="correcto" class="alert alert-success" role="alert">
                El producto ha sido agregado correctamente!
              </div>
            </div>
          </div>
          </div>
          </div>
        </div>
    </form>
    </div>
    </div>
</template>

<script>
import axios from "axios"
export default {
  name: "formularioproducto",

  data() {
    return {
      procesando: false,
      correcto: false,
      error: false,
      productos : [],
      producto: {
        descripcion_producto: "",
        precio_unitario: "",
        Calificacion:"",
        proveedor:"",
      },
    };
  },
  mounted(){
       this.traer_data()
       console.log(this.productos)
     },
  methods: {
    async traer_data(){
      let response = await axios.get("http://localhost:5000/productos")
      console.log(response.data)
      this.productos = response.data["productos"]; 
     },
    enviarFormularioproducto() {
      this.procesando = true;
      this.resetEstado();
      console.log(this.producto);
      this.$emit("add-producto", this.producto);
      this.verificar_existencia(this.producto.descripcion_producto)
      this.error = false;
      this.procesando = false;
      this.producto = {
        descripcion_producto: "",
        precio_unitario: "",
        Calificacion:"",
        proveedor:"",
      };
    },
    async verificar_existencia(descripcion_producto){
      try {
        var link = "http://localhost:5000/producto/" + descripcion_producto
        const response = await axios.get(link);
        console.log(response.data["Productos"], "iji")
        if (response.data["Productos"].length > 0){
          this.correcto = true
        }
        else{
          this.correcto = false
        }
      } catch (error) {
        console.log(error);
      }

},
    resetEstado() {
      this.correcto = false;
      this.error = false;
    },
  },
  computed: {
    descripcion_productoInvalido() {
      var descripcion_producto = this.producto.descripcion_producto.toString();
      return descripcion_producto.length < 1;
    },
    precio_unitarioInvalido() {
      var precio_unitario = this.producto.precio_unitario.toString();
      return precio_unitario.length < 1;
    },
    proveedorInvalido() {
      var proveedor = this.producto.proveedor.toString();
      return proveedor.length < 1;
    },
    CalificacionInvalido() {
      var Calificacion = this.producto.Calificacion.toString();
      return Calificacion.length < 1;
    },
  },
};
</script>
<style scoped>
form {
  margin-bottom: 2rem;
}
</style>
