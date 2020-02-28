<template>
    <div class="">



<div class="card-header" style="background-color:#f2f2f2;">
        <center><h2>Registrar usuario</h2></center>
    </div>

    <div class="card-body text-justify" style="background-color:white;">
        <div class="container" >

            <center>

                <form id="registeruser" @submit.prevent="CreateUser" v-if="token==null">
                                      
                    <div class="form-group">
                        <label for="name" class="col-lg-6 control-label text-left">Nombre de usuario</label>
                        <div class="col-lg-6">
                            <input type="text" name="name" id="name" class="form-control" autofocus maxlength="40" autofocus required v-model="username">
                        </div>
                    </div>

                     <div class="form-group">
                        <label for="name" class="col-lg-6 control-label text-left">Contraseña</label>
                        <div class="col-lg-6">
                            <input type="password" name="password" id="password" class="form-control" autofocus maxlength="40" autofocus required v-model="password">
                        </div>
                    </div>
                   
                     <div class="form-group">
                        <label for="name" class="col-lg-6 control-label text-left">Repita contraseña</label>
                        <div class="col-lg-6">
                            <input type="password" name="password2" id="password2" class="form-control" autofocus maxlength="40" autofocus required v-model="password2">
                        </div>
                    </div>                   





                    <div class="form-group">
                        <div class="col-lg-6">
                            <hr>
                            <button type="submit" class="btn btn-info btn-block">Registrarse</button>
                        </div>
                    </div> 
                       
                </form> 

            </center>
         
        </div>
    </div>


















    </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'register',
    components: {
    
    },

    data() {
        return {
            username:null,
            password:null,
            password2:null,
            token: localStorage.getItem('user-token') || null,
        }
    },

    methods: {
        CreateUser() {
            if (this.password == this.password2) {


            console.log(this.username)
            axios.post('http://127.0.0.1:8000/api/v1.0/user/', {
                username: this.username,
                password: this.password,

            })
            .then (res => console.lo(res))
            .catch(err => console.log(err));
            this.$router.push('/')
            }
            else {
                alert('Las contraseñas deben ser iguales');
            }
        }
    }


}
</script>

<style>

</style>