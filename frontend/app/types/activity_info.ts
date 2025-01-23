export interface ActivityInfo {
    caloriesOut: number;
    caloriesBMR: number;
    steps: number;
    distances: Distance[];
    floors: number;
    elevation: number;
    sedentaryMinutes: number;
    lightlyActiveMinutes: number;
    fairlyActiveMinutes: number;
    veryActiveMinutes: number;
}

interface Distance {
    activity: string;
    distance: number;
}