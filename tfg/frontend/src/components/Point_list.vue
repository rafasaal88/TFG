<template>
<div class="">
   
<br>

<div class="col-lg-12 mx-auto">
<table class="table" >
  <thead class="thead-dark">
    <tr>
      <th scope="col">Producto</th>
      <th scope="col">Descripción</th>
      <th scope="col">Campaña publicitaria</th>
    </tr>
  </thead>
  <tbody>


    <tr v-for="item in points" :key="item.id">
      <td>{{item.product}}</td>
      <td>{{item.description}}</td>
      <td>{{item.publicity_campaign}}</td>
    </tr>


  </tbody>
</table>
</div>



















</div>


</template>

<script>

import axios from 'axios';

export default {
    data(){
        return {
            points: [],
            user: localStorage.getItem('user-name') || null,
            id_user: '',
        }
    },
    methods: {
        getPoints () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/point/'
            const path2 = 'http://127.0.0.1:8000/api/v1.0/user/'


            axios.get(path).then((response) => {

                axios.get(path2).then((response2) => {
                var userFound = response2.data.find( item => item.username == this.user );
                this.id_user = userFound.id;
                                this.points = response.data.filter(item => item.user == this.id_user)

                })
                .catch((error) => {
                    console.log(error)
                })

            })



            .catch((error) => {
                console.log(error)
            })
        },    
 
    },
    created(){        

        this.getPoints()
       
    }

}
</script>

<style>

</style>