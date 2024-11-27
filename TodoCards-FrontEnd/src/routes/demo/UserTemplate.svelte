<script>
    import * as APIs from "$lib"

    let signup_username = ""
    let signup_password = ""
    let signup_status = false;
    async function signup(){
        signup_status = await APIs.signup(signup_username, signup_password)
    }

    let username = "" // the input requires a username & password
    let password = ""
    let status = false // status can either be true or false
    async function login(){
        status = await APIs.login(username, password)
    }

    async function logout(){
        status = await APIs.logout()
    }

</script>

signup_status = {signup_status} <br>
<input type="text" placeholder="username" bind:value={signup_username}>
<input type="password" placeholder="password" bind:value={signup_password}> 
<input type="button" value="signup" on:click={signup}> <br>
login status = {status} <br>
<input type="text" placeholder="username" bind:value={username}>
<input type="password" placeholder="password" bind:value={password}>
<input type="button" value="login" on:click={login}>
<input type="button" value="logout" on:click={logout}>