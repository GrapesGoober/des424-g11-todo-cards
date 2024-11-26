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

<style>
    .loginpage {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        background-color: #f5f5f5;
        padding: 40px;
    }

    h1 {
        color: #333;
        margin-bottom: 2rem;
        font-size: 3.5rem;
        font-weight: bold;
    }

    input {
        width: 400px;
        padding: 15px 25px;
        margin: 12px 0;
        border: 1px solid #ddd;
        border-radius: 8px;
        font-size: 1.2rem;
        transition: border-color 0.3s ease;
    }

    input:focus {
        outline: none;
        border-color: #4CAF50;
        box-shadow: 0 0 8px rgba(76, 175, 80, 0.3);
    }

    button {
        background-color: #4CAF50;
        color: white;
        padding: 16px 50px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1.2rem;
        margin-top: 25px;
        min-width: 200px;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
    }

    .wrong-text {
        color: #ff3e3e;
        margin-top: 15px;
        font-size: 1.1rem;
    }

    .signup-txt {
        margin-top: 30px;
        color: #666;
        font-size: 1.1rem;
    }

    .signup-txt a {
        color: #4CAF50;
        text-decoration: none;
        font-weight: bold;
        padding: 5px;
    }

    .signup-txt a:hover {
        text-decoration: underline;
    }

    @media (min-width: 1200px) {
        input {
            width: 500px;
        }
        
        button {
            min-width: 250px;
        }
    }
</style>

<link rel="apple-touch-icon" href="/custom_icon.png"/>
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
