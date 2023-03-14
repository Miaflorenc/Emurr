import { createStore } from 'vuex'

function updateLocalStorage(cart){
  localStorage.setItem('cart', JSON.stringify(cart))
}
export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    username:'',
    cart: [],
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    token: (state) => state.token,
    username: (state) => state.username,
    cartItems: (state) => {
      return state.cart
    },
    cartTotal: (state) => {
      return state.cart.reduce((a, b) => a + (b.price * b.quantity), 0)
    }
  },
  mutations: {
    initializeStore(state){
      if (localStorage.getItem("token")){
        state.token = localStorage.getItem("token")
        state.isAuthenticated = true
        state.username = localStorage.getItem("username")
      } else {
        state.token = ""
        state.isAuthenticated = false
        state.username = ""
      }
    },
    setToken(state, token){
      state.token = token
      localStorage.setItem("token", token)
      state.isAuthenticated = true
    },
    removeToken(state){
      state.token = ""
      localStorage.removeItem("token")
      localStorage.removeItem("username")
      state.isAuthenticated = false
      localStorage.removeItem("cart")
      state.cart.length = 0
    },
    addToCart(state, product){
      let item = state.cart.find( i => i.id === product.id)

      if(item){
        item.quantity++
      } else state.cart.push({...product, quantity: 1})
      updateLocalStorage(state.cart)
    },
    removeFromCart(state, product){
      let item = state.cart.find( i => i.id === product.id)
      if(item){
        if (item.quantity > 1){
            item.quantity--
        } else {
          state.cart =  state.cart.filter(i => i.id !== product.id)
        }
      }
      updateLocalStorage(state.cart)
    },
    removeFromCartProduct(state, product){
      let item = state.cart.find( i => i.id === product.id)
      if(item){
          state.cart =  state.cart.filter(i => i.id !== product.id)
      }
      updateLocalStorage(state.cart)
    },
    updateCartFromLocalStorage(state){
      const cart = localStorage.getItem('cart')
      if(cart)
        state.cart = JSON.parse(cart)
    }
  },

  actions: {
  },
  modules: {
  }
})
