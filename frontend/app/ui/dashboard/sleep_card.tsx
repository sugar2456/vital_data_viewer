"use client";

import { FaMoon } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';

export function SleepCard() {
    const Icon = FaMoon;
    const sleepList = ["深い睡眠：2時間", "浅い睡眠：2時間", "レム睡眠：2時間", "覚醒状態：2時間"];

    return (
        <div className="rounded-xl bg-gray-50 p-2 shadow-sm">
            <div className="flex p-4">
                {Icon ? <Icon className="h-5 w-5 text-gray-700" /> : null}
                <h3 className="ml-2 text-sm font-medium">睡眠</h3>
            </div>
            <div className="flex flex-col gap-2">
                <div className="rounded-xl bg-white px-4 py-4 shadow-sm">
                    <p
                        className={`${lusitana.className}
                    truncate text-2xl pb-2`}
                    >
                        トータル睡眠時間：8時間
                    </p>
                    <p
                        className={`${lusitana.className}
                    truncate text-2xl`}
                    >
                        本日の睡眠回数：1回
                    </p>
                </div>
                <InnerCard title="睡眠ステージ" sleepList={sleepList} />
            </div>
        </div>
    );
}

interface InnerCardProps {
    title: string;
    sleepList: string[];
}


const InnerCard: React.FC<InnerCardProps> = ({ title, sleepList }) => {
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