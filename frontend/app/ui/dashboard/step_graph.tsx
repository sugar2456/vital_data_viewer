"use client";
import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import 'chartjs-adapter-date-fns';
import stepsData from '@/app/ui/data/step/steps_intraday.json';
import { ChartOptions } from 'chart.js';
import { FaWalking } from 'react-icons/fa';
import { StepInfo } from '@/app/types/step_info';
import { getRequest } from '@/app/lib/httpUtil';
import { Card } from '../commons/card';
import { Loading } from '../commons/loadings';

Chart.register(TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

const StepsChart: React.FC = () => {
    const Icon = FaWalking;
    const [stepsData, setStepsData] =useState<StepInfo | null>(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRequest("http://localhost:8000/api/fitbit/steps/intraday/1/2024-12-02/15");
                setStepsData(data);
            } catch (error) {
                console.error('歩数情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, []);

    if (!stepsData) {
        return (
            <Card title="1日の歩数" icon={Icon}>
                <Loading />
            </Card>
        );
    }
    // データの整形
    const times = stepsData.steps_intraday.map((entry: { time: string }) => {
        return new Date(`1970-01-01T${entry.time}+09:00`);
    });
    const values = stepsData.steps_intraday.map((entry: { value: number }) => entry.value);

    const data = {
        labels: times,
        datasets: [
            {
                label: 'Steps',
                data: values,
                fill: false,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
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
                <h3 className="ml-2 text-sm font-medium">1日の歩数</h3>
            </div>
            <div className="h-auto bg-white">
                <Line data={data} options={options} />
            </div>
        </div>
    );
};

export default StepsChart;