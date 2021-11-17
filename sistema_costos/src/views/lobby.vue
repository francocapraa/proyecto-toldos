<template>
   <div>
        <head>
        <div class="pos-f-t">
  <div class="collapse" id="navbarToggleExternalContent">
    <div class="bg-dark p-4">
      <h4 class="text-white">Collapsed content</h4>
      <span class="text-muted">Toggleable via the navbar brand.</span>
    </div>
  </div>
  <nav class="navbar navbar-dark bg-dark">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
  </nav>
</div>
</head>

 <header class = "page-header header container-fluid">
        </header>  
        
        <div class="background">
        <h1>¡Bienvenido al centro de costos!</h1>
        <div class="row justify-content-between">
        <div class="col-md-4">
            <div class="form-group" >
                <button @click="anadir_toldo" class="btn btn-secondary">Añadir toldo</button>
            </div>
        </div>
        <div class="col-md-4">
            <div class="form-group">
                <button @click="anadir_producto" class="btn btn-secondary">Precio proveedores</button>
            </div>
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
<style scoped>

.background {
                background: url('../assets/fondox.jpg');
                padding: 11em 0;
                min-height:100%;
                background-size:cover;
}
h1{
    font-weight: 700;
}


</style>