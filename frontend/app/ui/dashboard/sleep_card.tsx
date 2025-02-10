"use client";
import React, { use, useEffect, useState } from 'react';
import { FaMoon } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';
import { Card } from '@/app/ui/commons/card';
import { SleepInfo } from "@/app/types/sleep_info";
import { authenticatedGetRequest } from '@/app/lib/common/apiClient';
import { Loading } from '../commons/loadings';
import { useDateStore } from '@/app/store/viewStore';

export function SleepCard() {
    const Icon = FaMoon;
    const [isLoading, setIsLoading] = useState(false);
    const [sleepInfo, setSleepInfo] = useState<SleepInfo | null>(null);
    const { date } = useDateStore();
    useEffect(() => {
        async function fetchData() {
            try {
                setIsLoading(true);
                const data = await authenticatedGetRequest(`/api/fitbit/sleep/${date}`);
                setSleepInfo(data);
            } catch (error) {
                console.error('睡眠情報の取得に失敗しました:', error);
            } finally {
                setIsLoading(false);
            }
        }

        fetchData();
    }, [date]);

    if (!sleepInfo) {
        return (
            <Card title="睡眠" icon={Icon}>
                <Loading isLoading={isLoading}/>
            </Card>
        );
    }
    const sleepMainInfo = {
        totalSleepTime: sleepInfo.totalMinutesAsleep,
        sleepCount: sleepInfo.totalSleepRecords,
    };
    const stage = sleepInfo.stages;
    const sleepStage = [`深い睡眠：${stage.deep}分`, `浅い睡眠：${stage.light}分`, `レム睡眠：${stage.rem}分`, `覚醒状態：${stage.wake}分`];

    return (
        <Card title="睡眠" icon={Icon}>
            <MainInnerCard totalSleepTime={sleepMainInfo.totalSleepTime} sleepCount={sleepMainInfo.sleepCount} />
            <SubInnerCard title="睡眠ステージ" sleepList={sleepStage} />
        </Card>
    );
}

interface MainInnerCardProps {
    totalSleepTime: number;
    sleepCount: number;
}

const MainInnerCard: React.FC<MainInnerCardProps> = ({ totalSleepTime, sleepCount }) => {
    return (
        <div className="rounded-xl bg-white px-4 py-4 shadow-sm">
            <p
                className={`${lusitana.className}
        truncate text-2xl pb-2`}
            >
                トータル睡眠時間：{totalSleepTime} 分
            </p>
            <p
                className={`${lusitana.className}
        truncate text-2xl`}
            >
                本日の睡眠回数：{sleepCount} 回
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