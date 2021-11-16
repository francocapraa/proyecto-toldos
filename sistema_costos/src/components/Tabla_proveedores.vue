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
        <div class="form-group">
      <button
        class="btn btn-info ml-2"
        @click="$emit('limpiar-datos')"
      >
        Limpiar
      </button>
    </div>
    <div class="form-group">
      <label>Buscar por descripcion: </label>

      <select v-model="nombre">
        <option
          v-for="producto in productos"
          :key="producto.id_producto"
          v-bind:value="{ producto }"
        >
          {{ producto.descripcion_producto }}
        </option>
      </select>
      <button
        class="btn btn-info ml-2"
        @click="$emit('producto-buscar', this.selected.producto.descripcion_producto)"
      >
        Buscar
      </button>
    </div>
        <div class="form-group">
      <button
        class="btn btn-info ml-2"
        @click="$emit('limpiar-datos')"
      >
        Limpiar
      </button>
    </div>
    <div v-if="!productos.length" class="alert alert-info" role="alert">
      No se han agregado personas
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
        <tr v-for="producto in productos" :key="producto.id_producto">
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
      }
    
  },
  data() {
    return {
      editando: null,
    };
  },
};
</script>
<style scoped></style>