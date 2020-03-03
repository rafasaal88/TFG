<template>
  <div id="app">

    <Header/>


    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
  name: '',
  components: {
    Header
  }
}
</script>

<style>
    .containercut > .crop {
      object-fit: cover;
      object-position: 100% 0;
    
      width: 300px;
      height: 300px;
    }

    .containercut > .crop2 {
      object-fit: cover;
      object-position: 50% 0;
    
      height: 300px;
    }

    a:link
    {
      text-decoration:none;
      color: black;
    }
    a:visited
    {
      text-decoration:none;
      color: black;
    }
</style>
