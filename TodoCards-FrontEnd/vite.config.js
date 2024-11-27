import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	watch: {
		usePolling: true,
	},
	server: {
		proxy: {
			'/api': 'http://localhost:5000'
		}
	}
});
