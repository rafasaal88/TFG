<template>
    <div class="" >

        <div class="" v-if="token==null">       
        
        <br>
        
            <div class="col-lg-12 mx-auto">       
                <div class="card rounded shadow shadow-sm">
                    <div class="card-body">
                        <div class="text-left">
                            
                            <div >
                                <center><h2>Registrar usuario</h2></center>
                            </div>
                            <hr>
                            
                                <div class="container" >

                                    <center>

                                        <form id="registeruser" @submit.prevent="CreateUser">
                                                            
                                            <div class="form-group">
                                                <label for="username" class="col-lg-6 mx-auto control-label text-left">Nombre de usuario</label>
                                                <div class="col-lg-6">
                                                    <input type="text" name="name" id="name" class="form-control" autofocus maxlength="40" autofocus required v-model="username">
                                                </div>
                                            </div>

                                            <div class="form-group">
                                                <label for="password" class="col-lg-6 control-label text-left">Contraseña</label>
                                                <div class="col-lg-6">
                                                    <input type="password"  name="password" id="password" class="form-control" autofocus maxlength="40" autofocus required v-model="password">
                                                </div>
                                            </div>
                                        
                                            <div class="form-group">
                                                <label for="password2" class="col-lg-6 control-label text-left">Repita contraseña</label>
                                                <div class="col-lg-6">
                                                    <input type="password" name="password2" id="password2" class="form-control" autofocus maxlength="40" autofocus required v-model="password2">
                                                </div>
                                            </div>       

                                            <div class="form-group">
                                                <label for="email" class="col-lg-6 control-label text-left">Email</label>
                                                <div class="col-lg-6">
                                                    <input type="email" name="email" id="email" class="form-control" autofocus maxlength="40" autofocus required v-model="email">
                                                </div>
                                            </div>

                                            <div class="form-group">
                                                <label for="first_name" class="col-lg-6 control-label text-left">Nombre</label>
                                                <div class="col-lg-6">
                                                    <input type="text" name="first_name" id="first_name" class="form-control" autofocus maxlength="40" autofocus required v-model="first_name">
                                                </div>
                                            </div>

                                            <div class="form-group">
                                                <label for="last_name" class="col-lg-6 control-label text-left">Apellidos</label>
                                                <div class="col-lg-6">
                                                    <input type="last_name" name="last_name" id="last_name" class="form-control" autofocus maxlength="40" autofocus required v-model="last_name">
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
                </div>
            </div>

        </div>

        <div class="" v-if="token!=null">       
            <br>

            <div class="col-lg-6 mx-auto">       
                <div class="card rounded shadow shadow-sm">
                    <div class="card-body">
                        <div class="text-center">
                                <h1><font style="color:black;">Ya se encuentra registrado. Si desea registrar una cuenta nueva debe cerrar sesión antes.</font></h1>
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
    name: 'register',
    components: {
    
    },

    data() {
        return {
            username:null,
            password:null,
            password2:null,
            email: null,
            first_name: null,
            last_name: null,
            token: localStorage.getItem('user-token') || null,
            user: localStorage.getItem('user-name') || null,
            api_ip: [],
            id_user: '',

        }
    },

    methods: {
        CreateUser() {
            if (this.password == this.password2) {


            console.log(this.username)
            axios.post('http://127.0.0.1:8000/api/v1.0/user/', {
                username: this.username,
                password: this.password,
                email: this.email,
                first_name: this.first_name,
                last_name: this.last_name,

            })
            .then (res => this.login())
            .catch(err => console.log(err))
            
            this.login();

            
            }

            else {
                alert('Las contraseñas deben ser iguales');
            }
        },

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
                location.reload();
            })
            .catch(err => {
                localStorage.removeItem('user-token')
                localStorage.removeItem('user-name')
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
        
        getIp(){
            const path = 'https://freegeoip.app/json/'


            axios.get(path).then((response) => {
                this.api_ip = response.data
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
                activity: "Visita sección",
                activity_name: "Registro",
                user: this.id_user,
            })
            .catch(err => {
                console.log(err)
            })

        }, 1000);
        },

        
    },

    created(){        
        this.getIp()
        this.getID()
        this.create_register_activity()
    }


}
</script>

<style>

</style>