<template>
  <div class="">


    <br>
    <div class="container" v-if="product.available">
      <div class="row">        
        <div class="col-lg-10">
          <div class="card shadow mb-3" >

            <div class="card-body d-flex flex-row">      
              <div>            

                <h4 class="card-title font-weight-bold mb-2" v-if="product.unit == 'kg'">{{product.name}}: {{product.price}} €/Kg</h4>

                <h4 class="card-title font-weight-bold mb-2" v-if="product.unit == 'litros'">{{product.name}}: {{product.price}} €/Litro</h4>

                <h4 class="card-title font-weight-bold mb-2" v-if="product.unit == 'unidad'">{{product.name}}: {{product.price}} €/Unidad</h4>             

              </div>      
            </div>

            <div class="view overlay">
              <img class="card-img-top rounded-0" :src="product.image" alt="Card image cap">
            </div>          
            
            <div class="container portfolio">
              <br>   
                <p>{{product.description}}</p>
            </div>

            <div class="container portfolio">
          
          
              <h4 class="card-title font-weight-bold mb-2" v-if="check" >Recetas disponibles:</h4>  


                <div v-for="item in recipe" :key="item.id">
                  <div v-for="item_product in item.product" :key="item_product.id" >
                    <ul>
                      <span v-if="product.id == item_product"> 
                        <li><a :href="'/Recipe/'+item.id">{{item.name}}</a></li>          
                        {{changevalue()}}
                      </span>  
                    </ul>
                  </div>
                </div>

            </div>

          </div>
        </div>
      </div>
    </div>

    <div class="container" v-else>
          <div class="row">        
            <div class="col-lg-10">
              <div class="card shadow mb-3" >

                <div class="card-body d-flex flex-row">      
                  <div>            
                    <h4 class="card-title font-weight-bold mb-2">El producto al que intenta acceder no se encuentra disponible en este momento</h4>         
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
            product: [],
            recipe: [],
            check: false,
            available: true,
            id_user: '',
            user: localStorage.getItem('user-name') || null,
            api_ip: [],
        }
    },
    methods: {
        getProduct_List () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/product_list/'+this.id+'/'

            axios.get(path).then((response) => {
                this.product = response.data
            })
            .catch((error) => {
                this.available = false;
                console.log(error)
            })
        },

        getRecipe () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/recipe_list/'

            axios.get(path).then((response) => {
                this.recipe = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            
        },

        changevalue(){
          this.check = true;
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
                activity_name: "Producto",
                user: this.id_user,
                product_name: this.product.name,
                product_price: this.product.price,

            })
            .catch(err => {
                console.log(err)
            })

        }, 2000);
        },
        
        

    },

    created(){        

        this.getProduct_List();
        this.getRecipe();   
        this.getIp()
        this.getID()
        this.create_register_activity()   
    },


  

}
</script>

<style>

</style>