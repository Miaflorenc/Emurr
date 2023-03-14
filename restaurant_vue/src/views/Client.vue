<template>
<Navbar></Navbar>
  <div class="page-orders">
    <img src="../assets/images/home.jpg">
		<div class="home_container">
			<div class="container">
				<div class="row">
					<div class="col">
						<div class="home_content text-center">
							<div class="home_subtitle page_subtitle">The EMurr</div>
							<div class="home_title"><h1>Личный кабинет</h1></div>
							<div class="home_text ml-auto mr-auto">
								<p>Здесь вы можете управлять заказами и  бронированием</p>
							</div>
						</div>
					</div>
				</div>
	  	</div>
	  </div>
    <div class="text-center">
      <div class="button sig_button trans_200" @click="CliOrders" v-on:click="isOpen = 1"><a> Заказы </a></div>
      <div class="button sig_button trans_200" @click="GetBooking(user)" v-on:click="isOpen = 2"> Забронированные столы </div>
    </div>
    <div class="columns is-multiline" v-if="isOpen === 1">
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="orders.length!==0">
          <thead>
            <tr>
              <th>Блюдо</th>
              <th>Количество</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
             <tr v-for="ord in orders">
              <td>{{ ord.product_name }}</td>
              <td>{{ ord.quantity }}  </td>
              <td><button class="delete" @click="DeleteOrder(ord.id)"></button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-if="isOpen === 2">
      <div class="column is-12">
        <h1 class="title column">Забронированные столики</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="booking.length!==0">
          <thead>
            <tr>
              <th>Дата</th>
              <th>Время</th>
              <th>Количество персон</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
             <tr v-for="books in booking">
              <td>{{ books.date }} </td>
              <td>{{ books.time }}</td>
              <td>{{ books.persons }}  </td>
              <td><button class="delete" @click="DeleteBooking(books.id)"></button></td>
            </tr>
          </tbody>
        </table>
        <p v-else> У вас пока нет забронированных столиков </p>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {toast} from "bulma-toast";
export default {
  name: "Client",
  components: {Navbar},
  data(){
    return{
      orders: [],
      user: '',
      isOpen: 0,
      booking: '',
    }
  },
  mounted() {
    this.GetUserIdCli()
  },
  methods:{
    GetUserIdCli(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      axios
            .get('http://127.0.0.1:8000/auth/users/me')
            .then(response =>{
              this.user = response.data.id
            })
    },
    CliOrders(){
     axios
          .get('http://localhost:8000/api/v1/orderscli/'+ this.user)
          .then(response=>{
            this.orders = response.data
          })
   },
    DeleteOrder(id){
      axios
          .delete('http://localhost:8000/api/v1/orders-delete/' + id)
          .then(response => {
                  toast({
                      message: 'Заказ удален',
                      type: 'is-dark',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                    })
                  this.orders = this.orders.filter(el => el.id !== id)
              })
    },
    GetBooking(idcli){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      axios
          .get('http://localhost:8000/api/v4/get_booking/' + idcli)
          .then(response =>{
            this.booking = response.data
          })

    },
    DeleteBooking(id){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      axios
          .delete('http://localhost:8000/api/v4/delete_booking/' + id)
          .then(response => {
                  toast({
                      message: 'Бронирование отменено',
                      type: 'is-dark',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                    })
                  this.booking = this.booking.filter(el => el.id !== id)
              })
    },
  }
}
</script>

<style scoped>

</style>