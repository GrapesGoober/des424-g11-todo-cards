<script lang="ts">
    let username: string = "";
    let password: string = "";
    let loginStatus: string = "";

    async function handleLogin() {
        const response = await fetch('/api/user/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username,
                password
            })
        });

        const result = await response.json();
        if (result.status) {
            loginStatus = "Login successful!";
            // You can redirect to dashboard or home page here
            // window.location.href = '/dashboard';
        } else {
            loginStatus = "Login failed. Please check your credentials.";
        }
    }
</script>

<div class="login-container">
    
    <div class="login_form">
    <form on:submit|preventDefault={handleLogin}>
        <h1>Login</h1>
        <label for="username: ">Username:</label>
        <input 
            type="text" 
            id="username"
            bind:value={username}
            required
        >
        <label for="password">Password:</label>
        <input 
            type="password" 
            id="password"
            bind:value={password}
            required
        >
        

        <button type="submit">Login</button>
    </form>
    </div>
    
    {#if loginStatus}
        <p class="status-message">{loginStatus}</p>
    {/if}
</div>

<div>
    <a href="/signup">Sign up here</a>
</div>