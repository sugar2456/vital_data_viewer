import { Card } from '../ui/dashboard/cards';
import StepsChart from '../ui/dashboard/step_graph';

export default function Page() {
    const cardData: { title: string; value: number; type: 'sleep' | 'step' | 'activity' | 'weight' }[] = [
        { title: 'Sleep', value: 8, type: 'sleep' },
        { title: 'Steps', value: 10000, type: 'step' },
        { title: 'Activity', value: 30, type: 'activity' },
        { title: 'Weight', value: 70, type: 'weight' },
    ];

    return (
        <div className="p-4 grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
            {cardData.map((card, index) => (
                <Card key={index} title={card.title} value={card.value} type={card.type} />
            ))}
            <div className="col-span-1 sm:col-span-2 lg:col-span-4">
                <StepsChart />
            </div>
        </div>
    );
}