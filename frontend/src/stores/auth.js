import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        isAuthenticated: false,
        user: null
    }),
    actions: {
        async login(username, password) {
            try {
                const res = await axios.post("api/auth/login/", {
                    username,
                    password,
                });
                debugger
                if (res) {
                    this.user = res.user;
                    this.isAuthenticated = true;
                } else {
                    this.user = null;
                    this.isAuthenticated = false;
                }
            } catch (err) {
                this.isAuthenticated = false;
            }
            return this.isAuthenticated;
        },
        async logout() {
            try {
                await axios.post("api/auth/logout/", null);
                this.isAuthenticated = false;
            } catch (err) {
                console.error(err);
                throw err;
            }
        },

        async getCurrentUser() {
            try {
                this.user = await axios.get("users/current/", null, { timeout: 2000 });
                this.isAuthenticated = true;
            } catch (err) {
                this.isAuthenticated = false;
            }
        }
    },
});
