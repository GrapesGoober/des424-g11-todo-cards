<script>
    import * as APIs from "$lib"

    let username = "" // the input requires a username & password
    let password = ""
    let wrongPassword = false
    async function login(){
        let status = await APIs.login(username, password)
        // upon successful login, we wanna redirect user to home page 
        if (status == true) {
            // (which is default endpoint)
            window.location.href = "/";
        }
        else if (status == "isAdmin") {
            window.location.href = "/admin";
        }
        // upon bad login, we might want to display something on the screen
        else {
            wrongPassword = true
        }
    }
</script>
<div class="loginpage">
    <h1>Login</h1>
    <div>
        <input type="text" placeholder="Username" bind:value={username}>
    </div>
    <div>
        <input type="password" placeholder="Password" bind:value={password}>
    </div>

    {#if wrongPassword}
    <p class="wrong-text">username or password is incorrect</p>  
    {/if}
    <button on:click={login}>Submit</button>

    <p class="signup-txt">If you don't have an account, sign up <a href="/signup">here</a></p>
</div>

<style>
    @import "../style.css";
    p {
        margin: 0;
    }
    div {
        width: 300px;
        height: 40px;
    }
    input {
        width: 250px;
        height: 28px;
        border-radius: 16px;
        border-width: 1px;
        padding-left: 16px;
    }
    button {
        width: 268px;
        height: 30px;
        border: none;
        border-radius: 15px;
        background-color: rgb(90, 90, 255);
        color: white;
        font-weight: bold;
        cursor: pointer;
    }
    button:hover {
        background-color: rgb(111, 111, 255);
    }
    button:active {
        background-color: rgb(129, 129, 255);
    }
    .wrong-text {
        color: red;
        font-size: 12px;
        margin-bottom: 12px;
    }
    .signup-txt {
        color: rgb(152, 152, 152);
        font-size: 12px;
        margin-top: 12px;
    }
    .loginpage {
        margin-left: 15px;
    }
</style>