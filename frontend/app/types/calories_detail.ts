export interface CaloriesPeriod {
    consumed_calories_period: Dataset[];
    intaked_calories_period: Dataset[];
    total_calories_period: Dataset[];
}

export interface Dataset {
    dateTime: string;
    value: number;
}