export interface ActivityDetail {
    calories_intraday: CaloriesDataset[];
    step_intraday: Dataset[];
    distance_intraday: Dataset[];
    heart_rate_intraday: Dataset[];
}

export interface CaloriesDataset {
    level: number;
    mets: number;
    time: string;
    value: number;
}

export interface Dataset {
    time: string;
    value: number;
}