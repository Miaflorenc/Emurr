<template>
  <div class="super_container">
    <navbar></navbar>
	<div class="home">
		<div class="parallax_background parallax-window" data-parallax="scroll" data-speed="0.8"><img src="../assets/images/home.jpg"></div>
		<div class="home_container">
			<div class="container">
				<div class="row">
					<div class="col">
						<div class="home_content text-center">
							<div class="home_subtitle page_subtitle">The EMurr is</div>
							<div class="home_title"><h1>Ресторан Французской кухни</h1></div>
							<div class="home_text ml-auto mr-auto">
								<p>Настоящий кусочек Франции в Казани!</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="intro">
		<div class="container">
			<div class="row">
				<div class="col">
					<div class="intro_content">
						<div class="intro_subtitle page_subtitle">Пару слов о нас</div>
						<div class="intro_title"><h2>Ресторан Французской кухни</h2></div>
						<div class="intro_text">
							<p>В интерьере, как и на улочках французских городов, соседствуют очаровательные детали прошлого и настоящего, что создает неповторимый дух места «с историей». Негромко звучащие композиции в исполнении знаменитых шансонье с легкостью прогоняют прочь печали и настраивают на мечтательный лад – как будто вы, перешагнув порог, мгновенно перенеслись в легкомысленный и беззаботный Париж.</p>
						</div>
					</div>
					<div class="row">
						<div class="col-xl-4 col-md-6 intro_col">
							<div class="intro_image"><img src="../assets/images/intro_1.jpg"></div>
						</div>
						<div class="col-xl-4 col-md-6 intro_col">
							<div class="intro_image"><img src="../assets/images/intro_2.jpg"></div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="reservations text-center">
		<div class="parallax_background parallax-window" data-parallax="scroll" data-image-src="../assets/images/reservations.jpg" data-speed="0.8"><img style="height: 700px" src="../assets/images/reservations.jpg"></div>
		<div class="container">
			<div class="row">
				<div class="col">
					<div class="reservations_content d-flex flex-column align-items-center justify-content-center">
						<div class="res_stars page_subtitle">5 Stars</div>
						<div class="res_title">Забронируйте столик</div>
						<div class="res_form_container">
							<form id="res_form" class="res_form" @submit.prevent="BookingTable">
                <div class="home_text">
									На какое число хотите забронировать столик?
								</div>
								<div class="d-flex flex-sm-row flex-column align-items-center justify-content-start">
									<input type="text" class="res_input" placeholder="2022-12-31" v-model="date">
								</div>
                <div class="home_text">
									Введите время:
								</div>
								<div class="d-flex flex-sm-row flex-column align-items-center justify-content-start">
									<input type="text" class="res_input" placeholder="12:00" v-model="time">
								</div>
                <div class="home_text">
									Количество персон:
								</div>
								<div class="d-flex flex-sm-row flex-column align-items-center justify-content-start">
									<input type="text" class="res_input" placeholder="2" v-model="persons">
								</div>
                <div class="d-flex flex-sm-row flex-column align-items-center justify-content-start">
									<button class="align-items-center res_button">Забронировать</button>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
    <Footer></Footer>
  </div>
</template>
<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import Footer from "@/components/Footer";
import {toast} from "bulma-toast";
export default {
  name: "Main",
  components: {Footer, Navbar},
  data(){
    return{
      Products: [],
      userinfo: '',
      client: '',
      date: '',
      time: '',
      persons: '',
    }
  },
  mounted() {
    axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
    this.GetUserId()
    axios
        .get("http://localhost:8000/api/v1/product-list/")
        .then(response=>{
          this.Products = response.data
          document.title = 'Эmurr'
        })
  },
  methods:{
    GetUserId(){
      axios
          .get('http://127.0.0.1:8000/auth/users/me')
          .then(response =>{
            this.userinfo = response.data
          })
    },
    BookingTable(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      console.log(axios.defaults.headers.common["Authorization"])
      const formData = {
        client: this.userinfo.id,
        date: this.date,
        time: this.time,
        persons: this.persons
      }
      axios
          .post('http://127.0.0.1:8000/api/v4/create_booking/', formData)
          .then(response => {
                  toast({
                      message: 'Стол успешно забронирован! Спасибо, что вы с нами',
                      type: 'is-dark',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                    })
              })
          .catch(response => {
                  toast({
                      message: 'Войдите в аккаунт, чтобы забронировать столик',
                      type: 'is-danger',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 5000,
                      position: 'bottom-right',
                    })
              })
    },
  },
}
</script>
<style scoped>
@import "../assets/styles/bootstrap-4.1.2/bootstrap.min.css";
@import "../assets/styles/elements_responsive.css";
@import "../assets/styles/elements.css";
@import "../assets/styles/main_styles.css";
@import "../assets/styles/responsive.css";
</style>