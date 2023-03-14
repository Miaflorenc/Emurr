<template>
<Navbar></Navbar>
  <div class="page-orders">
    <div class="home">
		<div class="parallax_background parallax-window" data-parallax="scroll" data-speed="0.8"><img src="../assets/images/home.jpg"></div>
		<div class="home_container">
			<div class="container">
				<div class="row">
					<div class="col">
						<div class="home_content text-center">
							<div class="home_subtitle page_subtitle">The EMurr is</div>
							<div class="home_title"><h1>Страница Администратора</h1></div>
							<div class="home_text ml-auto mr-auto">
								<p>Здесь вы можете управлять заказами, бронированием, и меню</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
    <div class="text-center">
      <div class="button sig_button trans_200" v-on:click="isOpenAdmin = 1"><a> Заказы </a></div>
      <div class="button sig_button trans_200" v-on:click="isOpenAdmin = 2"><a> Меню </a></div>
      <div class="button sig_button trans_200" v-on:click="isOpenAdmin = 3" @click="GetAllBookings"> Забронированные столики </div>
    </div>
    <div class="columns is-multiline" v-if="isOpenAdmin === 1">
      <div class="column is-12">
        <h1 class="title column">Заказы</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="orders.length!==0">
          <thead>
            <tr>
              <th>Клиент</th>
              <th>Номер столика</th>
              <th>Блюдо</th>
              <th>Количество</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
             <tr v-for="ord in orders">
              <td> <h1> {{ ord.username_id.username }} </h1> </td>
              <td>{{ ord.table }} </td>
              <td>{{ ord.product_name }}</td>
              <td>{{ ord.quantity }}  </td>
              <td><button class="delete" @click="DeleteOrder(ord.id)"></button></td>
            </tr>
          </tbody>
        </table>
        <p v-else> Пока заказов нет </p>
      </div>
    </div>
    <div v-if="isOpenAdmin === 2">
      <div class="columns is-multiline">
        <div class="column is-12">
            <h1 class="title column">Меню</h1>
        </div>
        <div class="center-block">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <button class="button sig_button trans_200" v-on:click="isOpen = 1"> Добавить блюдо </button>
            <button class="button sig_button trans_200" v-on:click="isOpen = 2"> Добавить категорию </button>
            <button class="button sig_button trans_200" v-on:click="isOpen = 4"> Удалить категорию </button>
            <button class="button sig_button trans_200" v-on:click="isOpen = 6"> Отредактировать категорию </button>
            <button class="button sig_button trans_200" v-on:click="isOpen = 3" > Удалить блюдо </button>
            <button class="button sig_button trans_200" v-on:click="isOpen = 5" > Отредактировать блюдо </button>
        </div>
      </div>
      <div v-if="isOpen === 1">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Добавление позиции в меню </h1>
              <form @submit.prevent="CreateProduct">
                <div class="field">
                  <label>Категория</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="prod.category" >
                          <option v-for="sl in category" v-bind:value="sl.id" >{{ sl.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <label>Название блюда</label>
                  <div class="control">
                    <input type="text" placeholder="Название блюда" class="input" v-model="prod.name">
                  </div>
                </div>
                <div class="field">
                  <label>Описание</label>
                  <div class="control">
                    <input type="text" placeholder="Описание" class="input" v-model="prod.description">
                  </div>
                </div>
                <div class="field">
                  <label>Стоимость</label>
                  <div class="control">
                    <input type="number" placeholder="Стоимость" class="input" v-model="prod.price">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark"> Добавить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>

        <div v-if="isOpen === 2">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Добавление категории </h1>
              <form @submit.prevent="CreateCategory">
                <div class="field">
                  <div class="control">
                    <input type="text" placeholder="Название категории" class="input" v-model="cat.name">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <input type="file" placeholder="Загрузите фото категории" id="file" ref="file" v-on:change="UploadFile()">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark"> Добавить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
        <div v-if="isOpen === 3">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Удаление позиции </h1>
              <form>
                <div class="field">
                  <label>Позиция</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="idparam" >
                          <option v-for="prod in products" v-bind:value="prod.id" >{{ prod.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark" @click="DeleteProduct(idparam)"> Удалить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
        <div v-if="isOpen === 4">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Удаление категории </h1>
              <form>
                <div class="field">
                  <label>Категория</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="idparam" >
                          <option v-for="sl in category"  v-bind:value="sl.id" >{{ sl.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark" @click="DeleteCategory(idparam)"> Удалить </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
        <div v-if="isOpen === 5">
          <div class="column is-4 is-offset-4">
              <h1 class="title"> Редактирование позиции </h1>
              <form>
                <div class="field">
                  <label>Выберите продукт</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="idparam" >
                          <option v-for="prod in products" v-bind:value="prod.id" >{{ prod.name }}</option>
                      </select>
                    </div>
                  </div>
                  <label>Категория</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="prod.category" >
                          <option  v-for="sl in category" v-bind:value="sl.id" >{{ sl.name }}</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <input type="text" class="input" placeholder="Название блюда" v-model="prod.name">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <input type="text" class="input" placeholder="Описание" v-model="prod.description">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <input type="number" class="input" placeholder="Стоимость" v-model="prod.price">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <button class="button is-dark" @click="UpdateProduct(idparam)"> Отредактировать </button>
                  </div>
                </div>
              </form>
          </div>
        </div>
        <div v-if="isOpen === 6">
            <div class="column is-4 is-offset-4">
                <h1 class="title"> Обновление категории </h1>
                <form>
                  <label>Категория</label>
                  <div class="control">
                    <div class=" select is-rounded">
                      <select v-model="cat.id" >
                          <option  v-for="sl in category" v-bind:value="sl.id" >{{ sl.name }}</option>
                      </select>
                    </div>
                  </div>
                  <label>Название категории</label>
                  <div class="field">
                    <div class="control">
                      <input type="text" class="input" v-model="cat.name">
                    </div>
                  </div>
                  <div class="field">
                    <div class="control">
                      <input type="file" placeholder="Загрузите фото категории" id="file" ref="file" v-on:change="UploadFile()">
                    </div>
                  </div>
                  <div class="field">
                    <div class="control">
                      <button class="button is-dark" @click="UpdateCategory(cat.id)"> Обновить </button>
                    </div>
                  </div>
                </form>
            </div>
          </div>
    </div>
    <div v-if="isOpenAdmin === 3">
      <div class="column is-12">
        <h1 class="title column">Забронированные столики</h1>
      </div>
      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="bookings.length!==0">
          <thead>
            <tr>
              <th>Клиент</th>
              <th>Дата</th>
              <th>Время</th>
              <th>Количество персон</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
             <tr v-for="books in bookings">
              <td> <h1> {{ books.client.username }} </h1> </td>
              <td>{{ books.date }} </td>
              <td>{{ books.time }}</td>
              <td>{{ books.persons }}  </td>
              <td><button class="delete" @click="DeleteBooking(books.id)"></button></td>
            </tr>
          </tbody>
        </table>
        <p v-else> Все столы свободны </p>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {toast} from "bulma-toast";
export default {
  name: "AdminOrders",
  components: {Navbar},
  data(){
    return {
      orders: [],
      isOpenAdmin: 0,
      category: null,
      products: null,
      isOpen: 0,
      prod: {
        category: '',
        name: '',
        description: '',
        price: '',
      },
      cat: {
        id: '',
        name: ''
      },
      idparam: '',
      bookings: '',
      file: '',
    }
  },
  mounted() {
    this.getProduct()
    this.GetOrders()
    document.title = "Страница администратора | ЭMurr"
    axios
          .get('http://localhost:8000/api/v1/category-list/')
          .then(response=>{
            this.category = response.data
          })
  },
  methods:{
    getProduct(){
      axios
          .get('http://localhost:8000/api/v1/product-list/')
          .then(response=>{
            this.products = response.data
          })
    },
    GetOrders(){
      axios
          .get('http://localhost:8000/api/v1/orders')
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
    CreateProduct(){
       axios.defaults.headers.common["Authorization"] = "Token" + localStorage.getItem("token")
       const formData = {
         category: this.prod.category,
         name: this.prod.name,
         description: this.prod.description,
         price: this.prod.price,
      }
       axios
           .post('http://localhost:8000/api/v1/product-create/', formData)
           .then(response => {
              toast({
                  message: 'Блюдо было добавлено',
                  type: 'is-success',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    UploadFile(){
      this.file = this.$refs.file.files[0]

    },
    CreateCategory(){
       axios.defaults.headers.common["Authorization"] = "Token" + localStorage.getItem("token")
       let  formData = new FormData()
       formData.append('name', this.cat.name)
       formData.append('thumbnail', this.file)
       axios
           .post('http://localhost:8000/api/v1/category-create/',
               formData,
               {
                          headers: {
                                      'Content-Type': 'media/upload'
                                    }
                      })
           .then(response => {
              toast({
                  message: 'Категория была создана',
                  type: 'is-dark',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
           .catch(response => {
              toast({
                  message: 'Упс, что-то не так',
                  type: 'is-danger',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    UpdateCategory(cat_id){
        axios.defaults.headers.common["Authorization"] = "Token" + localStorage.getItem("token")
       let  formData = new FormData()
       formData.append('name', this.cat.name)
       formData.append('thumbnail', this.file)

        axios
            .post('http://localhost:8000/api/v1/category-update/'+ cat_id, formData,
               {
                          headers: {
                                      'Content-Type': 'media/upload'
                                    }
                      })
           .then(response => {
              toast({
                  message: 'Категория была обновлена',
                  type: 'is-dark',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
           .catch(response => {
              toast({
                  message: 'Упс, что-то не так',
                  type: 'is-danger',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    UpdateProduct(prod_id){
        axios.defaults.headers.common["Authorization"] = "Token" + localStorage.getItem("token")
        const formData = {
          category: this.prod.category,
          name: this.prod.name,
          description: this.prod.description,
          price: this.prod.price
        }
        axios
            .post('http://localhost:8000/api/v1/product-update/'+ prod_id, formData)
            .then(responce => {
              toast({
                  message: 'Позиция была обновлена',
                  type: 'is-dark',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
            })
    },
    DeleteCategory(cat_id){
       axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")

       axios
           .delete('http://localhost:8000/api/v1/category-delete/' + cat_id )
           .then(response => {
              toast({
                  message: 'Категория была удалена',
                  type: 'is-dark',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    DeleteProduct(prod_id){
       axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")

       axios
           .delete('http://localhost:8000/api/v1/product-delete/' + prod_id )
           .then(response => {
              toast({
                  message: 'Позиция была удалена',
                  type: 'is-dark',
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: 'bottom-right',
                })
          })
    },
    GetAllBookings(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      axios
          .get('http://localhost:8000/api/v4/get_all_booking/')
          .then(response =>{
            this.bookings = response.data
          })
    },
    DeleteBooking(id){
      axios
          .delete('http://localhost:8000/api/v4/delete_booking/' + id)
          .then(response => {
                  toast({
                      message: 'Заказ удален',
                      type: 'is-dark',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                    })
                  this.bookings = this.bookings.filter(el => el.id !== id)
              })
    },
  },
}
</script>

<style scoped>

</style>