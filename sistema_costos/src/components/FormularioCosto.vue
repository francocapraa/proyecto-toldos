<template>
<div class=".col-sm-6 .col-md-5 .offset-md-2 .col-lg-6 .offset-lg-0">
  <div id="FormularioCosto">
    <form @submit.prevent="enviarFormulario">
      <p>Agregar un costo a un toldo ya existente</p>
          
          <div class="col-md-4">
            <label>Nombre del toldo: </label>              
            <select v-model="eleccion">
              <option v-for="toldo in costos" :key="toldo.id_inc" v-bind:value="{toldo}">
                {{ toldo.nombre_toldo }}
              </option>
            </select>
              </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Id toldo</label>
              <div class="form-control">
              <p><span v-if="eleccion">{{ eleccion.toldo.id_toldo }}</span></p>
              </div>
            </div>
          </div>
                    <div class="col-md-4">
            <label>Descripcion producto a agregar: </label>              
            <select v-model="selected">
              <option v-for="toldo in costos" :key="toldo.id_inc" v-bind:value="{toldo}">
                {{ toldo.descripcion_producto }}
              </option>
            </select>
              </div>

          <div class="col-md-4">
            <div class="form-group">
              <label>Id producto</label>
              <div class="form-control">
              <p><span v-if="selected">{{ selected.toldo.id_producto }}</span></p>
            </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Precio unitario</label>
              <div class="form-control">
              <p><span v-if="selected">{{ selected.toldo.precio_unitario }}</span></p>
            </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Cantidad</label>
              <input
                v-model="toldo.cantidad"
                type="number"
                step="any"
                class="form-control"
              />
            </div>
          </div>
        <div class="row">
          <div class="col-md-4">
            <div class="form-group">
              <button class="btn btn-primary">Añadir toldo</button>
            </div>
          </div>
        </div>
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
                El costo ha sido agregado correctamente!
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
  name: "formularioCosto",

  data() {
    return {
      procesando: false,
      correcto: false,
      error: false,
      costos : [],
      toldo: {
        nombre_toldo: "",
        descripcion_producto: "",
        cantidad: "",
      },
      selected:"",
      eleccion:"",
    };
  },
  mounted(){
       this.traer_data()
       console.log(this.costos)
     },
  methods: {
    async traer_data(){
      let response = await axios.get("http://localhost:5000/toldos")
      console.log(response.data)
      this.costos = response.data["toldos"]; 
     },
    enviarFormulario() {
      this.procesando = true;
      this.resetEstado();
      console.log(this.toldo);
      this.$emit("add-toldo-nuevo", this.toldo, this.selected, this.eleccion);
      this.$refs.id_toldo.focus();
      this.error = false;
      this.correcto = true;
      this.procesando = false;
      this.toldo = {
        id_toldo: "",
        nombre_toldo: "",
        id_producto: "",
        cantidad: "",
      };
    },
    resetEstado() {
      this.correcto = false;
      this.error = false;
    },
  },
  computed: {
    id_toldoInvalido() {
      var id_toldo = this.costo.id_toldo.toString();
      return id_toldo.length < 1;
    },
    nombre_toldoInvalido() {
      var nombre_toldo = this.costo.nombre_toldo.toString();
      return nombre_toldo.length < 1;
    },
    id_productoInvalido() {
      var id_producto = this.costo.id_producto.toString();
      return id_producto.length < 1;
    },
    descripcion_productoInvalido() {
      var descripcion_producto = this.costo.descripcion_producto.toString();
      return descripcion_producto.length < 1;
    },
    precio_unitarioInvalido() {
      var precio_unitario = this.costo.precio_unitario.toString();
      return precio_unitario.length < 1;
    },
    cantidadInvalido() {
      var cantidad = this.costo.cantidad.toString();
      return cantidad.length < 1;
    },
  },
};
</script>
<style scoped>
form {
  margin-bottom: 2rem;
}
</style>
