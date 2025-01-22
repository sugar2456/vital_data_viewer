import HeartRateChart from '../ui/dashboard/heart_rate_graph';
import { SleepCard } from '../ui/dashboard/sleep_card';
import StepsChart from '../ui/dashboard/step_graph';
import { WeightCard } from '../ui/dashboard/weight_card';
import { CaloriesCard } from '../ui/dashboard/calories_card';
import { DevicesCard } from '../ui/dashboard/devices_card';

export default function Page() {
    return (
        <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
            <SleepCard />
            <CaloriesCard />
            <WeightCard />
            <DevicesCard />
            <div className="col-span-1 sm:col-span-2 lg:col-span-4">
                <StepsChart />
            </div>
            <div className="col-span-1 sm:col-span-2 lg:col-span-4">
                <HeartRateChart />
            </div>
        </div>
    );
}