"use client";
import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import 'chartjs-adapter-date-fns';
import { ChartOptions } from 'chart.js';
import { FaWalking } from 'react-icons/fa';
import { StepInfo } from '@/app/types/step_info';
import { authenticatedGetRequest } from '@/app/lib/common/apiClient';
import { Card } from '../commons/card';
import { Loading } from '../commons/loadings';
import { useDateStore } from '@/app/store/viewStore';

Chart.register(TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

const StepsChart: React.FC = () => {
    const Icon = FaWalking;
    const [isLoading, setIsLoading] = useState(false);
    const [stepsData, setStepsData] =useState<StepInfo | null>(null);
    const { date } = useDateStore();
    useEffect(() => {
        async function fetchData() {
            try {
                setIsLoading(true);
                const data = await authenticatedGetRequest(`/api/fitbit/steps/intraday/${date}/15`);
                setStepsData(data);
            } catch (error) {
                console.error('歩数情報の取得に失敗しました:', error);
            } finally {
                setIsLoading(false);
            }
        }

        fetchData();
    }, [date]);

    if (!stepsData) {
        return (
            <Card title="1日の歩数" icon={Icon}>
                <Loading isLoading={isLoading}/>
            </Card>
        );
    }
    // データの整形
    const times = stepsData.steps_intraday.map((entry: { time: string }) => {
        return new Date(`${date}T${entry.time}+09:00`);
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
                <h3 className="ml-2 text-sm font-medium">1日の歩数</h3>
            </div>
            <div className="h-auto bg-white">
                <Line data={data} options={options} />
            </div>
        </div>
    );
};

export default StepsChart;