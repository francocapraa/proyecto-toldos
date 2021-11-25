<template> 
    <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <router-link to="/" class="nav-link activate" aria-current="page">Inicio</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/lobby" class="nav-link" aria-current="page">Lobby</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/toldos" class="nav-link" aria-current="page">Toldos</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/proveedores" class="nav-link" aria-current="page">Proveedores</router-link>
          </li>
        </ul>
      </div>
    </nav>
     <router-view/>
     </div>
  
</template>






<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
