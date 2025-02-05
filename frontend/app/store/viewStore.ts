import { create } from 'zustand';

interface ViewState {
  date: string;
  setDate: (date: string) => void;
}

export const useDateStore = create<ViewState>((set) => ({
  date: new Date().toISOString().split('T')[0],
  setDate: (date) => set({ date }),
}));

interface AuthState {
  token: string | null;
  setToken: (token: string | null) => void;
  removeToken: () => void;
  isAuthenticated: boolean;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: typeof window !== 'undefined' ? sessionStorage.getItem('token') : null,
  setToken: (token: string | null) => {
    if (token) {
      sessionStorage.setItem('token', token);
    } else {
      sessionStorage.removeItem('token');
    }
    set({ token, isAuthenticated: !!token });
  },
  removeToken: () => {
    sessionStorage.removeItem('token');
    set({ token: null, isAuthenticated: false });
  },
  isAuthenticated: typeof window !== 'undefined' ? !!sessionStorage.getItem('token') : false,
}));