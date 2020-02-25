<template lang="html">
     <div class="container">
      <div class="row">
          <div class="col text-left">

            <div>
                <h2>Editar productos</h2>
                {{ form }}                
            </div>
            
            <div class="row">
                <div class="col">
                    <div class="card">
                        <div class="card-body">

                            <form @onSubmit="onSubmit">

                                <div class="form-group row">
                                
                                    <label for="name" class="col-sm-2 col-form-label" >Nombre</label>
                                
                                    <div class="col-sm-6">

                                        <input type="text" placeholder="Nombre" name="name" class="form-control" v-model.trim="form.name">                                        

                                    </div>

                                </div>

                                <div class="form-group row">
                                
                                    <label for="description" class="col-sm-2 col-form-label">Descripción</label>
                                
                                    <div class="col-sm-6">

                                        <textarea placeholder="Descripción" name="description" class="form-control" v-model.trim="form.description"></textarea>                                   

                                    </div>

                                </div>


                                <div class="rows">
                                    <div class="col text-left">
                                        <b-button type="submit" variant="primary">Editar</b-button>
                                        <b-button type="submit" class="btn-large-space" :to="{ name: 'ListProduct' }">Cancelar</b-button>
                                    </div>                                
                                </div>

                            </form>

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
            form: {
                name: '',
                description: ''
            },
        }
    },
    methods: {
        getProducts () 
        {
            const path = 'http://localhost:8000/api/v1.0/product_list/'+this.id+'/'

            axios.get(path).then((response) => {
                this.form.name = response.data.name
                this.form.description = response.data.description
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

<style lang="css" scoped>

</style>