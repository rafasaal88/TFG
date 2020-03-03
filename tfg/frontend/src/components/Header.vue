<template>
    <div class="">



 <b-navbar toggleable="lg" type="dark" variant="info shadow">

    <b-navbar-toggle target="nav-collapse" >
      </b-navbar-toggle>
   
    <b-collapse  id="nav-collapse" is-nav>
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
            


            <b-button size="lm" style="width: 100%" class="btn btn-dark" type="submit">Iniciar sesión</b-button>
            &nbsp;&nbsp;
            <b-button :to="{name:'Register'}" size="lm" class="btn btn-dark" style="width: 100%" >Registrarse</b-button>

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
            <b-button :to="{name:'Register'}" size="lm" class="btn btn-dark" >Registrarse</b-button>

        </b-nav-form>
    </div> 
        


        <b-nav-item-dropdown left v-if="token!=null">
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <span class="mr-3 d-lg-inline" style="color:white"> Hola {{user}}</span>
          </template>

        
                     
                
                         <b-dropdown-item v-on:click="logout">Cerrar sesión</b-dropdown-item>



        </b-nav-item-dropdown>





       
        
      </b-navbar-nav>
    </b-collapse>
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
            user: localStorage.getItem('user-name') || null,
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
                location.reload();
            })
            .catch(err => {
                localStorage.removeItem('user-token')
                localStorage.removeItem('user-name')
            })
            
        },

        logout() {
            this.$cookie.delete('user-token', {domain: 'localhost'});
            localStorage.removeItem('user-token');
            localStorage.removeItem('user-name');
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