<template>
    <div class="">

    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand class="text-white" href="#">Frontend</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            

        <b-navbar-var class="ml-auto">

            <b-nav-form @submit.prevent="login" v-if="token==null">
                
                <b-form-input id="username" size="sm" class="nr-sm-2" v-model="username" placeholder="username" name="username"></b-form-input>
                <b-form-input id="password" size="sm" class="nr-sm-2" v-model="password" placeholder="password" type="password" name="password"></b-form-input>

                <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>

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
            })
            .catch(err => {
                localStorage.removeItem('user-token')
            })
        }
    }


}
</script>

<style>

</style>