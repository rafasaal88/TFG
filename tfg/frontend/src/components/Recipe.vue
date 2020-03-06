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
        
        

    },

    created(){        
        this.getRecipe();      
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