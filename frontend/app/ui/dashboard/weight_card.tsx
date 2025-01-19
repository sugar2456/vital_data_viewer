"use client";

import { FaWeight } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';
import { Card } from '@/app/ui/commons/card';
import bodyRowData from '@/app/ui/data/weight/weight.json';
export function WeightCard() {
    const Icon = FaWeight;
    const bodyInfo = {
        weight: bodyRowData.weight,
        fat: bodyRowData.fat,
        bmi: bodyRowData.bmi,
    };
    return (
        <Card title="体重" icon={Icon}>
            <MainInnerCard weight={bodyInfo.weight} fat={bodyInfo.fat} bmi={bodyInfo.bmi}/>
        </Card>
    );
}

interface MainInnerCardProps {
    weight: number;
    fat: number;
    bmi: number;
}

const MainInnerCard: React.FC<MainInnerCardProps> = ({ weight, fat, bmi }) => {
    return (
        <div className="rounded-xl bg-white px-4 py-4 shadow-sm">
            <ul>
                <li
                    className={`${lusitana.className}
                truncate text-2xl pb-2`}
                >
                    体重：{weight}
                </li>
                <li
                    className={`${lusitana.className}
                truncate text-2xl pb-2`}
                >
                    体脂肪：{fat}%
                </li>
                <li
                    className={`${lusitana.className}
                truncate text-2xl`}
                >
                    bmi：{bmi}
                </li>
            </ul>
        </div>
    );
}