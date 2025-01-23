export interface HeartRateInfo {
    heart_rate_intraday: {
        time: string;
        value: number;
    }[];
}