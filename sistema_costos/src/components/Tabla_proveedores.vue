<template>
  <div id="TablaCostos">
    <div class="form-group">
      <label>Buscar por proveedores: </label>

      <select v-model="selected">
        <option
          v-for="producto in productos"
          :key="producto.id_producto"
          v-bind:value="{ producto }"
        >
          {{ producto.proveedor }}
        </option>
      </select>
      <button
        class="btn btn-info ml-2"
        @click="$emit('proveedor-buscar', this.selected.producto.proveedor)"
      >
        Buscar
      </button>
    </div>
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
      <button
        class="btn btn-info ml-2"
        @click="limpiar_datos"
      >
        Limpiar
      </button>
    </div>
    <div v-if="!productos.length" class="alert alert-info" role="alert">
      No hay productos que coincidan con la busqueda
    </div>
    <div class="table-responsive">
    <table class="table" >
      <thead>
        <tr>
          <th>Id producto</th>
          <th>Proveedor</th>
          <th>Precio unitario</th>
          <th>Descripcion producto</th>
          <th>Calificacion</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producto in datosPaginados" :key="producto.id_producto">
        <td>{{ producto.id_producto }}</td>
          <td v-if="editando === producto.id_producto">
           <input
              type="text"
              class="form-control"
              v-model="producto.proveedor"
            />
          </td>
          <td v-else>
                      {{ producto.proveedor }}
          </td>
          <td v-if="editando === producto.id_producto">
            <input
              type="text"
              step="any"
              class="form-control"
              v-model="producto.precio_unitario"
            />
          </td>
          <td v-else>
            {{ producto.precio_unitario }}
          </td>
          <td v-if="editando === producto.id_producto">
            <input
              type="text"
              class="form-control"
              v-model="producto.descripcion_producto"
            />
          </td>
          <td>
            {{ producto.descripcion_producto }}
          </td>
          <td v-if="editando === producto.Calificacion">
            <input
              type="text"
              class="form-control"
              v-model="producto.Calificacion"
            />
          </td>
          <td v-else>
            {{ producto.Calificacion }}
          </td>
          <td v-if="editando === producto.id_producto">
            <button class="btn btn-success" @click="guardarproducto(producto)">💾 Guardar
            </button>
            <button class="btn btn-secondary ml-2" @click="cancelarEdicion(producto)">❌ Cancelar
            </button>
          </td>
          <td v-else>
            <button class="btn btn-info ml-2" @click="editarproducto(producto)">✏️ Editar</button>
            <button class="btn btn-danger" @click="$emit('delete-producto', producto.id_producto)">🗑 Eliminar
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
</template>
<script>
export default {
  name: "tablaProveedores",
  props: {
    productos: Array,
  },
  selected: "",
  nombre: "",
    data() {
    return {
      editando: null,
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
    editarproducto(producto) {
      this.productoEditado = Object.assign({}, producto);
      this.editando = producto.id_producto;
    },
    cancelarEdicion(producto) {
      Object.assign(producto, this.productoEditado);
      this.editando = null;
    },
    guardarproducto(producto) {
      var prec = producto.precio_unitario.toString()
      if (
        !prec.length ||
        !producto.descripcion_producto.length
      ) {
        return;
      }
      this.$emit("actualizar-producto", producto.id_producto, producto);
      this.editando = null;
      },
      buscar_productos() {
      this.$emit("producto-buscar", this.buscador);
    },
      buscar_() {
      clearTimeout(this.setTimeoutbuscador);
      this.setTimeoutbuscador = setTimeout(this.buscar_productos, 460);
    },
    totalPaginas() {
      return Math.ceil(this.productos.length / this.elementosPorPagina);
    },
    getDataPagina(noPagina) {
      this.paginaActual = noPagina;
      let ini = (noPagina * this.elementosPorPagina) - this.elementosPorPagina;
      let fin = (noPagina * this.elementosPorPagina);
      this.datosPaginados = this.productos.slice(ini, fin);
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
      return noPagina == this.paginaActual ? "active":""
    },
    limpiar_datos(){
      this.$emit('limpiar-datos')
      this.buscador = "",
      this.selected = ""
    }
    
  },
};
</script>
<style scoped></style>