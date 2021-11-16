import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Lobby from "../views/lobby.vue"
import Toldos from "../views/Toldos.vue"
import Proveedores from "../views/Proveedores.vue";


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/lobby',
    name: 'Lobby',
    component: Lobby
  },
  {
    path: '/toldos',
    name: 'Toldos',
    component: Toldos
  },
  {
    path: '/proveedores',
    name: 'Proveedores',
    component: Proveedores
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router


