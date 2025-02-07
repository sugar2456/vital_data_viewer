"use client";
import HeartRateChart from '../ui/dashboard/heart_rate_graph';
import { SleepCard } from '../ui/dashboard/sleep_card';
import StepsChart from '../ui/dashboard/step_graph';
import { BodyCard } from '../ui/dashboard/body_card';
import { ActivityCard } from '../ui/dashboard/activity_card';
import { DevicesCard } from '../ui/dashboard/devices_card';
import { useAuthRedirect } from '../hooks/useAuthRedirect';

export default function Page() {
    useAuthRedirect();
    return (
        <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4">
            <SleepCard />
            <ActivityCard />
            <BodyCard />
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