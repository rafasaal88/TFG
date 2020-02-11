<template>
  <div class="container">
      <div class="row">
        <div class = "col-lg-12">
          <div class="col text-left">
            <div class="card shadow mb-3" >
                <div>
                <h2>Listado de productos</h2>
                </div>
                    <div class="card-body d-flex flex-row">      

                  <b-table striped hover :items="product" :fields="fields">

                  </b-table>
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
                { key: 'price', label: 'Precio'}, 
                { key: 'description', label: 'Descripcion'},
                { key: 'date', label: 'Fecha'}, 
                { key: 'available', label: 'Disponible'}, 
                { key: 'user', label: 'Usuario'},                 { key: 'price', label: 'Precio'}, 
                { key: 'image', label: 'Imagen'}, 
            ],
            product: []
        }
    },
    methods: {
        getProducts () 
        {
            const path = 'http://localhost:8000/api/v1.0/product/'

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