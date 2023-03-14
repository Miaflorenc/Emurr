<template>
  <Navbar></Navbar>
  <div class="page-cart">
    <img src="../assets/images/home.jpg">
		<div class="home_container">
			<div class="container">
				<div class="row">
					<div class="col">
						<div class="home_content text-center">
							<div class="home_subtitle page_subtitle">Корзина</div>
						</div>
					</div>
				</div>
	  	</div>
	  </div>
    <div class="columns is-multiline">
      <div class="column is-12 box" v-if="products.length!==0">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Блюдо</th>
              <th>Цена</th>
              <th>Количество</th>
              <th>Общая стоимость</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <CartItem v-for="product in products" v-bind:key="product.id" :product="product"/>
          </tbody>
          <thead>
            <tr>
              <th>Общая стоимость: {{cart_total}}</th>
            </tr>
          </thead>
        </table>
        <div class="column is-4 is-offset-4">
          <h1 class="title"> Сделайте заказ </h1>
            <form @submit.prevent="PostOrder">
              <div class="field">
                <div class="control">
                  <input placeholder="Введите номер столика"  type="number" class="input" v-model="table">
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <button class="button sig_button trans_200"> Заказать </button>
                </div>
              </div>
            </form>
        </div>
      </div>
        <div class="home_content text-center column" v-else>
							<div class="sig_title"><h1>Ваша корзина пуста</h1></div>
        </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import CartItem from "@/components/CartItem";
import axios  from "axios";
import {toast} from "bulma-toast";
export default {
  name: "Cart",
  components: {Navbar, CartItem},
  data(){
    return {
      table: '',
      userinfo: '',
      ordersArray: [],
    }
  },
  mounted() {
    this.$store.commit("updateCartFromLocalStorage")
    document.title = 'Корзина | Эmurr'
    this.GetUserId()
  },
  methods:{
    GetUserId(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      axios
          .get('http://127.0.0.1:8000/auth/users/me')
          .then(response =>{
            this.userinfo = response.data
          })
    },
    PostOrder(){
      let len = Object.keys(this.products).length;
            for (let i = 0; i < len; i++)
              this.ordersArray.push({
                username_id: this.userinfo.id,
                table: this.table,
                product_name: this.products[i].name,
                quantity: this.products[i].quantity
              });
      console.log(this.ordersArray)
      axios
          .post("http://localhost:8000/api/v1/orders", this.ordersArray)
          .then(response => {
              toast({
                  message: 'Уже начали готовить! Спасибо, что вы с нами',
                  type: 'is-dark',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
      this.ordersArray.length = 0
    },
  },
  computed: {
    products(){
      return this.$store.getters.cartItems
    },
    cart_total(){
      return this.$store.getters.cartTotal
    }
  }
}
</script>

<style scoped>

</style>