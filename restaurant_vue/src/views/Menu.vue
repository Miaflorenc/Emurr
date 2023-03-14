<template>
<navbar></navbar>
  <div class="super_container">
    <div class="home">
      <div class="parallax_background parallax-window" data-parallax="scroll" data-image-src="images/menu.jpg" data-speed="0.8"><img src="../assets/images/menu.jpg"></div>
      <div class="home_container">
        <div class="container">
          <div class="row">
            <div class="col">
              <div class="home_content text-center">
                <div class="home_subtitle page_subtitle">The EMurr</div>
                <div class="home_title"><h1>Меню</h1></div>
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
              <div class="section_title"><h1>Познакомьтесь с нашим меню</h1></div>
            </div>
          </div>
        </div>
        <div class="row themenu_text_row">
          <div class="col-lg-6">
            <div class="themenu_text">
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse cursus faucibus finibus. Ut non justo eleifend, facilisis nibh ut, interdum odio. Suspendisse potenti. Vivamus luctus diam eu neque rutrum, vitae aliquet dolor venenatis. Nulla consequat fringilla.</p>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="themenu_text">
              <p>Sit amet, consectetur adipiscing elit. Donec malesuada lorem maximus mauris scelerisque, at rutrum nulla dictum. Ut ac ligula sapien. Suspendisse cursus faucibus finibus. Ut non justo eleifend, facilisis nibh ut, interdum odio. Suspendisse potenti. Vivamus luctus diam eu neque rutrum, vitae aliquet dolor venenatis. Nulla consequat fringilla.</p>
            </div>
          </div>
        </div>
        			<div class="row">
				<div class="col">
					<div class="themenu_title_bar_container">
						<div class="themenu_stars text-center page_subtitle">5 Stars</div>
						<div class="themenu_rating text-center">
							<div class="rating_r rating_r_5"><i></i><i></i><i></i><i></i><i></i></div>
						</div>
						<div class="themenu_title_bar d-flex flex-column align-items-center justify-content-center">
							<div class="themenu_title">Меню</div>
						</div>
					</div>
				</div>
			</div>
        <div class="row themenu_row">
          <div class="col-lg-4 themenu_column" v-for="cat in category">
            <div class="themenu_image"><img :src="cat.get_thumbnail"></div>
            <div class="themenu_col trans_400">
              <div class="themenu_col_title">{{cat.name}}</div>
              <div class="dish_list">
                <div class="dish" v-for="prod in products">
                  <div v-if="prod.category===cat.id">
                    <div class="dish_title_container d-flex flex-xl-row flex-column align-items-start justify-content-start" >
                      <div class="dish_title">{{ prod.name }}</div>
                      <div class="dish_price">{{prod.price}}</div>
                    </div>
                    <div class="dish_contents">
                      <ul class="d-flex flex-row align-items-start justify-content-start flex-wrap">
                        <li>{{prod.description}}</li>
                      </ul>
                    </div>
                    <div class="dish_order"><a @click="addToCart(prod)"> В корзину </a></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
import { toast } from "bulma-toast";
import {mapGetters} from "vuex";
import Footer from "@/components/Footer";
export default {
  name: "Menu",
  components: {Footer, Navbar},
  data(){
    return{
      category: null,
      products: null,
      quantity: 1,
    }
  },
   mounted() {
     this.$store.commit("updateCartFromLocalStorage")
     this.getProduct()
     axios
          .get('http://localhost:8000/api/v1/category-list/')
          .then(response=>{
            this.category = response.data
            document.title ='Меню | Эmurr'
          })

  },
  methods: {
     getProduct(){
      axios
          .get('http://localhost:8000/api/v1/product-list/')
          .then(response=>{
            this.products = response.data
          })
    },

    addToCart(prod) {
      this.$store.commit('addToCart', prod)

      toast({
        message: 'Позиция была добавлена в корзину',
        type: 'is-dark',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
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