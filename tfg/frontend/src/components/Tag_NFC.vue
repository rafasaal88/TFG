<template>
  <div class="">

    <div class="" v-if="token==null">       
        <br>

        <div class="col-lg-12 mx-auto">       
            <div class="card rounded shadow shadow-sm">
                <div class="card-body">
                    <div class="text-center">
                            <h1><font style="color:black;">Debe iniciar sesión para poder registrar la promoción del producto!!</font></h1>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <br>

    




    <div class="container" v-if="product.available">
      <div class="row">        
        <div class="col-lg-8">
          <div class="card shadow mb-3" >

            <div class="card-body d-flex flex-row">      
              <div>            

                <h4 class="card-title font-weight-bold mb-2" v-if="product.unit == 'kg'">{{product.name}}: {{product.price}} €/Kg</h4>

                <h4 class="card-title font-weight-bold mb-2" v-if="product.unit == 'litros'">{{product.name}}: {{product.price}} €/Litro</h4>

                <h4 class="card-title font-weight-bold mb-2" v-if="product.unit == 'unidad'">{{product.name}}: {{product.price}} €/Unidad</h4> 
                
                <h5 class="card-title font-weight-bold mb-2">Promoción disponible: {{tag.description}}</h5>             
            
                    
              </div>      
            </div>

            <div class="view overlay">
              <img class="card-img-top rounded-0" :src="product.image" alt="Card image cap">
            </div>          
            
            <div class="container">
              <br>   
                <p>{{product.description}}</p>
            
                <hr>
                    
                <div class="" v-if="token!=null">       

                    <b-nav-form v-if="check_insert">

                        <div class="col-lg-12 mx-auto">       
                            <h4><font style="color:black;">Promoción registrada con éxito</font></h4>
                        </div>    
            
                    </b-nav-form>

                    <b-nav-form v-if="exists">

                        <div class="col-lg-12 mx-auto">       
                            <h4><font style="color:black;">Esta promoción ya la tienes registrada</font></h4>                                  
                        </div>            
            
                    </b-nav-form>

                    

                    <div class="form-group">
                        <div class="col-lg-12" v-if="!exists">
                            <button class="btn btn btn-secondary btn-block btn-lg" v-if="!check_insert" v-on:click="checkPoint()" >Obtener promoción</button>
                        </div>
                    </div> 

                </div>
            <br>

            </div>




          </div>
        </div>
      </div>
    </div>
{{api_ip}}
<br>
latitud: {{latitud}}
<br>
longitud: {{longitud}}

                            <button class="btn btn btn-secondary btn-block btn-lg" v-on:click="getPosition()" >Localización</button>




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
            product: [],
            api_ip: [],
            latitud: '',
            longitud: '',
        }
    },
    methods: {

        getIp(){
            const path = 'https://freegeoip.app/json/'


            axios.get(path).then((response) => {
                this.api_ip = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },


        getPosition(){
            var content = document.getElementById("geolocation-test");

            this.gettingLocation = true;
            // get position
            navigator.geolocation.getCurrentPosition(pos => {
            this.gettingLocation = false;

            this.longitud = pos.coords.longitude;
            this.latitud = pos.coords.latitude;


            }, err => {
            this.gettingLocation = false;
            this.errorStr = err.message;
            })
















            if (navigator.geolocation)
            {
                navigator.geolocation.getCurrentPosition(function(objPosition)
                {
                    var lon = objPosition.coords.longitude;
                    var lat = objPosition.coords.latitude;
                        
                    self.longitud = objPosition.coords.longitude;

                    



                }, 
                
                function(objPositionError)
                {
                    switch (objPositionError.code)
                    {
                        case objPositionError.PERMISSION_DENIED:
                            content.innerHTML = "No se ha permitido el acceso a la posición del usuario.";
                        break;
                        case objPositionError.POSITION_UNAVAILABLE:
                            content.innerHTML = "No se ha podido acceder a la información de su posición.";
                        break;
                        case objPositionError.TIMEOUT:
                            content.innerHTML = "El servicio ha tardado demasiado tiempo en responder.";
                        break;
                        default:
                            content.innerHTML = "Error desconocido.";
                    }
                }, 
                {
                    maximumAge: 75000,
                    timeout: 15000
                });
            }
            else
            {
                content.innerHTML = "Su navegador no soporta la API de geolocalización.";
            }
        },

        getTag () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/tag_nfc/'+this.id+'/'

            axios.get(path).then((response) => {
                this.tag = response.data
                this.getProduct();
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

        getProduct () 
        {
            const path = 'http://127.0.0.1:8000/api/v1.0/product_list/'+this.tag.product+'/'

            axios.get(path).then((response) => {
                this.product = response.data
            })
            .catch((error) => {
                this.available = false;
                console.log(error)
            })
        },






    },

    created(){        
        this.getTag();   
        this.getID();  
        this.getIp();
        this.getPosition();
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