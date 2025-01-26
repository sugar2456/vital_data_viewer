export interface SleepDetail {
    dateOfSleep: string;
    duration: number;
    efficiency: number;
    endTime: string;
    infoCode: number;
    levels: SleepLevel;
    logId: number;
    minutesAfterWakeup: number;
    minutesAsleep: number;
    minutesAwake: number;
    minutesToFallAsleep: number;
    startTime: string;
    timeInBed: number;
    type: string;
}

interface SleepLevel {
    data: SleepData[];
    shortData: SleepData[];
}

export interface SleepData {
    dateTime: string;
    level: string;
    seconds: number;
}