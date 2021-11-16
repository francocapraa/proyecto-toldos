<template>
    <div>
        <h1>¡Bienvenido al centro de costos!</h1>
        <div class="row justify-content-between">
        <div class="col-md-4">
            <div class="form-group" >
                <button  @click="anadir_toldo" class="btn btn-primary">Añadir toldo</button>
            </div>
        </div>
        <div class="col-md-4">
            <div class="form-group">
                <button @click="anadir_producto" class="btn btn-primary">Precio proveedores</button>
            </div>
        </div>
         </div>
    </div>

</template>

<script>

export default {
        name:"Lobby",

        components: {

        },
        methods: {
            anadir_toldo(){
                this.$router.push("toldos");
            },
            anadir_producto(){
                this.$router.push("proveedores")
            }

        }
}
</script>
<style lang="stylus" scoped>

</style>