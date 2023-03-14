<template>
  <navbar></navbar>
  <div class="activate">
     <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title"> Активация почты </h1>
          <div v-if="Object.keys(errors).length > 0 ||uid === undefined ||uid.length === 0 " >
            <form ref="loginForm" @submit.prevent="resend_activation">
               <div class="field">
                <label>E-mail</label>
                <div class="control">
                  <input type="email" class="input" v-model="email">
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <button class="button is-dark"> Отправить письмо </button>
                </div>
              </div>
            </form>
          </div>
<!--          <div class="field">-->
<!--              <button class="button is-dark"  v-if="isAuthenticated">-->
<!--                <router-link to="/cart">В корзину</router-link>-->
<!--              </button>-->
<!--              <button class="button is-dark"  v-if="!isAuthenticated">-->
<!--                <router-link to="/log-in">Войти</router-link>-->
<!--              </button>-->
<!--          </div>-->
      </div>
     </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {mapGetters} from "vuex";
import {toast} from "bulma-toast";
export default {
  name: "Activate",
  components: {Navbar},
  data(){
    return{
      uid: this.$route.params.uid,
      token: this.$route.params.token,
      email:'',
      errors: {},
      success: {},
    }
  },
  mounted() {
    if( this.uid !== undefined && this.token !== undefined){
      if(this.uid.length > 0 && this.token.length > 0 )
        this.activate()
        this.$router.push("/cart")
    }
  },
  methods:{
    activate(){
      axios.defaults.headers.common["Authorization"] = ""
      axios
          .post("http://localhost:8000/auth/users/activation/",{
            uid: this.uid,
            token: this.token,
          })
          .then(response => {
            toast({
                message: 'Ура! Ваша почта активирована',
                type: 'is-dark',
                dismissible: true,
                pauseOnHover: true,
                duration: 20000,
                position: 'bottom-right',
              })
            console.log(response.data)
          })
          .catch(error => {
            toast({
                message: 'Что-то пошло не так. Попробуйте снова',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 20000,
                position: 'bottom-right',
              })
          })
    },
    resend_activation(){
      axios.defaults.headers.common["Authorization"] = ""
      axios
          .post('http://localhost:8000/auth/users/resend_activation/',{
            email: this.email
          })
          .then(response =>{
            const status = response.status
            toast({
                message: status === 400 ? "Письмо было отправлено на почту" : status,
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 20000,
                position: 'bottom-right',
              })
            console.log(response.data)
          })
          .catch(error => {
            const status = error.response.status
            toast({
                message: status === 400 ? error.response.statusText : status,
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 20000,
                position: 'bottom-right',
              })
          })
    },
  },
  computed:{
    ...mapGetters({
         isAuthenticated: "isAuthenticated",
    }),
  }
}
</script>

<style scoped>

</style>