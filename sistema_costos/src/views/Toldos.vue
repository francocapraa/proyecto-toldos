<template>
<div>
    <div class="row">
      <div class="col-md-12">
        <h1>Toldos</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="container">
  <div class="row justify-content-center justify-content-md-start">
        <formularioCosto  :costos="costos" @add-toldo="agregarToldo" />
        <formularioAgregartoldo :costos="costos" @add-toldo="agregarToldo"/>
        </div>
        <tablaCostos :costos="costos" 
        @delete-toldo="eliminartoldo" 
        @actualizar-toldo="actualizartoldo"/>
        </div>
        </div>
      </div>
</div>
</template>
<script>

import axios from "axios"
import TablaCostos from '../components/TablaCostos.vue'
import FormularioCosto from '../components/FormularioCosto.vue'
import FormularioAgregartoldo from '../components/Formulario_agregartoldo.vue'

//import https from "https"
export default {
  name: "Toldos",
  components: {
    FormularioCosto,
    TablaCostos,
    FormularioAgregartoldo,
  },
  data() {
    return {
      costos: [],
    }
  },
 //   },
    created() {
      this.getData();
      },
  // GET request using axios with error handling
  //const agent = new https.Agent({
  //  rejectUnauthorized: false,
//});
  //async () => {
 // var response = await axios.get('http://localhost/5000/toldos', { 
//    httpsAgent: agent
 // })
 // response = response()
 // console.log(response);
//  this.costos = response;
//
// https://medium.com/@dtkatz/3-ways-to-fix-the-cors-error-and-how-access-control-allow-origin-works-d97d55946d9
methods: {
async agregarToldo(toldo) {
  try {
      const response = await axios.post("http://localhost:5000/insertartoldo", toldo);
      console.log(response)
      var result =  response["data"]
      var msg = result["mensaje"]
      console.log(msg)
          if ( result["mensaje"] == "Costo registrado."){
              this.costos= [...this.costos, { ...toldo}];
          }
        } 
  catch (error) {
        console.log(error);
      }

},
eliminartoldo(id_inc){
  try{
    var link = "http://localhost:5000/eliminartoldo/" + id_inc
    
    axios.delete(link)
     .then(response => {
         console.log(response);
     });
  this.costos = this.costos.filter(
    toldo => toldo.id_inc !== id_inc

  );
  }
  catch (error) {
        console.log(error);
      }

},
actualizartoldo(id_inc, toldoActualizado) {
      try{
      var link = "http://localhost:5000/modificartoldo/" + id_inc
      const response = axios.put(link, toldoActualizado);
      console.log(response)
      this.costos = this.costos.map(toldo => toldo.id_inc === id_inc ? toldoActualizado : toldo)
      }
      catch (error) {
        console.log(error);
      }
},

async getData() {
      try {
        const response = await axios.get("http://localhost:5000/toldos");
        console.log(response.data)
        this.costos = response.data["toldos"];
      } catch (error) {
        console.log(error);
      }

}
},
}

</script>

<style>
button {
  background: #009435;
  border: 1px solid #009435;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
