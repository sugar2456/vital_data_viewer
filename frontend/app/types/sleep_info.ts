export interface SleepInfo {
    totalMinutesAsleep: number;
    totalSleepRecords: number;
    totalTimeInBed: number;
    stages: Stage;
}

interface Stage {
    deep: number;
    light: number;
    rem: number;
    wake: number;
}