export interface Weight {
    weight: number;
    bmi: number;
    fat: number;
    date: string;
}

export interface WeightPeriod {
    wight_list: WeightDetail[];
}

export interface WeightDetail {
    bmi: number;
    date: string;
    fat: number;
    logId: number;
    source: string;
    time: string;
    weight: number;
}