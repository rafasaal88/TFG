<template>
  <div class="">
     <br>

    <div class="container-fluid">
      <div class="row">        
        <div class="col-lg-8 mx-auto">
          <div class="card" >

            <div class="card-body">      
              <div>      
                <h4 class="card-title font-weight-bold mb-2">{{ publicity_campaign.name}}</h4>
              </div>      
            </div>

            <div class="view overlay">
              <img class="card-img-top rounded-0" :src="publicity_campaign.image" alt="Card image cap">
            </div>              
            
            

            <div class="d-none d-sm-none d-md-block" >
                  <div class="col-lg-12 mx-auto">
                     <br>

                      <div class="card rounded">
                        
                          <div class="card-body">
                              <div class="text-left" >          
                                
                                  <div>
                                      <center><h2>¡¡Busca los siguientes productos en la tienda, toca la etiqueta NFC y consigue descuentos!!</h2></center>
                                  </div>
                                  
                              </div>
                          </div>
                      </div>
                  </div>
              </div>











            <div class="container">
              <br> 
              <div class="row">                   

                <div class="col-lg-4" v-for="(item, index) in publicity_campaign.product" :key="item.id" >
                  
                  <div v-if="item.available">

                    <a :href="'/Product/'+item.id" >

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
            publicity_campaign: [],
        }
    },
    
    methods: {
        getPublicity_Campaign () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/publicity_campaign_list/'+this.id+'/'

            axios.get(path).then((response) => {
                this.publicity_campaign = response.data
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