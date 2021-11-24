<template>
   <div class="bueno">
        <div class="background">
          <a href="#" @click="onLogout">Logout</a>
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
    <footer class="bg-dark text-center text-white">
  <!-- Grid container -->
  <div class="container p-4">

    <section class="">
      <form action="">
        <!--Grid row-->
        <div class="row d-flex justify-content-center">
          <!--Grid column-->
<br>
        
          <!--Grid column-->
        </div>
        <!--Grid row-->
      </form>
    </section>
    <!-- Section: Form -->

    <!-- Section: Text -->
    <section class="mb-4">
      <p>
        Esta es una pagina para la administracion y actualizacion de costos de toldos   </p>
    </section>
  </div>

  <!-- Copyright -->
  <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
    © 2020 Copyright:
    <a class="text-white" href="https://mdbootstrap.com/">MDBootstrap.com</a>
  </div>
  <!-- Copyright -->
</footer>
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
            },
            onLogout() {
              this.$router.push("/");
              // sacar cookies?
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
                margin-bottom: 0;
}
h1{
    font-weight: 700;
}
#bueno {
    display: flex;
    flex-direction: column;
    height: 100%;
}


</style>