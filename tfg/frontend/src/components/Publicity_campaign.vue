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
            
            <div class="card-body">      
              <div>      
                <h4 class="card-title mb-2">{{ publicity_campaign.description}}</h4>
              </div>      
            </div>            
         
          </div>
        </div>
      </div>
    </div>   

    <br>

    <div class="container-fluid">
      <div class="row">        
        <div class="col-lg-8 mx-auto">
          <div class="card" >

            <div class="card-body">      
              <div>      
                <center><h2>¡¡Busca los siguientes productos en la tienda, toca la etiqueta NFC y consigue descuentos!!</h2></center>
              </div>      
            </div>     

          </div>
        </div>
      </div>
    </div>   


    <br>






    <div class="container-fluid">
      <div class="row">        
        <div class="col-lg-8 mx-auto">
          <div class="card" >



            <div class="container-fluid">
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
            id_user: '',
            user: localStorage.getItem('user-name') || null,
            api_ip: [],
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
        },
        getID()
        {
           const path = 'http://127.0.0.1:8000/api/v1.0/user/'

            axios.get(path).then((response) => {
                var userFound = response.data.find( item => item.username == this.user );
                this.id_user = userFound.id;


            })
            .catch((error) => {
                console.log(error)
            })
           
        },
        
        getIp(){
            const path = 'https://freegeoip.app/json/'


            axios.get(path).then((response) => {
                this.api_ip = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },

        create_register_activity() {
        setTimeout(() => {
                axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                ip_address: this.api_ip.ip,
                country_name: this.api_ip.country_name,
                region_name: this.api_ip.region_name,
                city: this.api_ip.city,
                activity: "Visita sección",
                activity_name: "Campaña de publicidad",
                user: this.id_user,
                publicity_campaign_name: this.publicity_campaign.name,
                publicity_campaign_date_start: this.publicity_campaign.date_start,
                publicity_campaign_date_end: this.publicity_campaign.date_end,
                publicity_campaign_description: this.publicity_campaign.description,


    

            })
            .catch(err => {
                console.log(err)
            })

        }, 2000);
        },
        
    },

    created(){        
        this.getIp()
        this.getID()
        this.create_register_activity()  
        this.getPublicity_Campaign()
    }

}
</script>

<style>
 
</style>