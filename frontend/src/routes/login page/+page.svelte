<script lang="ts">
    import { PostApi } from "$lib";
    
    let username: string = "";
    let password: string = "";

    async function Login(): Promise<void> {
            const response = await PostApi("/api/user/login", {
                username,
                password
            });

            const data = await response.json();

            if (response.ok && data.status) {
                window.location.href = "/home";
            } else if (response.status === 500) {
                alert("Server error: Please try again later or contact support");
            } else if (response.status === 401) {
                alert("Invalid username or password");
            } else {
                alert(data.message || "Login failed. Please try again");
            }

    }
</script>


<div class="login-container">
    <h1>Login</h1>

    <form on:submit|preventDefault={Login}>
        <div>
            <label for="username">Username:</label><br>
            <input type="text" id="username" bind:value={username} required>
        </div>

        <div>
            <label for="password">Password:</label><br>
            <input type="password" id="password" bind:value={password} required>
        </div>

        <div>
            <button type="submit">Login</button>
        </div>
    </form>

    <div>
        <a href="/signup page">Don't have an account? Sign up here</a>
    </div>
</div>



<style>
    .login-container {
        max-width: 400px;
        margin: 50px auto;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        background: white;
    }

    h1 {
        text-align: center;
        color: #333;
        margin-bottom: 20px;
    }

    form div {
        margin-bottom: 15px;
    }

    label {
        display: block;
        margin-bottom: 5px;
        color: #555;
    }

    input {
        width: 100%;
        padding: 8px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 16px;
    }

    button {
        width: 100%;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
    }

    button:hover {
        background-color: #45a049;
    }

    a {
        display: block;
        text-align: center;
        margin-top: 15px;
        color: #666;
        text-decoration: none;
    }

    a:hover {
        color: #4CAF50;
    }

    p {
        color: #ff4444;
        text-align: center;
        margin-bottom: 15px;
    }
</style>
