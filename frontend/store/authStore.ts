import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface AuthState {
  token: string | null;
  isAuthenticated: boolean;
  login: (token: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      isAuthenticated: false,
      login: (token: string) => {
        set({ token, isAuthenticated: true });
        // Set cookie for middleware
        document.cookie = `auth-token=${token}; path=/`;
      },
      logout: () => {
        set({ token: null, isAuthenticated: false });
        // Remove cookie
        document.cookie = 'auth-token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
      },
    }),
    {
      name: 'auth-storage',
    }
  )
); 