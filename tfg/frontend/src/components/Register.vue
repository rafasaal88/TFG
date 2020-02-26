<template>
    <div class="">

    <h2>Registro de usuario</h2>

    <form id="registeruser" @submit.prevent="CreateUser" v-if="token==null">
        <p>
            <label for="username">Usuario</label>
            <input class="ml-2" type="text" name="username" id="username" v-model="username">
            
        </p>

        <p>
            <label for="username">Usuario</label>
            <input class="ml-2" type="password" name="password" id="password" v-model="password">


        </p>

            <input type="submit" value="submit">

    </form>
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
            token: localStorage.getItem('user-token') || null,
        }
    },

    methods: {
        CreateUser() {
            console.log(this.username)
            axios.post('http://127.0.0.1:8000/api/v1.0/user/', {
                username: this.username,
                password: this.password,

            })
            .then (res => console.lo(res))
            .catch(err => console.log(err));
            this.$router.push('/')

        }
    }


}
</script>

<style>

</style>