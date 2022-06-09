<template>
  <div>
    <h1>Hello Worlds</h1>
    <h2>Count {{ counter }} </h2>
    <input type="text">
    <input type="password">
    <input type="checkbox">
    <br>
    <button @click="myBtn">Increase Count</button>
  </div>
</template>

<script>

export default {
  name: "App",
  data: function(){
    return { 
      counter: 0
      }
  },
  methods: {
    myBtn() {
      this.counter ++ 
      console.log(window.pywebview.api.showCount(this.counter));
      
    }
  }
}
</script>

<style scoped>

</style>