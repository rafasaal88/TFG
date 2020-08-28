<template>
<div class="">
   
<br>


    <div class="" v-if="token==null">       
        <br>

        <div class="col-lg-12 mx-auto">       
            <div class="card rounded shadow shadow-sm">
                <div class="card-body">
                    <div class="text-center">
                            <h1><font style="color:black;">Debe iniciar sesión para poder acceder a esta sección</font></h1>
                    </div>
                </div>
            </div>
        </div>
    </div>






    <div class="col-lg-12 mx-auto" v-if="token!=null">
        <table class="table" >

            <thead class="thead-dark">
                <tr>
                <th scope="col">Producto</th>
                <th scope="col">Promoción</th>
                <th scope="col">Campaña publicitaria</th>
                <th scope="col">Fecha y hora</th>

                </tr>
            </thead>

            <tbody>

                <tr v-for="item in points" :key="item.id">
                
                    <td v-for="item2 in product" :key="item2.id" v-if="item.product == item2.id">{{item2.name}}</td>                
                
                    <td>{{item.description}}</td>

                    <td v-for="item3 in publicity_campaign" :key="item3.id" v-if="item.publicity_campaign == item3.id">{{item3.name}}</td>
                
                    <td>El {{formatDate(item.date)}} a las {{formatTime(item.time)}}</td>  


                </tr>


            </tbody>

        </table>
    </div>


  


</div>


</template>

<script>


import moment from 'moment'
import axios from 'axios';






export default {
    data(){
        return {
            points: [],
            user: localStorage.getItem('user-name') || null,
            id_user: '',
            product: [],
            publicity_campaign: [],
            token: localStorage.getItem('user-token') || null,
            api_ip: [],
        }

        
    },

    
    methods: {



        formatDate(date){
            if (date) {
                return moment(String(date)).format('DD/MM/YYYY')
            }
        },

        formatTime(time){
            if (time) {
                time = moment.utc(time, "HH:mm:ss").format("HH:mm:ss");
                return time
            }
        },


        getPoints () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/point/'
            const path2 = 'http://127.0.0.1:8000/api/v1.0/user/'


            axios.get(path).then((response) => {

                axios.get(path2).then((response2) => {
                    var userFound = response2.data.find( item => item.username == this.user );
                    this.id_user = userFound.id;
                    this.points = response.data.filter(item => item.user == this.id_user);

                })
                .catch((error) => {
                    console.log(error)
                })

            })



            .catch((error) => {
                console.log(error)
            })
        },    

        getProduct()
        {
            const path = 'http://localhost:8000/api/v1.0/product_list/'

            axios.get(path).then((response) => {
                this.product = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },

        getPublicity_Campaign () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/publicity_campaign_list/'

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
                activity_name: "Lista de puntos",
                user: this.id_user,
            })
            .catch(err => {
                console.log(err)
            })

        }, 2000);
        },
 
    },
    created(){        

        this.getPoints()
        this.getProduct()
        this.getPublicity_Campaign()
        this.getIp()
        this.getID()
        this.create_register_activity()
       
    }

}
</script>

<style>

</style>