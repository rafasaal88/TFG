<template>
<div class="">
    
    <br>

        <div class="col-lg-12 mx-auto">       
            <div class="card rounded">
                <div class="card-body">
                    <div class="text-left" >          

                        <div v-if="product.length">
                            <center><h2>Productos disponibles</h2></center>
                        </div>

                        <div v-else>
                            <center><h2>No hay productos disponibles</h2></center>
                        </div>

                    </div>
                </div>
            </div>
        </div>

<br>

<div class="container-fluid">
  <div class="row">        
    <div class="col-lg-3" v-for="item in product" :key="item.id" v-if="item.available==true">
       
        <a :href="'/product/'+item.id">
            <div class="card" >

                <div class="card-body d-flex flex-row">      
                <div>      
                    <h4 class="card-title font-weight-bold mb-2">{{ item.name }}</h4>
                </div>      
                </div>

                <div class="view overlay containercut">
                    <img class="card-img-top rounded-0 crop2" :src="item.image" alt="Card image cap">
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

export default {
    data(){
        return {
            product: [],
            id_user: '',
            user: localStorage.getItem('user-name') || null,
            api_ip: [],
        }
    },
    methods: {
        getProducts () 
        {
            const path = 'http://localhost:8000/api/v1.0/product_list/'

            axios.get(path).then((response) => {
                this.product = response.data
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
                activity_name: "Lista de productos",
                user: this.id_user,
            })
            .catch(err => {
                console.log(err)
            })

        }, 1000);
        },
    },
    
    created(){        

        this.getProducts()
        this.getIp()
        this.getID()
        this.create_register_activity()
    }

}
</script>

<style>

</style>