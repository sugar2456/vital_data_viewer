import { create } from 'zustand';

interface FoodViewState {
    foodId: number;
    setFoodId: (foodId: number) => void;
}

export const useFoodViewDataStore = create<FoodViewState>((set) => ({
    foodId: 0,
    setFoodId: (foodId) => set({ foodId }),
}));