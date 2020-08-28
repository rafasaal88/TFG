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
            id_user: '',
            user: localStorage.getItem('user-name') || null,
            api_ip: [],
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
                activity_name: "Lista de campañas",
                user: this.id_user,
            })
            .catch(err => {
                console.log(err)
            })

        }, 1000);
        },
    },

    created(){        

        this.getPublicity_Campaign()
        this.getIp()
        this.getID()
        this.create_register_activity()
    }

}
</script>

<style>

</style>