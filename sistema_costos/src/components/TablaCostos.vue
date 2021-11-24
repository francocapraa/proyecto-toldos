<template>
  <div id="TablaCostos" class="display">
    <form class="form-inline my-2 my-lg-0">
      <input
        class="form-control mr-sm-2 buscador"
        type="search"
        placeholder="Buscar por nombre"
        aria-label="Search"
        v-model="buscador"
        @keyup="buscar_"
      />
    </form>
    <div class="form-group">
      <button class="btn btn-info ml-2" @click="limpiar_datos">Limpiar</button>
    </div>
    <div v-if="!costos.length" class="alert alert-info" role="alert">
      No hay toldos que conincidan con la busqueda
    </div>

    <div class="row">
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr>
              <th>Id toldo</th>
              <th>Nombre toldo</th>
              <th>Id producto</th>
              <th>Descripcion producto</th>
              <th>Precio unitario</th>
              <th>Cantidad</th>
              <th>acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="toldo in datosPaginados" :key="toldo.id_inc">
              <td>
                {{ toldo.id_toldo }}
              </td>
              <td>
                {{ toldo.nombre_toldo }}
              </td>
              <td v-if="editando === toldo.id_inc">
                <input
                  type="number"
                  class="form-control"
                  v-model="toldo.id_producto"
                />
              </td>
              <td v-else>
                {{ toldo.id_producto }}
              </td>
              <td>
                {{ toldo.descripcion_producto }}
              </td>
              <td>
                {{ toldo.precio_unitario }}
              </td>
              <td v-if="editando === toldo.id_inc">
                <input
                  type="number"
                  step="any"
                  class="form-control"
                  v-model="toldo.cantidad"
                />
              </td>
              <td v-else>
                {{ toldo.cantidad }}
              </td>
              <td v-if="editando === toldo.id_inc">
                <button class="btn btn-success" @click="guardartoldo(toldo)">
                  💾 Guardar
                </button>
                <button
                  class="btn btn-secondary ml-2"
                  @click="cancelarEdicion(toldo)"
                >
                  ❌ Cancelar
                </button>
              </td>
              <td v-else>
                <button class="btn btn-info ml-2" @click="editartoldo(toldo)">
                  ✏️ Editar
                </button>
                <button
                  class="btn btn-danger"
                  @click="$emit('delete-toldo', toldo.id_inc)"
                >
                  🗑 Eliminar
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <nav aria-label="Page navigation example">
          <ul class="pagination">
            <li class="page-item" v-on:click="getPreaviousPage()">
              <a class="page-link" href="#">Previous</a>
            </li>
            <li
              v-for="pagina in totalPaginas()"
              :key="pagina"
              v-on:click="getDataPagina(pagina)"
              class="page-item" v-bind:class="isActive(pagina)">
              <a class="page-link" href="#">{{ pagina }}</a>
            </li>
            <li class="page-item"  v-on:click="getNextPage()"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>
      </div>
    </div>
    <div v-if="buscador" class="bg-info">
      <h3>Precio del toldo: {{ precio }}</h3>
    </div>
  </div>
</template>
<script>
export default {
  name: "TablaCostos",
  props: {
    costos: Array,
    precio: Number,
  },
  data() {
    return {
      editando: null,
      selected: "",
      buscador: "",
      setTimeoutbuscador: "",
      elementosPorPagina: 3,
      datosPaginados: [],
      paginaActual:1
    };
  },
  mounted(){
    this.getDataPagina(1);
  },
  methods: {
    editartoldo(toldo) {
      this.toldoEditado = Object.assign({}, toldo);
      this.editando = toldo.id_inc;
    },
    cancelarEdicion(toldo) {
      Object.assign(toldo, this.toldoEditado);
      this.editando = null;
    },
    guardartoldo(toldo) {
      var cantid = toldo.cantidad.toString();
      var id_po = toldo.id_producto.toString();
      console.log(toldo.cantidad);
      if (!cantid.length || !id_po.length) {
        return;
      }
      this.$emit("actualizar-toldo", toldo.id_inc, toldo);
      this.editando = null;
    },
    limpiar_datos() {
      this.$emit("cargar-datos");
      (this.selected = ""), (this.buscador = "");
    },
    buscar_toldos() {
      this.$emit("toldo-buscar", this.buscador);
    },
    buscar_() {
      clearTimeout(this.setTimeoutbuscador);
      this.setTimeoutbuscador = setTimeout(this.buscar_toldos, 460);
    },
    totalPaginas() {
      return Math.ceil(this.costos.length / this.elementosPorPagina);
    },
    getDataPagina(noPagina) {
      this.paginaActual = noPagina;
      this.datosPaginados = [];
      let ini = (noPagina * this.elementosPorPagina) - this.elementosPorPagina;
      let fin = (noPagina * this.elementosPorPagina);
      this.datosPaginados = this.costos.slice(ini, fin);
    },

    getPreaviousPage(){
      if(this.paginaActual > 1){
        this.paginaActual--;
    }
    this.getDataPagina(this.paginaActual);
    },
    getNextPage(){
      if(this.paginaActual < this.totalPaginas()){
        this.paginaActual++;
    }
    this.getDataPagina(this.paginaActual);
    },

    isActive(noPagina){
      if(noPagina === this.PaginaActual){
        return "active";
      }
      else{
        return "";
      }
    }
  },
};
</script>
<style scoped></style>