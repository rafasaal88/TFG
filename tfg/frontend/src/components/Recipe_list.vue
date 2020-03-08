<template>
<div class="">
    
    <br>

        <div class="col-lg-12 mx-auto">       
            <div class="card rounded">
                <div class="card-body">
                    <div class="text-left" >          

                        <div v-if="recipe.length">
                            <center><h2>Recetas disponibles</h2></center>
                        </div>

                        <div v-else>
                            <center><h2>No hay recetas disponibles</h2></center>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    <br>

<div class="container-fluid">
  <div class="row">        
    <div class="col-lg-3" v-for="item in recipe" :key="item.id">
       
        <a :href="'/recipe/'+item.id">
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
            recipe: [],
        }
    },
    methods: {
        getRecipe () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/recipe_list/'

            axios.get(path).then((response) => {
                this.recipe = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    created(){        

        this.getRecipe()
    }

}
</script>

<style>

</style>