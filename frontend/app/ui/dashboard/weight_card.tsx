"use client";

import React, { useEffect, useState } from 'react';
import { FaWeight } from "react-icons/fa";
import { lusitana } from '@/app/ui/fonts';
import { Card } from '@/app/ui/commons/card';
import { BodyInfo } from '@/app/types/body_info';
import { getRequest } from '@/app/lib/httpUtil';
import { Loading } from '../commons/loadings';

export function WeightCard() {
    const Icon = FaWeight;
    const [bodyInfo, setBodyInfo] = useState<BodyInfo | null>(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRequest("http://localhost:8000/api/fitbit/weight/1/2024-12-15");
                setBodyInfo(data);
            } catch (error) {
                console.error('体重情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, []);

    if (!bodyInfo) {
        return (
            <Card title="体重" icon={Icon}>
                <Loading />
            </Card>
        );
    }
    
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