<template>
  <div class="">
      
  <br>
  <!--Desktop version-->
    <div class="d-none d-sm-none d-md-block" >
        <div class="col-lg-12 mx-auto">       
            <div class="card rounded">
                <div class="card-body">
                    <div class="text-left" >          

                        <div v-if="publicity_campaign.length">
                            <center><h2>Campañas publicitarias que tenemos activas en este momento.</h2></center>
                        </div>

                        <div v-else>
                            <center><h2>No hay ninguna campañas publicitaria activas en este momento.</h2></center>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>

<!--Mobile version-->
    <div class="d-block d-sm-block d-md-none" >
        <div class="col-lg-12 mx-auto">       
            <div class="card rounded">
                <div class="card-body">
                    <div class="text-left">
                        
                        <div v-if="publicity_campaign.length">
                            <center><h5>Campañas publicitarias activas</h5></center>
                        </div>
                        
                        <div v-else>
                            <center><h5>No hay campañas publicitarias activas</h5></center>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>

    <br>

<div class="container-fluid">
  <div class="row">        
    <div class="col-lg-6" v-for="(item, index) in publicity_campaign" :key="item.id">
       
        <a v-bind:href="'Publicity_campaign/'+item.id" style="color:black">
            <div class="card" >

                <div class="card-body d-flex flex-row">      
                <div>      
                    <h4 class="card-title font-weight-bold mb-2">{{ item.name }}</h4>
                </div>      
                </div>

                <div class="view overlay containercut">
                    <img class="card-img-top rounded-0" :src="item.image" alt="Card image cap">
                    <a href="#!">
                        <div class="mask rgba-white-slight"></div>
                    </a>
                </div>          
                
                <div class="container portfolio">
                <br>
                    <p>{{item.description}}</p>
                </div>
                    
            
            </div>
        
        </a>

      <br>
    </div>
  </div>
</div>


          
      
  </div>
</template>

<script>

import axios from 'axios';
import moment from 'moment';

export default {
    data(){
        return {
            publicity_campaign: [],
        }
    },
    methods: {
        getPublicity_Campaign () 
        {

            var date = new Date();
            date = moment(date, 'YYYY-MM-DD').format('YYYY-MM-DD');

            const path = 'http://127.0.0.1:8000/api/v1.0/publicity_campaign_list/'

            axios.get(path).then((response) => {
                this.publicity_campaign = response.data.filter(item => item.date_end >= date)
            })
            .catch((error) => {
                console.log(error)
            })
        },
    },

    created(){        

        this.getPublicity_Campaign()
    }

}
</script>

<style>

</style>