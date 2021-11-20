<template>
  <div id="FormularioCosto">
    <form @submit.prevent="enviarFormulario" class="form-row align-items-center">
      <legend> Agregar un costo a un toldo ya existente</legend>
          
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
              <div class="form-control mb-2 mr-sm-2">
              <p><span v-if="eleccion">{{ eleccion.toldo.id_toldo }}</span></p>
              </div>
            </div>
          </div>
                    <div class="col-md-4">
            <label>Descripcion producto a agregar: </label>              
            <select v-model="selected">
              <option                     v-for="producto in productos"
                    :key="producto.id_producto"
                    v-bind:value="{ producto }"
                  >
                    {{ producto.descripcion_producto }}
              </option>
            </select>
              </div>

          <div class="col-md-4">
            <div class="form-group">
              <label>Id producto</label>
              <div class="form-control mb-2 mr-sm-2">
              <p><span v-if="selected">{{ selected.producto.id_producto }}</span></p>
            </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Precio unitario</label>
              <div class="form-control">
              <p><span v-if="selected">{{ selected.producto.precio_unitario }}</span></p>
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
              <button type="button" class="btn btn-secondary btn-lg btn-block" @click="enviarFormulario">Añadir toldo</button>
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
</template>

<script>
import axios from "axios"
export default {
  name: "formularioCosto",

  data() {
    return {
      procesando: false,
      error: false,
      correcto: false,
      costos : [],
      productos: [],
      toldo: {
        nombre_toldo: "",
        descripcion_producto: "",
        cantidad: "",
      },
      selected:null,
      eleccion:null,
      ingreso: false
    };
  },
  mounted(){
       this.traer_data()
       this.traer_produ()
       console.log(this.costos)
     },
  methods: {
    async traer_data(){
      let response = await axios.get("http://localhost:5000/toldos")
      console.log(response.data)
      this.costos = response.data["toldos"]; 
     },
      async traer_produ() {
      let response = await axios.get("http://localhost:5000/productos");
      console.log(response.data);
      this.productos = response.data["productos"];
    },
    enviarFormulario() {
      this.procesando = true;
      console.log(this.toldo);
            console.log(this.selected);
                  console.log(this.eleccion);
      this.$emit("add-toldo-nuevo", this.toldo, this.selected, this.eleccion)
      this.error = false;
      this.procesando = false;
      this.toldo = {
        id_toldo: "",
        nombre_toldo: "",
        id_producto: "",
        cantidad: "",
      };
            this.resetEstado();
            console.log(this.ingreso)
    },
    resetEstado() {
      this.error = false;
      this.selected = null;
      this.eleccion = null
    },
  },
  computed: {
    id_toldoInvalido() {
      var id_toldo = this.toldo.id_toldo.toString();
      return id_toldo.length < 1;
    },
    nombre_toldoInvalido() {
      var nombre_toldo = this.toldo.nombre_toldo.toString();
      return nombre_toldo.length < 1;
    },
    id_productoInvalido() {
      var id_producto = this.toldo.id_producto.toString();
      return id_producto.length < 1;
    },
    descripcion_productoInvalido() {
      var descripcion_producto = this.toldo.descripcion_producto.toString();
      return descripcion_producto.length < 1;
    },
    precio_unitarioInvalido() {
      var precio_unitario = this.toldo.precio_unitario.toString();
      return precio_unitario.length < 1;
    },
    cantidadInvalido() {
      var cantidad = this.toldo.cantidad.toString();
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
