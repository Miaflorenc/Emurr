<template>
  <navbar></navbar>
  <div class="super_container">
    <div class="home">
      <div class="parallax_background parallax-window" data-parallax="scroll" data-image-src="../assets/images/about.jpg" data-speed="0.8"> <img src="../assets/images/about.jpg"></div>
      <div class="home_container">
        <div class="container">
          <div class="row">
            <div class="col">
              <div class="home_content text-center">
                <div class="home_subtitle page_subtitle">The EMurr is</div>
                <div class="home_title"><h1>О нас</h1></div>
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
						  <div class="intro_title"><h2>Ресторан Французской кухни</h2></div>
						  <div class="intro_text">
							  <p>В интерьере, как и на улочках французских городов, соседствуют очаровательные детали прошлого и настоящего, что создает неповторимый дух места «с историей». Негромко звучащие композиции в исполнении знаменитых шансонье с легкостью прогоняют прочь печали и настраивают на мечтательный лад – как будто вы, перешагнув порог, мгновенно перенеслись в легкомысленный и беззаботный Париж.</p>
						  </div>
            </div>
            <div class="row">
              <div class="col-lg-8">
                <div class="intro_image"><img src="../assets/images/about_intro.jpg" alt="https://unsplash.com/@quanle2819"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="chefs">
      <div class="container">
        <div class="row">
          <div class="col">
            <div class="section_title_container">
              <div class="section_subtitle page_subtitle">Something new</div>
              <div class="section_title"><h1>Познакомьтесь с нашими поварами</h1></div>
            </div>
          </div>
        </div>
        <div class="row chefs_text_row">
          <div class="col-lg-6">
            <div class="chefs_text">
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse cursus faucibus finibus. Ut non justo eleifend, facilisis nibh ut, interdum odio. Suspendisse potenti. Vivamus luctus diam eu neque rutrum, vitae aliquet dolor venenatis. Nulla consequat fringilla.</p>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="chefs_text">
              <p>Sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse cursus faucibus finibus. Ut non justo eleifend, facilisis nibh ut, interdum odio. Suspendisse potenti. Vivamus luctus diam eu neque rutrum, vitae aliquet dolor venenatis. Nulla consequat fringilla.</p>
            </div>
          </div>
        </div>
        <div class="row chefs_row row-eq-height">
          <div class="col-xl-3 col-md-6 chef_col d-flex flex-column align-items-center justify-content-end">
            <div class="chef">
              <div class="chef_image"><img src="../assets/images/chef_1.jpg" alt=""></div>
              <div class="chef_content text-center">
                <div class="chef_name">Хасанова Элина</div>
                <div class="chef_subtitle">Шеф Повар</div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 chef_col d-flex flex-column align-items-center justify-content-end">
            <div class="chef">
              <div class="chef_image"><img src="../assets/images/chef_2.jpg" alt=""></div>
              <div class="chef_content text-center">
                <div class="chef_name">Ахмадиев Азат</div>
                <div class="chef_subtitle">Кондитер</div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 chef_col d-flex flex-column align-items-center justify-content-end">
            <div class="chef">
              <div class="chef_image"><img src="../assets/images/chef_3.jpg" alt=""></div>
              <div class="chef_content text-center">
                <div class="chef_name">Гибатдинов Нияз</div>
                <div class="chef_subtitle">Суши Шеф</div>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 chef_col d-flex flex-column align-items-center justify-content-end">
            <div class="chef">
              <div class="chef_image"><img src="../assets/images/chef_4.jpg" alt=""></div>
              <div class="chef_content text-center">
                <div class="chef_name">Рахматуллина Гузель</div>
                <div class="chef_subtitle">Су-Шеф</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="themenu">
      <div class="container">
        <div class="row">
          <div class="col">
            <div class="section_title_container text-center">
              <div class="section_title"><h1>Отзывы</h1></div>
            </div>
          </div>
        </div>
      <div class="row themenu_row">
        <div class="col-lg-4 themenu_column" v-for="feeds in feedbacks">
            <div class="themenu_col trans_400">
              <div class="themenu_col_title">{{feeds.author.username}}</div>
              <div class="dish_list">
                <div class="dish">
                    <div class="dish_title_container d-flex flex-xl-row flex-column align-items-start justify-content-start" >
                      <div class="dish_title">{{ feeds.text }}</div>
                    </div>
                    <div class="dish_contents">
                      <ul class="d-flex flex-row align-items-start justify-content-start flex-wrap">
                        <li>{{feeds.create_date}}</li>
                      </ul>
                    </div>
                </div>
              </div>
            </div>
        </div>
      </div>
        <div class="column" v-if="isAuthenticated">
          <form @submit.prevent="CreateFeedbacks">
          <input class="textarea" placeholder="Здесь вы можете оставить о нас отзыв" v-model="feedtext">
          <button class="button sig_button trans_200">  Отправить </button>
        </form>
        </div>
      </div>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import {mapGetters} from "vuex";
import {toast} from "bulma-toast";
import Footer from "@/components/Footer";
export default {
  name: "Reviews",
  components: {Footer, Navbar},
  data(){
    return{
      userinfo: '',
      feedbacks: null,
      feedtext: '',
    }
  },
  mounted() {
    axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
    this.GetFeedbacks()
    this.GetUserId()
  },
  methods:{
    GetFeedbacks(){
      axios
          .get('http://localhost:8000/api/v2/feedbacks/')
          .then(response =>{
            this.feedbacks = response.data
            document.title = 'Отзывы | Эmurr'
          })
    },
    GetUserId(){
      axios
          .get('http://127.0.0.1:8000/auth/users/me')
          .then(response =>{
            this.userinfo = response.data
          })
    },
    CreateFeedbacks(){
      axios.defaults.headers.common["Authorization"] = "Token " + localStorage.getItem("token")
      const formData = {
        author: this.userinfo.id,
        text: this.feedtext
      }
      // console.log(formData)
      axios
          .post('http://localhost:8000/api/v2/feeds-create/', formData)
          .then(response => {
                  toast({
                      message: 'Спасибо за ваш отзыв!',
                      type: 'is-dark',
                      dismissible: true,
                      pauseOnHover: true,
                      duration: 2000,
                      position: 'bottom-right',
                    })

                  this.feedbacks.push(response.data)
                  this.feedtext.push('')
              })
    }
  },
  computed: {
    ...mapGetters({
      isAuthenticated: "isAuthenticated",
      username: "username",
    }),
  },
}
</script>

<style scoped>

</style>