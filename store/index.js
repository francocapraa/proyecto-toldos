/*
import Vue from "vue";
import Vuex from "vuex";
import axios from "axios"
Vue.use(Vuex);
*/
/*const store = new Vuex.Store({
  state: {
    users: [],
    username: null,
    contrasena: null,
    auth: false
  },
  mutations: {
    setUsers(state, users) {
      state.users = users;
    },
    doLogin(state, username, contrasena) {
      state.auth = true;
      state.username = username;
      state.contrasena = contrasena;
    },
    doLogout(state) {
      state.auth = false;
      state.username = null;
    }
  },
  actions: {
    doLogin({ commit }, username, contrasena) {
        let json = {
            "usuario": this.username,
            "contrasena": this.contrasena
          };
        axios.post("http://localhost:5000/login", json)
        .then( data =>{
          if(data.data.datos == "321rte980"){
            localStorage.token = data.data.datos;
            commit("doLogin", username, contrasena);
          }else{
            this.error = true;
            this.error_msg = data.data.datos
          }
        })
    },
    doLogout({ commit }) {
      commit("doLogout");
    },
    async setUsers({ commit }) {
      const users = window.localStorage.getItem("users");
      if (users) {
        commit("setUsers", JSON.parse(users));
      } else {
        try {
          await fetch("https://randomuser.me/api/?results=100")
            .then(data => data.json())
            .then(data => {
              commit("setUsers", data.results);
              window.localStorage.setItem(
                "users",
                JSON.stringify(data.results)
              );
            });
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
});
/*
export default store;

store.dispatch("setUsers"); 
*/