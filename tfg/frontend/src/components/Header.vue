<template>
    <div class="">

    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand class="text-white" href="#">Frontend</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            

        <b-navbar-var class="ml-auto">

            <b-nav-form @submit.prevent="login" v-if="token==null">
                
                <b-form-input id="username" size="sm" class="nr-sm-2" v-model="username" placeholder="usuario" name="username"></b-form-input>
                <b-form-input id="password" size="sm" class="nr-sm-2" v-model="password" placeholder="contraseña" type="password" name="password"></b-form-input>

                <b-button size="sm" class="my-2 my-sm-0" type="submit">Iniciar sesión</b-button>
                <b-button :to="{name:'Register'}" size="sm" class="my-2 ml-2" >Registrarse</b-button>

            


            </b-nav-form>
<!--
            <b-nav-form @submit.prevent="register" v-if="token==null">

                <b-button :to="{name:'Register'}" size="sm" class="my-2 ml-2" type="submit">Registrarse</b-button>


            </b-nav-form>
-->

            <b-nav-form @submit.prevent="logout" v-if="token!=null">

                <b-button size="sm" class="my-2 ml-2" type="submit">Cerrar sesión</b-button>


            </b-nav-form>




        </b-navbar-var>

    </b-navbar>
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
                console.log(this.token)
                localStorage.setItem('user-token', resp.data.access)
                location.reload();
            })
            .catch(err => {
                localStorage.removeItem('user-token')
            })
            
        },

        logout() {
            localStorage.removeItem('user-token');
            this.token = null;
            location.reload();
        },
        register() {
            console.log('Router')
        }


    }


}
</script>

<style>

</style>