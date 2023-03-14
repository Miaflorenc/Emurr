<template>
  <header class="header">
		<div class="container">
			<div class="row">
				<div class="col">
					<div class="header_content d-flex flex-row align-items-center justify-content-start">
						<div class="logo">
							<router-link to="/">
								<div>The ЭMurr</div>
								<div>restaurant</div>
							</router-link>
						</div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="page-sign-up">
		<img style="width: 1920px; height:500px" src="../assets/images/home.jpg">
		<div class="home_container">
			<div class="container">
				<div class="row">
					<div class="col">
						<div class="home_content text-center">
							<div class="home_subtitle page_subtitle">Регистрация</div>
						</div>
					</div>
				</div>
			</div>
		</div>
      <div class="column is-4 is-offset-4">
        <form ref="registerForm" @submit.prevent="submitForm">
          <div class="field">
            <label>Имя пользователя</label>
            <div class="control">
              <input type="text" class="input" v-model="username">
            </div>
          </div>
          <div class="field">
            <label>E-mail</label>
            <div class="control">
              <input type="email" class="input" v-model="email">
            </div>
          </div>
          <div class="field">
            <label>Пароль</label>
            <div class="control">
              <input type="password" class="input" v-model="password">
            </div>
          </div>
          <div class="field">
            <label>Подтвердите пароль</label>
            <div class="control">
              <input type="password" class="input" v-model="password2">
            </div>
          </div>
          <dt v-for="(values, name) in errors" :key="name">
                <dl>
                    <div v-if="Array.isArray(values)"> <li v-for="value in values" :key="value"> {{ value }} </li></div>
                    <div v-else> <li> {{ values }} </li> </div>
                </dl>
            </dt>
          <div class="field">
            <div class="control">
              <button class="button is-dark"> Зарегистрироваться </button>
            </div>
          </div>
          <hr>
            Уже зарегистрированы? <router-link to="/log-in"> Войти </router-link>
        </form>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import Navbar from "@/components/Navbar";
export default {
  name: "SignUp",
  components: {Navbar},
  data(){
    return{
      username: '',
      email: '',
      password: '',
      password2: '',
      errors: [],
    }
  },
  mounted() {
    document.title = 'Регистрация | Эmurr'
  },
  methods:{
    submitForm(){
      this.errors = []
      if (this.username ==='')
        this.errors.push('Введите имя пользователя')
       if (this.email ==='')
        this.errors.push('Введите e-mail')
      if (this.password ==='')
        this.errors.push('Введите пароль')
      if (this.password !== this.password2)
        this.errors.push('Пароли не совпадают')
      if (!this.errors.length) {
        axios
            .post('http://127.0.0.1:8000/auth/users/', {
              username: this.username,
              password: this.password,
              password2: this.password2,
              email: this.email,
            })
            .then(response => {
              toast({
                message: 'Регистрация прошла успешно! Подтвердите e-mail, чтобы войти в аккаунт',
                type: 'is-dark',
                dismissible: true,
                pauseOnHover: true,
                duration: 20000,
                position: 'bottom-right',
              })
              this.$router.push('log-in')
            })
            .catch(error => {
              this.errors = error.response.data;
              console.log(this.errors);
            })
        }
      }
    },
  }
</script>

<style scoped>
</style>