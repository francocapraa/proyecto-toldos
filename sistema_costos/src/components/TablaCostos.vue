<template>
  <div id="TablaCostos">
    <div v-if="!costos.length" class="alert alert-info" role="alert">
      No se han agregado personas
    </div>
    <div class="table-responsive">
    <table class="table" >
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
        <tr v-for="toldo in costos" :key="toldo.id_inc">
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
            <button class="btn btn-success" @click="guardartoldo(toldo)">💾 Guardar
            </button>
            <button class="btn btn-secondary ml-2" @click="cancelarEdicion(toldo)">❌ Cancelar
            </button>
          </td>
          <td v-else>
            <button class="btn btn-info ml-2" @click="editartoldo(toldo)">✏️ Editar</button>
            <button class="btn btn-danger" @click="$emit('delete-toldo', toldo.id_inc)">🗑 Eliminar
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
  name: "TablaCostos",
  props: {
    costos: Array,
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
      var cantid = toldo.cantidad.toString()
      var id_po = toldo.id_producto.toString()
      console.log(toldo.cantidad)
      if (
        !cantid.length ||
        !id_po.length
      ) {
        return;
      }
      this.$emit("actualizar-toldo", toldo.id_inc, toldo);
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