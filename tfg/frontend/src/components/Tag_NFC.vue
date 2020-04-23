<template>
  <div class="">


    <div class="" v-if="token==null">       
        <br>

        <div class="col-lg-12 mx-auto">       
            <div class="card rounded shadow shadow-sm">
                <div class="card-body">
                    <div class="text-center">
                            <h1><font style="color:black;">Debe loguearse para poder registrar la promoción del producto!!</font></h1>
                    </div>
                </div>
            </div>
        </div>
    </div>

<br>




    <div class="" v-if="token!=null">       

        <b-nav-form v-if="check_insert">

            <div class="col-lg-12 mx-auto">       
                <div class="card rounded shadow shadow-sm">
                    <div class="card-body">
                        <div class="text-center">
                                <h1><font style="color:black;">Promoción registrada con éxito</font></h1>
                        </div>
                    </div>
                </div>
            </div>            
  
        </b-nav-form>

        <b-nav-form v-if="exists">

            <div class="col-lg-12 mx-auto">       
                <div class="card rounded shadow shadow-sm">
                    <div class="card-body">
                        <div class="text-center">
                                <h1><font style="color:black;">Esta promoción ya la tienes registrada</font></h1>
                        </div>
                    </div>
                </div>
            </div>            
  
        </b-nav-form>


        <b-nav-form @submit.prevent="checkPoint" v-if="!exists">

            <b-button size="lm" class="btn btn-dark" v-if="!check_insert" type="submit">Obtener promoción</b-button>
            &nbsp;&nbsp;

        </b-nav-form>

    </div>





</div>





</template>

<script>

import axios from 'axios';

export default {
    data(){
        return {
            id: this.$route.params.id,
            tag: [],
            token: localStorage.getItem('user-token') || null,
            user: localStorage.getItem('user-name') || null,
            id_user: '',
            exists : false,
            check_insert: false,
        }
    },
    methods: {


        getRecipe () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/tag_nfc/'+this.id+'/'

            axios.get(path).then((response) => {
                this.tag = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            
        },

        getID () 
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

        create_point() {
          console.log("estoy aqui")
            axios.post('http://127.0.0.1:8000/api/v1.0/point/', {
                description: this.tag.description,
                user: this.id_user,
                product: this.tag.product,
                publicity_campaign: this.tag.publicity_campaign,
            })
            .catch(err => {
                console.log(err)
            })
            
        },  

        checkPoint () 
        {
           const path = 'http://127.0.0.1:8000/api/v1.0/point/'

            axios.get(path).then((response) => {
                var TagFound = null;
                TagFound = response.data.find( item => item.product == this.tag.product && item.user == this.id_user && item.description == this.tag.description && item.publicity_campaign == this.tag.publicity_campaign);
                
               
                if (TagFound == undefined)
                {
                    console.log ("No hemos encontrado nada");
                    this.create_point();
                    this.check_insert = true;
                }
                else
                {
                    this.exists = true;
                }
                

            })
            .catch((error) => {
                console.log(error)
            })

            
        },








    },

    created(){        
        this.getRecipe();   
        this.getID();  
       
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