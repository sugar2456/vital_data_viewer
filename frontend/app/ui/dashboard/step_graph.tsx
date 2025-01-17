"use client";

import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import 'chartjs-adapter-date-fns';
import stepsData from '@/app/ui/data/step/steps_intraday.json';
import { ChartOptions } from 'chart.js';
import { FaWalking } from 'react-icons/fa';

Chart.register(TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

const StepsChart: React.FC = () => {
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

    const Icon = FaWalking;
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