<template>
    <tr>
      <td> <h1> {{ product.name }} </h1> </td>
      <td>{{ product.price }} руб</td>
      <td>
        {{ product.quantity }}
        <a @click="decrementQuantity(product)">-</a>
        <a @click="incrementQuantity(product)">+</a>
      </td>
      <td>{{ item_cost.toFixed(2  ) }} руб </td>
      <td><button class="delete" @click="removeFromCart(product)"></button></td>
    </tr>
</template>

<script>
export default {
  name: "CartItem",
  props: ['product'],
  computed:{
    item_cost(){
      return this.product.price * this.product.quantity
    }
  },
  methods:{
    decrementQuantity(item){
      item.quantity -=1

      if(item.quantity === 0){
        this.$store.commit('removeFromCart', this.product)
      }
      this.updateCart()
    },
    incrementQuantity(item){
      item.quantity +=1
      this.updateCart()
    },
    updateCart(){
      localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
    },
    removeFromCart(){
      this.$store.commit('removeFromCartProduct', this.product)
      this.updateCart()
    },
  }
}
</script>

<style scoped>

</style>