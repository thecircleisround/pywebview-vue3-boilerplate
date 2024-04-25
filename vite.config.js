import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { resolve } from "path";
import { fileURLToPath, URL } from 'node:url';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  root: resolve("./src"),
  base: "/static/",
  server: {
    host: "localhost",
    port: 5174,
    open: false,
    fs:{
      allow: ['../../..'],
      base: ['/'] 
    },
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    resolve: {
      extensions: [".vue", ".js", ".jsx", ".json", ".css", ".scss", ".woff", ".ttf"],
    },
    alias: {
                '__STATIC__': 'static',
                "@": resolve(__dirname, "./src"),
                "~@": resolve(__dirname, "./src"),
                "~": resolve(__dirname, "./node_modules"),
            },
  },
  build: {
    outDir: resolve("./static/dist"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "es2015",
    rollupOptions: {
      input: {
        main: resolve("./src/main.jsx"),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
});
