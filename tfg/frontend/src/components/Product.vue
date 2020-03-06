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
              <h4 class="card-title font-weight-bold mb-2" v-if="!check" >No hay recetas disponibles para este producto</h4>


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

    <div class="container" v-if="!available">
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
        }
        
        

    },

    created(){        

        this.getPublicity_Campaign();
        this.getRecipe();      
    },


  

}
</script>

<style>

</style>