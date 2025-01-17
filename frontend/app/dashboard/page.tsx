import { Card } from '../ui/dashboard/cards';
import HeartRateChart from '../ui/dashboard/heart_rate_graph';
import { SleepCard } from '../ui/dashboard/sleep_card';
import StepsChart from '../ui/dashboard/step_graph';

export default function Page() {
    const cardData: { title: string; value: number; type: 'sleep' | 'step' | 'activity' | 'weight' }[] = [
        { title: 'Steps', value: 10000, type: 'step' },
        { title: 'Activity', value: 30, type: 'activity' },
        { title: 'Weight', value: 70, type: 'weight' },
    ];

    return (
        <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
            <SleepCard />
            {cardData.map((card, index) => (
                <Card key={index} title={card.title} value={card.value} type={card.type} />
            ))}
            <div className="col-span-1 sm:col-span-2 lg:col-span-4">
                <StepsChart />
            </div>
            <div className="col-span-1 sm:col-span-2 lg:col-span-4">
                <HeartRateChart />
            </div>
        </div>
    );
}