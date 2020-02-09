<template>
  <div class="container">
      <div class="row">
          <div class="col text-left">
              <h2>Listado de productos</h2>

              <div class = "col-md-12">

                  <b-table striped hover :items="product" :fields="fields">

                  </b-table>

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
                { key: 'description', label: 'Descripcion'},
                { key: 'price', label: 'Precio'}, 
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