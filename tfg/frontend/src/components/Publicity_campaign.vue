<template>
  <div class="">
     <br>

    <div class="container-fluid">
      <div class="row">        
        <div class="col-lg-8 mx-auto">
          <div class="card shadow mb-4" >

            <div class="card-body">      
              <div>      
                <h4 class="card-title font-weight-bold mb-2">{{ product.name}}</h4>
              </div>      
            </div>

            <div class="view overlay">
              <img class="card-img-top rounded-0" :src="product.image" alt="Card image cap">
            </div>              

            <div class="container">
              <br> 
              <div class="row">                   

                <div class="col-lg-4" v-for="(item, index) in product.product" :key="item.id" >
                  
                  <div v-if="item.available">

                    <a v-bind:href="'#'+item.id" >

                      <div class="card" >

                        <div class="card-body">      
                          <div>      
                            <h4 class="card-title font-weight-bold mb-2">{{item.name}}</h4>                          
                          </div>      
                        </div>        

                        <div class="view overlay containercut">
                          <img class="card-img-top rounded-0 crop2" :src="item.image" alt="Card image cap">
                        </div>          
                        
                        <div class="container portfolio text-right" v-if="item.unit == 'unidad'">            
                          <br>
                              <h4>{{item.price}} €/Unidad<br></h4>
                          <br>
                        </div>

                        <div class="container portfolio text-right" v-if="item.unit == 'kg'">            
                          <br>
                              <h4>{{item.price}} €/Kg<br></h4>
                          <br>
                        </div>

                        <div class="container portfolio text-right" v-if="item.unit == 'litros'">            
                          <br>
                              <h4>{{item.price}} €/Litro<br></h4>
                          <br>
                        </div>

                      </div>
                      <br>
                    </a>
                 </div>


                  <div v-else>

                      <div class="card" >

                        <div class="card-body">      
                          <div>      
                            <h4 class="card-title font-weight-bold mb-2">{{item.name}}</h4>                          
                          </div>      
                        </div>        

                        <div class="view overlay containercut">
                          <img class="card-img-top rounded-0 crop2" :src="item.image" alt="Card image cap">
                        </div>      
                                        
                        <div class="container portfolio text-right">            
                          <br>
                              <h5><b>PRODUCTO NO DISPONIBLE</b></h5>
                          <br>
                        </div>                     

                      </div>

                      <br>

                  </div>

               </div>

              </div>

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
            fields: [
                { key: 'name', label: 'Nombre'},
                { key: 'date_start', label: 'Fecha de inicio'}, 
                { key: 'date_end', label: 'Fecha de finalización'},
                { key: 'description', label: 'Descripción'}, 
                { key: 'user', label: 'Usuario'},                 
                { key: 'image', label: 'Imagen'}, 
                { key: 'product', label: 'Producto'},
                { key: 'action', label: ''}, 
            ],
            product: [],
        }
    },
    
    methods: {
        getPublicity_Campaign () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/publicity_campaign_list/'+this.id+'/'

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