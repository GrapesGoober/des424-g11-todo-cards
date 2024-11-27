<script>
    import * as APIs from "$lib"

    let signup_username = ""
    let signup_password = ""
    let signup_confirm_password = ""
    let signup_status = false;

    let errorMessage = ""

    async function signup() {

        if (signup_username == "" || signup_password == "" || signup_confirm_password == "") {
            errorMessage = "Please fill in all forms"
            return
        }

        if (signup_password != signup_confirm_password) {
            errorMessage = "Password doesn't match";
            return
        }

        signup_status = await APIs.signup(signup_username, signup_password);
        if (signup_status === true) {
            window.location.href = "/";
        }
        else {
            errorMessage = signup_status
        }
    }

    async function goback(){
        window.location.href = "/login";
    }
</script>

<!-- Font Awesome 5 Free -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
<link rel="apple-touch-icon" href="/custom_icon.png"/>
<div class="signuppage">
    <div class="header">
        <!--might add an icon for going back to login page-->
        <button class="goback_btn" on:click={goback}><i class="fas fa-angle-left"></i></button>
        <h1>Sign up</h1>
    </div>
    <div>
        <input type="text" placeholder="Username" bind:value={signup_username}>
    </div>
    <div>
        <input type="password" placeholder="Password" bind:value={signup_password}> 
    </div>
    <div>
        <input type="password" placeholder="Confirm Password" bind:value={signup_confirm_password}>
    </div>

    {#if errorMessage}
        <p class="wrong-text">{errorMessage}</p>  
    {/if}
    <button class="signup_btn" on:click={signup}>Sign up</button>
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
    .signuppage {
        margin-left: 15px;
    }
    input {
        width: 250px;
        height: 28px;
        border-radius: 16px;
        border-width: 1px;
        padding-left: 16px;
    }
    .signup_btn {
        width: 268px;
        height: 30px;
        border: none;
        border-radius: 15px;
        background-color: rgb(90, 90, 255);
        color: white;
        font-weight: bold;
        cursor: pointer;
    }
    .signup_btn:hover {
        background-color: rgb(111, 111, 255);
    }
    .signup_btn:active {
        background-color: rgb(129, 129, 255);
    }
    .wrong-text {
        color: red;
        font-size: 12px;
        margin-bottom: 12px;
        margin-right: 10px;
    }
    .header {
        margin-top: 20px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }
    .goback_btn {
        font-weight: bold;
        font-size: 36px;
        margin-right: 12px;
        background-color: white;
        padding: 0;
        border: none;
        cursor: pointer;
    }
    .goback_btn:active {
        color: rgb(77, 77, 77);
    }
</style>