<template>
    <div class="">


        <b-navbar toggleable="lg" type="dark" variant="dark">
            <b-navbar-brand href="/">Inicio</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse" >

            

            </b-navbar-toggle>
        
            <b-collapse  id="nav-collapse" is-nav>

                <b-navbar-nav>
                    <b-nav-item href="/recipe_list">Recetas</b-nav-item>
                    <b-nav-item href="/products_list">Productos</b-nav-item>
                    <b-nav-item href="/publicity_campaign_list">Campañas</b-nav-item>            
                    <b-nav-item href="/register" v-if="token==null">Registrarse</b-nav-item>
                </b-navbar-nav>

                <br>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                

            <!--Mobile version-->
            <div class="d-block d-sm-block d-md-none">

                <b-nav-form @submit.prevent="login" v-if="token==null">
                        
                        
                    <b-form-input id="username" size="lm" class="nr-sm-2" style="width: 100%" v-model="username" placeholder="usuario" name="username"></b-form-input>
                    &nbsp;&nbsp;
                    <b-form-input id="password" size="lm" class="nr-sm-2" style="width: 100%" v-model="password" placeholder="contraseña" type="password" name="password"></b-form-input>
                    &nbsp;&nbsp;
                    


                    <b-button size="lm" style="width: 100%" class="btn btn-dark btn-lg" type="submit">Iniciar sesión</b-button>
                    &nbsp;&nbsp;
                </b-nav-form>
            </div> 
                

            <!--Desktop version-->
            <div class="d-none d-sm-none d-md-block">



                <b-nav-form @submit.prevent="login" v-if="token==null">                        
                        
                    <b-form-input id="username" size="lm" class="nr-sm-2" v-model="username" placeholder="usuario" name="username"></b-form-input>
                    &nbsp;&nbsp;
                    <b-form-input id="password" size="lm" class="nr-sm-2" v-model="password" placeholder="contraseña" type="password" name="password"></b-form-input>
                    &nbsp;&nbsp;                    


                    <b-button size="lm" class="btn btn-dark" type="submit">Iniciar sesión</b-button>
                    &nbsp;&nbsp;

                </b-nav-form>
            </div> 
                


                <b-nav-item-dropdown left v-if="token!=null">

                <!-- Using 'button-content' slot -->

                <template v-slot:button-content>
                    <span class="mr-3 d-lg-inline" style="color:white"><b-icon icon="person-fill"></b-icon> Hola {{user}}</span>
                </template>

                    <b-dropdown-item href="#">Perfil <b-icon icon="gear-fill"></b-icon></b-dropdown-item>
                    <b-dropdown-item href="/point">Mis promociones <b-icon icon="award"></b-icon></b-dropdown-item>

            
                    <b-dropdown-item @click="$bvModal.show('bv-modal-example')">Cerrar sesión <b-icon icon="power"></b-icon></b-dropdown-item>

                </b-nav-item-dropdown>

            </b-navbar-nav>
            </b-collapse>
        </b-navbar>


        <div>

        <b-modal id="bv-modal-example" hide-footer>
            <template v-slot:modal-title>
            AVISO
            </template>
            <div class="d-block text-center">
            <h3>¿Está seguro que desea cerrar sesión?</h3>
            </div>
            <div>
                <center>
            <b-button class="btn btn-dark btn-lg" @click="$bvModal.hide('bv-modal-example')">Cancelar</b-button>
            <b-button class="btn btn-info btn-lg" v-on:click="logout">Aceptar</b-button>
                </center>
            </div>
        </b-modal>
        </div>




    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: "Header",
    components: {

    },
    data() {
        return {
            username: '',
            password: '',
            token: localStorage.getItem('user-token') || null,
            user: localStorage.getItem('user-name') || null,
            api_ip: [],
            id_user: '',
            activity: '',
        }
    },
    
    methods: {
        login() {
            axios.post('http://127.0.0.1:8000/api/v1.0/auth', {
                username: this.username,
                password: this.password,
            })
            
            .then(resp => {
                this.token = resp.data.access;
                this.user = this.username;
                console.log(this.token)
                localStorage.setItem('user-token', resp.data.access)
                localStorage.setItem('user-name', this.username)
                this.$cookie.set('user-token', resp.data.access, {expires: 1, domain: 'localhost'});
                this.activity = "Inicio de sesión";
                this.getID();
                this.create_register_activity();
            })
            .catch(err => {
                localStorage.removeItem('user-token')
                localStorage.removeItem('user-name')
            })
            
        },

        logout() {
            this.activity = "Cierre de sesión";
            this.create_register_activity();
            this.$cookie.delete('user-token', {domain: 'localhost'});
            localStorage.removeItem('user-token');
            localStorage.removeItem('user-name');
            this.token = null;
        },

        register() {
            console.log('Router')
        },



        getIp(){
            const path = 'https://freegeoip.app/json/'


            axios.get(path).then((response) => {
                this.api_ip = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },

        getID()
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

        create_register_activity() {

        setTimeout(() => {
                axios.post('http://127.0.0.1:8000/api/v1.0/register_activity/', {
                ip_address: this.api_ip.ip,
                country_name: this.api_ip.country_name,
                region_name: this.api_ip.region_name,
                city: this.api_ip.city,
                activity: this.activity,
                user: this.id_user,
            })
            .catch(err => {
                console.log(err)
            })
        location.reload();

        }, 1000);



        },  




    },

    created(){        
        this.getIp();   
        this.getID();


    }

}
</script>

<style>

</style>