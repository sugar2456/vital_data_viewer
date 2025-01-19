"use client";

import { FaFire } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';
import { Card } from '@/app/ui/commons/card';

export function CaloriesCard() {
    const Icon = FaFire;
    const sleepInfo = {
        totalSleepTime: "8時間",
        sleepCount: 1,
    };
    return (
        <Card title="運動量" icon={Icon}>
            <MainInnerCard
                caloriesOut={2000}
                caloriesBMR={1500}
                steps={10000}
                distance={5}
                floors={5}
                elevation={100}
            />
            <SubInnerCard
                title="活動量"
                sedentaryMinutes={100}
                lightlyActiveMinutes={200}
                fairlyActiveMinutes={300}
                veryActiveMinutes={400}
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
                    座っている時間：{sedentaryMinutes}
                </li>
                <li
                    className={`${lusitana.className}
                flex justify-between`}
                >
                    低い活動量の時間：{lightlyActiveMinutes}
                </li>
                <li
                    className={`${lusitana.className}
                flex justify-between`}
                >
                    中程度の活動量の時間：{fairlyActiveMinutes}
                </li>
                <li
                    className={`${lusitana.className}
                flex justify-between`}
                >
                    高い活動量の時間：{veryActiveMinutes}
                </li>
            </ul>
        </div>
    );
};