<!--Generate from chatGPT. try to modify and understand in script part (line 9 - 22)-->
<script lang="ts">
    import { post_api_ping } from "$lib";
    let username: string = ""
    let password: string = ""
    let message: string = ""
    
    async function Login(): Promise<void> {
        const response = await fetch("http://localhost:8000/api/user/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();

            if (response.ok && data.status) {
                // Successful login, redirect or show success
                alert("Login successful!");
                window.location.href = "/dashboard"; // Redirect to another page
            } else {
                // Show error message
                message = "Login failed";
            }
    }
</script>

<h1>Login page</h1>

<label for="username">Username </label>
<input type="text" id="username" bind:value={username} />

<label for="password">Password </label>
<input type="password" id="password" bind:value={password} required />

<input type="button" value="login" on:click={Login}>

