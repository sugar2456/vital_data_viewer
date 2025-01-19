"use client";

import { FaMoon } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';
import { Card } from '@/app/ui/commons/card';

export function SleepCard() {
    const Icon = FaMoon;
    const sleepInfo = {
        totalSleepTime: "8時間",
        sleepCount: 1,
    };
    const sleepStage = ["深い睡眠：2時間", "浅い睡眠：2時間", "レム睡眠：2時間", "覚醒状態：2時間"];

    return (
        <Card title="睡眠" icon={Icon}>
            <MainInnerCard totalSleepTime={sleepInfo.totalSleepTime} sleepCount={sleepInfo.sleepCount} />
            <SubInnerCard title="睡眠ステージ" sleepList={sleepStage} />
        </Card>
    );
}

interface MainInnerCardProps {
    totalSleepTime: string;
    sleepCount: number;
}

const MainInnerCard: React.FC<MainInnerCardProps> = ({ totalSleepTime, sleepCount }) => {
    return (
        <div className="rounded-xl bg-white px-4 py-4 shadow-sm">
        <p
            className={`${lusitana.className}
        truncate text-2xl pb-2`}
        >
            トータル睡眠時間：{totalSleepTime}
        </p>
        <p
            className={`${lusitana.className}
        truncate text-2xl`}
        >
            本日の睡眠回数：{sleepCount}
        </p>
    </div>
    );
}

interface SubInnerCardProps {
    title: string;
    sleepList: string[];
}

const SubInnerCard: React.FC<SubInnerCardProps> = ({ title, sleepList }) => {
    return (
        <div className="rounded-xl bg-white p-4 shadow-sm">
            <h3 className="text-lg font-semibold mb-2">{title}</h3>
            <ul className="pl-4">
                {sleepList.map((sleep: string, index: number) => (
                    <li key={index} className="flex justify-between">
                        {sleep}
                    </li>
                ))}
            </ul>
        </div>
    );
};