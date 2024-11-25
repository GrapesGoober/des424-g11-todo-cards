<script lang="ts">
    import { PostApi } from "$lib";
    
    let username: string = "";
    let password: string = "";
    let confirmPassword: string = "";
    let date_of_birth: string = "";
    let email: string = "";


    function validateForm(): boolean {
        if (username.length < 5 || username.length > 20) {
            alert("Username must be between 5 and 20 characters");
            return false;
        }
        
        if (password.length < 5 || password.length > 20) {
            alert("Password must be between 5 and 20 characters");
            return false;
        }

        if (password !== confirmPassword) {
            alert("Passwords do not match");
            return false;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert("Please enter a valid email address");
            return false;
        }

        if (!date_of_birth) {
            alert("Please enter your date of birth");
            return false;
        }

        return true;
    }

    async function Signup(): Promise<void> {
        if (!validateForm()) {
            return;
        }

        const response = await PostApi("/api/user/signup", {
            username,
            password,
            date_of_birth,
            email
        });

        const data = await response.json();

        if (response.ok && data.status) {
            alert("Signup successful!");
            window.location.href = "/login page";
        } else {
            alert(data.message || "Signup failed. Please try again.");
        }
    }
</script>


<div class="signup-container">
    <h1>Sign Up</h1>

    <form on:submit|preventDefault={Signup}>
        <div>
            <label for="username">Username:</label><br>
            <input type="text" id="username" bind:value={username} required>
        </div>

        <div>
            <label for="email">Email:</label><br>
            <input type="email" id="email" bind:value={email} required>
        </div>

        <div>
            <label for="password">Password:</label><br>
            <input type="password" id="password" bind:value={password} required>
        </div>

        <div>
            <label for="confirmPassword">Confirm Password:</label><br>
            <input type="password" id="confirmPassword" bind:value={confirmPassword} required>
        </div>

        <div>
            <label for="date_of_birth">Date of Birth:</label><br>
            <input type="date" id="date_of_birth" bind:value={date_of_birth} required>
        </div>

        <div>
            <button type="submit">Sign Up</button>
        </div>
    </form>

    <div>
        <a href="/login page">Back to Login</a>
    </div>
</div>

<style>
    .signup-container {
        max-width: 400px;
        margin: 50px auto;
        padding: 30px;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        background: white;
    }

    h1 {
        text-align: center;
        color: #333;
        margin-bottom: 30px;
        font-size: 28px;
    }

    form div {
        margin-bottom: 20px;
    }

    label {
        display: block;
        margin-bottom: 8px;
        color: #555;
        font-size: 16px;
    }

    input {
        width: 100%;
        padding: 12px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 16px;
        transition: border-color 0.3s;
    }

    input:focus {
        outline: none;
        border-color: #4CAF50;
    }

    input[type="date"] {
        color: #555;
    }

    button {
        width: 100%;
        padding: 12px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
        margin-top: 10px;
    }

    button:hover {
        background-color: #45a049;
    }

    .login-link {
        margin-top: 20px;
        text-align: center;
    }

    a {
        color: #4CAF50;
        text-decoration: none;
        font-size: 14px;
    }

    a:hover {
        text-decoration: underline;
    }

    .error {
        color: #ff4444;
        text-align: center;
        margin-bottom: 20px;
        font-size: 14px;
        background-color: #ffebee;
        padding: 10px;
        border-radius: 4px;
    }
</style>