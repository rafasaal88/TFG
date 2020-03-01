<template>
  <div class="">
      
  <br>
  <!--Desktop version-->
    <div class="d-none d-sm-none d-md-block" >
        <div class="col-lg-12 mx-auto">       
            <div class="card rounded shadow shadow-sm">
                <div class="card-body">
                    <div class="text-left" >          

                        <div v-if="product.length">
                            <center><h2>Bienvenido, estas son las campañas publicitarias que tenemos activas en este momento.</h2></center>
                        </div>

                        <div v-else>
                            <center><h2>Bienvenido, no hay ninguna campañas publicitaria activas en este momento.</h2></center>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>

<!--Mobile version-->
    <div class="d-block d-sm-block d-md-none" >
        <div class="col-lg-12 mx-auto">       
            <div class="card rounded shadow shadow-sm">
                <div class="card-body">
                    <div class="text-left">
                        
                        <div v-if="product.length">
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
    <div class="col-lg-6" v-for="(item, index) in product" :key="item.id">

      <div class="card shadow mb-3" >

        <div class="card-body d-flex flex-row">      
          <div>      
            <h4 class="card-title font-weight-bold mb-2">{{ item.name }}</h4>
          </div>      
        </div>

        <div class="view overlay">
          <img class="card-img-top rounded-0" :src="item.image" alt="Card image cap">
          <a href="#!">
            <div class="mask rgba-white-slight"></div>
          </a>
        </div>          
        
        <div class="container portfolio">
          <br>
            <p>{{item.description}}</p>
        </div>
            
        <div class="container portfolio">
          <br>
            <p>{{item.product}}</p>
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
            fields: [
                { key: 'name', label: 'Nombre'},
                { key: 'date_start', label: 'Fecha de inicio'}, 
                { key: 'date_end', label: 'Fecha de finalización'},
                { key: 'description', label: 'Descripción'}, 
                { key: 'user', label: 'Usuario'},                 
                { key: 'image', label: 'Imagen'}, 
                { key: 'product', label: 'Producto'},
                { key: 'action', label: ''}, 
            ],
            product: [],
        }
    },
    methods: {
        getPublicity_Campaign () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/publicity_campaign_list/'

            axios.get(path).then((response) => {
                this.product = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    created(){        

        this.getPublicity_Campaign()
    }

}
</script>

<style>

</style>