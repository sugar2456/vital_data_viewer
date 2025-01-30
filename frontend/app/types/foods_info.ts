export interface FoodUnit {
    id: number;
    name: string;
    plural: string;
}

export interface LoggedFood {
    accessLevel: string;
    amount: number;
    brand: string;
    calories: number;
    foodId: number;
    locale: string;
    mealTypeId: number;
    name: string;
    unit: FoodUnit;
    units: number[];
    creatorEncodedId?: string;
}

export interface Food {
    isFavorite: boolean;
    logDate: string;
    logId: number;
    loggedFood: LoggedFood;
    nutritionalValues?: {
        calories: number;
        carbohydrates: number;
        fat: number;
        protein: number;
    };
}

export interface FoodRecord {
    date: string;
    foods: Food[] | [];
}