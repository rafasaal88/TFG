<template>
  <div class="">

    <div v-if="tag.available==false">

        <div class="" >       
            <br>

            <div class="col-lg-12 mx-auto">       
                <div class="card rounded shadow shadow-sm">
                    <div class="card-body">
                        <div class="text-center">
                                <h4><font style="color:black;">Tag NFC desactivado</font></h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>




    </div>

        <div v-if="product.available==false && tag.available==true">

            <div class="" >       
                <br>

                <div class="col-lg-12 mx-auto">       
                    <div class="card rounded shadow shadow-sm">
                        <div class="card-body">
                            <div class="text-center">
                                    <h4><font style="color:black;">Producto no disponible</font></h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

    <div v-if="tag.available==true">  





        <div class="" v-if="token==null && product.available">       
            <br>

            <div class="col-lg-12 mx-auto">       
                <div class="card rounded shadow shadow-sm">
                    <div class="card-body">
                        <div class="text-center">
                                <h4><font style="color:black;">Debe iniciar sesión para poder registrar la promoción del producto!!</font></h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br>

      




        <div class="container" v-if="product.available==true">
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
            product: [],
           // api_ip: [],
            latitud: '',
            longitud: '',
            api_ip: [],
            activity: "Visita sección",
            activity_name: "TAG NFC",

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
                longitude: this.tag.longitude,
                latitude: this.tag.latitude,
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
                    this.create_register_activity_point_accept();
                }
                else
                {
                    this.exists = true;
                    this.create_register_activity_point_denied(); 
                }
                

            })
            .catch((error) => {
                console.log(error)
            })

            
            
        },
        create_register_activity_point_accept() {
        
            
        

        setTimeout(() => {

                axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                    ip_address: this.api_ip.ip,
                    country_name: this.api_ip.country_name,
                    region_name: this.api_ip.region_name,
                    city: this.api_ip.city,
                    activity: this.activity,
                    activity_name: this.activity_name,
                    user: this.id_user,
                    activity: "Registro",
                    activity_name: "Promocion",
                    tag_id: this.tag.id,
                    tag_nfc_status: "Correcto",
                    tag_nfc_description: this.tag.description,
                    tag_nfc_latitude: this.tag.latitude,
                    tag_nfc_longitude: this.tag.longitude,
                    tag_nfc_product: this.product.name,
                    
                        })
                    .catch(err => {
                    console.log(err)
                    })
                           
    


        }, 4000);
        },

        create_register_activity_point_denied() {
        
            
        

        setTimeout(() => {

                axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                    ip_address: this.api_ip.ip,
                    country_name: this.api_ip.country_name,
                    region_name: this.api_ip.region_name,
                    city: this.api_ip.city,
                    activity: this.activity,
                    activity_name: this.activity_name,
                    user: this.id_user,
                    activity: "Registro",
                    activity_name: "Promocion",
                    tag_id: this.tag.id,
                    tag_nfc_status: "Denegado. Promoción ya registrada",
                    tag_nfc_description: this.tag.description,
                    tag_nfc_latitude: this.tag.latitude,
                    tag_nfc_longitude: this.tag.longitude,
                    tag_nfc_product: this.product.name,
                    
                        })
                    .catch(err => {
                    console.log(err)
                    })
                           
    


        }, 4000);
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

        create_register_activity() {
        
        

        setTimeout(() => {
                if (this.tag.available == true & this.product.available == true)
                {
                    axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                    ip_address: this.api_ip.ip,
                    country_name: this.api_ip.country_name,
                    region_name: this.api_ip.region_name,
                    city: this.api_ip.city,
                    activity: this.activity,
                    activity_name: this.activity_name,
                    user: this.id_user,
                    tag_id: this.tag.id,
                    tag_nfc_status: "correcto",
                    tag_nfc_description: this.tag.description,
                    tag_nfc_latitude: this.tag.latitude,
                    tag_nfc_longitude: this.tag.longitude,
                    tag_nfc_product: this.product.name,
                    
                        })
                    .catch(err => {
                    console.log(err)
                    })
                }
                
                
    

                if (this.tag.available == false & this.product.available == true)
                {
                    axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                    ip_address: this.api_ip.ip,
                    country_name: this.api_ip.country_name,
                    region_name: this.api_ip.region_name,
                    city: this.api_ip.city,
                    activity: this.activity,
                    activity_name: this.activity_name,
                    user: this.id_user,
                    tag_id: this.tag.id,
                    tag_nfc_status: "tag desactivado",
                    tag_nfc_description: this.tag.description,
                    tag_nfc_latitude: this.tag.latitude,
                    tag_nfc_longitude: this.tag.longitude,
                    tag_nfc_product: this.product.name,
                    
                        })
                    .catch(err => {
                    console.log(err)
                    })
                }

                if (this.tag.available == true & this.product.available == false)
                {
                    axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                    ip_address: this.api_ip.ip,
                    country_name: this.api_ip.country_name,
                    region_name: this.api_ip.region_name,
                    city: this.api_ip.city,
                    activity: this.activity,
                    activity_name: this.activity_name,
                    user: this.id_user,
                    tag_id: this.tag.id,
                    tag_nfc_status: "producto desactivado",
                    tag_nfc_description: this.tag.description,
                    tag_nfc_latitude: this.tag.latitude,
                    tag_nfc_longitude: this.tag.longitude,
                    tag_nfc_product: this.product.name,
                    
                        })
                    .catch(err => {
                    console.log(err)
                    })
                }

                if (this.tag.available == false & this.product.available == false)
                {
                    axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                    ip_address: this.api_ip.ip,
                    country_name: this.api_ip.country_name,
                    region_name: this.api_ip.region_name,
                    city: this.api_ip.city,
                    activity: this.activity,
                    activity_name: this.activity_name,
                    user: this.id_user,
                    tag_id: this.tag.id,
                    tag_nfc_status: "producto y tag desactivado",
                    tag_nfc_description: this.tag.description,
                    tag_nfc_latitude: this.tag.latitude,
                    tag_nfc_longitude: this.tag.longitude,
                    tag_nfc_product: this.product.name,
                    
                        })
                    .catch(err => {
                    console.log(err)
                    })
                }


        }, 4000);
        },

    },

    created(){        
        this.getTag();   
        this.getID();  
        this.getIp();
        this.create_register_activity();
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