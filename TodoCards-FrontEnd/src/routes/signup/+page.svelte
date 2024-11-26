<script>
    import * as APIs from "$lib"

    let username = ""
    let password = ""
    let confirmPassword = ""
    //let passwordMismatch = false
    //let signupFailed = false

    async function signup() {
        if (password !== confirmPassword) {
            //passwordMismatch = true
            alert("Passwords do not match")
            return
        }
        //passwordMismatch = false
        
        let status = await APIs.signup(username, password)
        if (status == true) {
            window.location.href = "/login"
        } else {
            alert("Username already exists")
            //signupFailed = true
        }
    }
</script>

<style>
    .signuppage {
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

    .error-text {
        color: #ff3e3e;
        margin-top: 15px;
        font-size: 1.1rem;
    }

    .login-txt {
        margin-top: 30px;
        color: #666;
        font-size: 1.1rem;
    }

    .login-txt a {
        color: #4CAF50;
        text-decoration: none;
        font-weight: bold;
        padding: 5px;
    }

    .login-txt a:hover {
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

<div class="signuppage">
    <h1>Sign Up</h1>
    <div>
        <input type="text" placeholder="Username" bind:value={username}>
    </div>
    <div>
        <input type="password" placeholder="Password" bind:value={password}>
    </div>
    <div>
        <input type="password" placeholder="Confirm Password" bind:value={confirmPassword}>
    </div>

    <!-- {#if passwordMismatch}
    <p class="error-text">Passwords do not match</p>
    {/if}

    {#if signupFailed}
    <p class="error-text">Username already exists</p>
    {/if} -->

    <button on:click={signup}>Sign Up</button>

    <p class="login-txt">Already have an account? Login <a href="/login">here</a></p>
</div>
