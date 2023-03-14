<template>
  <header class="header">
		<div class="container">
			<div class="row">
				<div class="col">
					<div class="header_content d-flex flex-row align-items-center justify-content-start">
						<div class="logo">
							<a href="/">
								<div>The ЭMurr</div>
								<div>restaurant</div>
							</a>
						</div>
						<nav class="main_nav">
							<ul class="d-flex flex-row align-items-center justify-content-start">
								<li><a href="/">На главную</a></li>
								<li><router-link to="/reviews"> О нас </router-link></li>
								<li><router-link to="/menu"> Меню </router-link></li>
								<li>
                    <router-link to="/orders" v-if="username==='root'"> Страница Администратора </router-link>
                    <router-link to="/client" v-else> Личный кабинет </router-link>
                </li>
                <li>
                  <router-link to="/cart">
                    <span> Корзина </span>
                    <span class="icon">
                      <i class="fas fa-shopping-cart"></i>
                    </span>
                  </router-link>
                </li>
                <li>{{username}}</li>
                </ul>
						</nav>
            <router-link to="/log-in" class="reservations_phone ml-auto main_nav " v-if="!isAuthenticated"> Вход </router-link>
						<a class="reservations_phone ml-auto" v-if="isAuthenticated" @click="LogOut()"> Выйти </a>
					</div>
				</div>
			</div>
		</div>
	</header>
	<div class="hamburger_bar trans_400 d-flex flex-row align-items-center justify-content-start">
		<div class="hamburger">
			<div class="menu_toggle d-flex flex-row align-items-center justify-content-start">
				<div class="hamburger_container">
					<div class="menu_hamburger">
						<div class="line_1 hamburger_lines" style="transform: matrix(1, 0, 0, 1, 0, 0);"></div>
						<div class="line_2 hamburger_lines" style="visibility: inherit; opacity: 1;"></div>
						<div class="line_3 hamburger_lines" style="transform: matrix(1, 0, 0, 1, 0, 0);"></div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="menu trans_800">
		<div class="menu_content d-flex flex-column align-items-center justify-content-center text-center">
			<ul>
				<li><a href="/">На главную</a></li>
        <li><router-link to="/reviews"> О нас </router-link></li>
        <li><router-link to="/menu"> Меню </router-link></li>
        <li>
          <router-link to="/orders" v-if="username==='root'"> Заказы </router-link>
          <router-link to="/client" v-else> Мои заказы </router-link>
        </li>
        <li>
          <router-link to="/cart">
            <span class="icon">
              <i class="fas fa-shopping-cart"></i>
            </span>
            <span> Корзина </span>
          </router-link>
        </li>
        <li>{{username}}</li>
        <li>
          <router-link to="/log-in" v-if="!isAuthenticated"> Вход </router-link>
          <a v-if="isAuthenticated" @click="LogOut()"> Выйти </a>
        </li>
			</ul>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import {mapGetters} from "vuex";

export default {
  name: "Navbar",
  data(){
    return{
      showMobileMenu: false,
    }
  },
  mounted() {
    this.$store.commit('initializeStore')
  },
  methods:{
    LogOut(){
      this.$store.commit('removeToken')
      this.$router.push('/log-in')
    }
  },
  computed:{
    ...mapGetters({
          isAuthenticated: "isAuthenticated",
          username: "username"
    }),
  }
}
</script>

<style scoped>

</style>