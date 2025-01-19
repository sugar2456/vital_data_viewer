import { Card } from '../ui/dashboard/cards';
import HeartRateChart from '../ui/dashboard/heart_rate_graph';
import { SleepCard } from '../ui/dashboard/sleep_card';
import StepsChart from '../ui/dashboard/step_graph';
import { WeightCard } from '../ui/dashboard/weight_card';

export default function Page() {
    const cardData: { title: string; value: number; type: 'sleep' | 'step' | 'activity' | 'weight' }[] = [
        { title: 'Activity', value: 30, type: 'activity' },
    ];

    return (
        <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
            <SleepCard />
            {cardData.map((card, index) => (
                <Card key={index} title={card.title} value={card.value} type={card.type} />
            ))}
            <WeightCard />
            <div className="col-span-1 sm:col-span-2 lg:col-span-4">
                <StepsChart />
            </div>
            <div className="col-span-1 sm:col-span-2 lg:col-span-4">
                <HeartRateChart />
            </div>
        </div>
    );
}