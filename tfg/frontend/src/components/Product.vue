<template>
  <div class="">

<br>
<div class="container">
  <div class="row">        
    <div class="col-lg-10">
      <div class="card shadow mb-3" >

        <div class="card-body d-flex flex-row">      
          <div>      
      

            <h4 class="card-title font-weight-bold mb-2">{{product.name}}</h4>

            <h5 class="card-title font-weight-bold mb-2" v-if="product.unit == 'kg'">Precio: {{product.price}} €/Kg</h5>

            <h5 class="card-title font-weight-bold mb-2" v-if="product.unit == 'litros'">Precio: {{product.price}} €/Litro</h5>

            <h5 class="card-title font-weight-bold mb-2" v-if="product.unit == 'unidad'">Precio: {{product.price}} €/Unidad</h5>

              

                     
          </div>      
        </div>

        <div class="view overlay">
          <img class="card-img-top rounded-0" :src="product.image" alt="Card image cap">
        </div>          
        
        <div class="container portfolio">
          <br>
          <h4 class="card-title font-weight-bold mb-2">Descripción:</h4>           
            <p>{{product.description}}</p>
        </div>

      </div>
    </div>
  </div>
</div>













      
  </div>
</template>

<script>

import axios from 'axios';

export default {
    data(){
        return {
            id: this.$route.params.id,
            product: [],
        }
    },
    methods: {
        getPublicity_Campaign () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/product_list/'+this.id+'/'

            axios.get(path).then((response) => {
                this.product = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    created(){        

        this.getPublicity_Campaign()
    }

}
</script>

<style>

</style>