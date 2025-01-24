"use client";

import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import 'chartjs-adapter-date-fns';
import heartRateData from '@/app/ui/data/heart_rate/heart_rate.json';
import { ChartOptions } from 'chart.js';
import { FaHeart } from 'react-icons/fa';
import { HeartRateInfo } from '@/app/types/heart_rate_info';
import { getRequest } from '@/app/lib/httpUtil';
import { Card } from '../commons/card';
import { Loading } from '../commons/loadings';
import { useDateStore } from '@/app/store/viewStore';

Chart.register(TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

const HeartRateChart: React.FC = () => {
    const Icon = FaHeart;
    const [heartRateData, setHeartRateData] = useState<HeartRateInfo | null>(null);
    const { date } = useDateStore();
    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRequest(`http://localhost:8000/api/fitbit/heart/1/${date}/15`);
                setHeartRateData(data);
            } catch (error) {
                console.error('心拍数情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, [date]);

    if (!heartRateData) {
        return (
            <Card title="1日の心拍数" icon={Icon}>
                <Loading />
            </Card>
        );
    }
    // データの整形
    const times = heartRateData.heart_rate_intraday.map((entry: { time: string }) => {
        return new Date(`${date}T${entry.time}+09:00`);
    });
    const values = heartRateData.heart_rate_intraday.map((entry: { value: number }) => entry.value);

    const data = {
        labels: times,
        datasets: [
            {
                label: 'bpm',
                data: values,
                fill: false,
                backgroundColor: 'rgba(255, 77, 77,0.4)',
                borderColor: 'rgba(255,90,77,1)',
            },
        ],
    };

    const options: ChartOptions<'line'> = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'hour',
                    tooltipFormat: 'HH:mm',
                    displayFormats: {
                        hour: 'HH:mm',
                    },
                },
                min: new Date(`${date}T00:00:00`).getTime(),
                max: new Date(`${date}T23:59:59`).getTime(),
            },
            y: {
                beginAtZero: true,
            },
        },
    };

    return (
        <div className="rounded-xl bg-gray-50 shadow-sm p-2">
            <div className="flex p-4">
                {Icon ? <Icon className="h-5 w-5 text-gray-700" /> : null}
                <h3 className="ml-2 text-sm font-medium">1日の心拍数</h3>
            </div>
            <div className="h-auto bg-white">
                <Line data={data} options={options} />
            </div>
        </div>
    );
};

export default HeartRateChart;