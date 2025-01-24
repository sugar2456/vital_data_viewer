import { create } from 'zustand';

interface ViewState {
  date: string;
  setDate: (date: string) => void;
}

export const useDateStore = create<ViewState>((set) => ({
  date: new Date().toISOString().split('T')[0],
  setDate: (date) => set({ date }),
}));