<template>
  <div class="">
    <br>
    <div class="container">
      <div class="row">        
        <div class="col-lg-10">
          <div class="card shadow mb-3" >

            <div class="card-body d-flex flex-row">      
              <div>            

                <h4 class="card-title font-weight-bold mb-2">{{recipe.name}}</h4>
 
        
              </div>      
            </div>

            <div class="view overlay">
              <img class="card-img-top rounded-0" :src="recipe.image" alt="Card image cap">
            </div>          
            
            <div class="container portfolio">
              <br>   
                <pre>{{recipe.description}}</pre>
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
            recipe: [],
            id_user: '',
            user: localStorage.getItem('user-name') || null,
            api_ip: [],
        }
    },
    methods: {


        getRecipe () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/recipe_list/'+this.id+'/'

            axios.get(path).then((response) => {
                this.recipe = response.data
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
                activity_name: "Receta",
                user: this.id_user,
                recipe_name: this.recipe.name,
            })
            .catch(err => {
                console.log(err)
            })

        }, 1000);
        },

    },

    created(){        
        this.getRecipe();
        this.getIp();
        this.getID();
        this.create_register_activity();      
    },


  

}
</script>

<style>
pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  text-align: justify;
  font-family: Arial, Helvetica, sans-serif;
}
</style>