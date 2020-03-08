<template>
<div class="">
    
    <br>

        <div class="col-lg-12 mx-auto">       
            <div class="card rounded">
                <div class="card-body">
                    <div class="text-left" >          

                        <div>
                            <center><h2>Estos son los productos de los que disponemos actualmente</h2></center>
                        </div>

                    </div>
                </div>
            </div>
        </div>

<br>

<div class="container-fluid">
  <div class="row">        
    <div class="col-lg-3" v-for="(item, index) in product" :key="item.id">
       
        <a :href="'/product/'+item.id" >
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
            fields: [
                { key: 'name', label: 'Nombre'},
                { key: 'price', label: 'Precio'}, 
                { key: 'description', label: 'Descripcion'},
                { key: 'date', label: 'Fecha'}, 
                { key: 'available', label: 'Disponible'}, 
                { key: 'user', label: 'Usuario'},                 
                { key: 'price', label: 'Precio'}, 
                { key: 'image', label: 'Imagen'}, 
                { key: 'action', label: ''}, 
            ],
            product: []
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
        }
    },

    created(){        

        this.getProducts()
    }

}
</script>

<style>

</style>