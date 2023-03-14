import { createRouter, createWebHistory } from 'vue-router'
import main from "@/views/Main";
import Menu from "@/views/Menu";
import Reviews from "@/views/Reviews";
import Cart from "@/views/Cart";
import SignUp from "@/views/SignUp";
import Activate from "@/views/Activate";
import LogIn from "@/views/LogIn";
import AdminOrders from "@/views/AdminOrders";
import Client from "@/views/Client";

const routes = [
  {path:'/', component: main, name: "ЭMurr"},
  {path: '/menu', component: Menu, name: "ЭMurr меню"},
  {path: '/reviews', component: Reviews, name: "Эmurr отзывы"},
  {path: '/cart', component: Cart, name: "Эmurr Корзина", meta: { requiresAuth: true }  },
  {path: '/sign-up', component: SignUp, name: "Эmurr Регистрация"},
  {path: '/activate/:uid/:token', component: Activate, name:"Эmurr Активация аккаунта"},
  {path: '/log-in', component: LogIn, name: "Эmurr Вход"},
  {path: '/orders', component: AdminOrders , name: "Эmurr Заказы"},
  {path: '/client', component: Client , name: "Эmurr Заказы клиента"},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (localStorage.getItem("token")) {
      next();
      return;
    }
    next("/log-in");
  } else {
    next();
  }
});
export default router
