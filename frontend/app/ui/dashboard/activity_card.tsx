"use client";

import React, { useEffect, useState } from 'react';
import { FaFire } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';
import { Card } from '@/app/ui/commons/card';
import { getRequest } from '@/app/lib/httpUtil';
import { ActivityInfo } from '@/app/types/activity_info';
import { Loading } from '../commons/loadings';
import { useDateStore } from '@/app/store/viewStore';

export function ActivityCard() {
    const Icon = FaFire;
    const [caloriesInfo, setCaloriesInfo] = useState<ActivityInfo | null>(null);
    const { date } = useDateStore();
    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRequest(`http://localhost:8000/api/fitbit/activity/1/${date}`);
                setCaloriesInfo(data.activity);
            } catch (error) {
                console.error('カロリー情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, []);

    if (!caloriesInfo) {
        return (
            <Card title="運動量" icon={Icon}>
                <Loading />
            </Card>
        );
    }

    const totalDistance = Array.isArray(caloriesInfo.distances)
        ? caloriesInfo.distances.filter((distance) => distance.activity === "total")[0]?.distance
        : 0;
    return (
        <Card title="運動量" icon={Icon}>
            <MainInnerCard
                caloriesOut={caloriesInfo.caloriesOut}
                caloriesBMR={caloriesInfo.caloriesBMR}
                steps={caloriesInfo.steps}
                distance={totalDistance}
                floors={caloriesInfo.floors}
                elevation={caloriesInfo.elevation}
            />
            <SubInnerCard
                title="活動量"
                sedentaryMinutes={caloriesInfo.sedentaryMinutes}
                lightlyActiveMinutes={caloriesInfo.lightlyActiveMinutes}
                fairlyActiveMinutes={caloriesInfo.fairlyActiveMinutes}
                veryActiveMinutes={caloriesInfo.veryActiveMinutes}
            />
        </Card>
    );
}

interface MainInnerCardProps {
    /**
     * トータル消費カロリー
     */
    caloriesOut: number;
    /**
     * 基礎代謝カロリー
     */
    caloriesBMR: number;
    /**
     * 歩数
     */
    steps: number;
    /**
     * 移動距離
    */
    distance: number;
    /**
     * 上昇した階数
     */
    floors: number;
    /**
     * 上昇した標高
     */
    elevation: number;
}

const MainInnerCard: React.FC<MainInnerCardProps> = ({
    caloriesOut,
    caloriesBMR,
    steps,
    distance,
    floors,
    elevation,
}) => {
    return (
        <div className="rounded-xl bg-white px-4 py-4 shadow-sm">
            <ul>
                <li
                    className={`${lusitana.className}
                truncate text-l`}
                >
                    トータル消費カロリー：{caloriesOut} kcal
                </li>
                <li
                    className={`${lusitana.className}
                truncate text-l`}
                >
                    歩数：{steps} 歩
                </li>
                <li
                    className={`${lusitana.className}
                truncate text-l`}
                >
                    移動距離：{distance} km
                </li>
            </ul>
        </div>
    );
}

interface SubInnerCardProps {
    title: string;
    /**
     * 座っている時間
     */
    sedentaryMinutes: number;
    /**
     * 低い活動量の時間
     */
    lightlyActiveMinutes: number;
    /**
     * 中程度の活動量の時間
     */
    fairlyActiveMinutes: number;
    /**
     * 高い活動量の時間
     */
    veryActiveMinutes: number;
}

const SubInnerCard: React.FC<SubInnerCardProps> = ({
    title,
    sedentaryMinutes,
    lightlyActiveMinutes,
    fairlyActiveMinutes,
    veryActiveMinutes,
}) => {
    return (
        <div className="rounded-xl bg-white px-4 py-4 shadow-sm">
            <h3 className="text-lg font-semibold mb-2">{title}</h3>
            <ul className="pl-4">
                <li
                    className={`${lusitana.className}
                flex justify-between`}
                >
                    座っている時間：{sedentaryMinutes} 分
                </li>
                <li
                    className={`${lusitana.className}
                flex justify-between`}
                >
                    低い活動量の時間：{lightlyActiveMinutes} 分
                </li>
                <li
                    className={`${lusitana.className}
                flex justify-between`}
                >
                    中程度の活動量の時間：{fairlyActiveMinutes} 分
                </li>
                <li
                    className={`${lusitana.className}
                flex justify-between`}
                >
                    高い活動量の時間：{veryActiveMinutes} 分
                </li>
            </ul>
        </div>
    );
};