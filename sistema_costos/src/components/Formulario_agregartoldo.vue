<template>
  <div id="formularioAgregartoldo">
    <form @submit.prevent="enviarFormulario" class="form-row align-items-center">
          <legend class="font-weight-bold">Comenzar la creacion de un nuevo toldo</legend>
            <div class="col-md-4">
              <div class="form-group">
                <label>Nombre del toldo</label>
                <input
                  ref="toldo.nombre_toldo"
                  v-model="toldo.nombre_toldo"
                  type="text"
                  class="form-control"
                  :class="{ 'is-invalid': procesando && nombre_toldoInvalido }"
                  @focus="resetEstado"
                  @keypress="resetEstado"
                />
              </div>
            </div>
            <div class="col-md-4">
              <div class="form-group">
                <label>Id toldo</label>
                <input
                  v-model="toldo.id_toldo"
                  type="number"
                  class="form-control"
                />
              </div>
            </div>
            <div class="col-md-4">
                <label>Descripcion producto a agregar: </label>
              <div class="form-control">
                <select v-model="selected">
                  <option
                    v-for="producto in productos"
                    :key="producto.id_producto"
                    v-bind:value="{ producto }"
                  >
                    {{ producto.descripcion_producto }}
                  </option>
                </select>
              </div>
            </div>

            <div class="col-md-4">
              <div class="form-group">
                <label>Id producto:  </label>
                <div class="form-control mb-2 mr-sm-2">
                  <p>
                    <span v-if="selected">{{
                      selected.producto.id_producto
                    }}</span>
                  </p>
                </div>
              </div>
            </div>

            <div class="col-md-4">
              <div class="form-group">
                <label>Precio unitario:  </label>
                <div class="form-control">
                  <p>
                    <span v-if="selected">{{
                      selected.producto.precio_unitario
                    }}</span>
                  </p>
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
                  :class="{ 'is-invalid': procesando && cantidadInvalido }"
                  @focus="resetEstado"
                  @keypress="resetEstado"
                />
              </div>
            </div>
            <br>
            <br>
            
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
import axios from "axios";
export default {
  name: "formularioAgregartoldo",

  data() {
    return {
      procesando: false,
      error: false,
      correcto:false,
      costos: [],
      productos: [],
      toldo: {
        id_toldo: "",
        nombre_toldo: "",
        cantidad: "",
      },
      selected: "",
    };
  },
  mounted() {
    this.traer_data();
    this.traer_prod();
    console.log(this.costos);
  },
  methods: {
    async traer_data() {
      let response = await axios.get("http://localhost:5000/toldos");
      this.costos = response.data["toldos"];
    },
    async traer_prod() {
      let response = await axios.get("http://localhost:5000/productos");
      this.productos = response.data["productos"];
    },
    enviarFormulario() {
      this.procesando = true;
      console.log(this.toldo, this.selected, "tyler")
      this.$emit("add-toldo", this.toldo, this.selected);
     // this.verificar_existencia(this.toldo.nombre_toldo)
     this.correcto = true
      this.error = false;
      this.procesando = false;
      this.toldo = {
        id_toldo: "",
        nombre_toldo: "",
        id_producto: "",
        cantidad: "",
      };
      this.selected = "",
      this.eleccion = "",
      this.resetEstado();
      
    },
    resetEstado() {
      this.error = false;
    },
    async verificar_existencia(nombre_toldo){
      try {

        var link = "http://localhost:5000/toldo/" + nombre_toldo
        const response = await axios.get(link);
        console.log(response.data["Toldo"].length, "hokwdqio")
        if (response.data["Toldo"].length > 0){
          this.correcto = true
        }
        else{
          this.correcto = false
        }
      } catch (error) {
        console.log(error);
      }

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



 .select {
  background-color: #f6f6f6;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #f6f6f6;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}
</style>
