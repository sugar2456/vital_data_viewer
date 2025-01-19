"use client";

import { FaFire } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';
import { Card } from '@/app/ui/commons/card';
import activityData from '@/app/ui/data/activities/activity_summary.json';
export function CaloriesCard() {
    const Icon = FaFire;
    const caloriesInfo = activityData.activity;
    return (
        <Card title="運動量" icon={Icon}>
            <MainInnerCard
                caloriesOut={caloriesInfo.caloriesOut}
                caloriesBMR={caloriesInfo.caloriesBMR}
                steps={caloriesInfo.steps}
                distance={caloriesInfo.distances[0].distance}
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