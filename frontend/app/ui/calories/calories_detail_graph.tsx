"use client";
import React, { useEffect, useState } from 'react';
import { authenticatedGetRequest } from '@/app/lib/common/apiClient';
import { useDateStore } from '@/app/store/viewStore';
import { FaFire } from 'react-icons/fa';
import { ChartData, Chart as ChartJS, ChartOptions, registerables, Point } from 'chart.js';

import { Chart } from 'react-chartjs-2';
import { Dataset } from '@/app/types/calories_detail';
import { WeightDetail, WeightPeriod } from '@/app/types/weight';
import 'chartjs-adapter-date-fns';

ChartJS.register(...registerables);

const options: ChartOptions<'line' | 'bar'> = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'top' as const,
        },
    },
    scales: {
        x: {
            type: 'time',
            time: {
                unit: 'day',
            },
            title: {
                display: true,
                text: '日付',
            },
        },
        'y-calories': {
            type: 'linear',
            position: 'right',
            beginAtZero: true,
            title: {
                display: true,
                text: 'カロリー(kcal)',
            },
        },
        'y-weight': {
            type: 'linear',
            position: 'left',
            beginAtZero: true,
            title: {
                display: true,
                text: '体重(kg)',
            },
        },
        'y-fat': {
            type: 'linear',
            position: 'left',
            beginAtZero: true,
            title: {
                display: true,
                text: '体脂肪率(%)',
            },
        },
    },
};

export function CaloriesDetailGraph() {
    const Icon = FaFire;
    const [consumedCalories, setConsumedCalories] = useState<Dataset[] | null>(null);
    const [intakedCalories, setIntakedCalories] = useState<Dataset[] | null>(null);
    const [totalCalories, setTotalCalories] = useState<Dataset[] | null>(null);
    const [weightDetails, setWeightDetails] = useState<WeightDetail[] | null>(null);
    const { date } = useDateStore();

    useEffect(() => {
        async function fetchData() {
            try {
                const currentDate = new Date(date);
                const oneMonthAgo = new Date(currentDate.setMonth(currentDate.getMonth() - 1));
                const formattedDate = oneMonthAgo.toISOString().split('T')[0];

                const data = await authenticatedGetRequest(`http://localhost:8000/api/fitbit/calories/${formattedDate}/${date}`);
                setConsumedCalories(data.consumed_calories_period);
                setIntakedCalories(data.intaked_calories_period);
                setTotalCalories(data.total_calories_period);

                const weightData = await authenticatedGetRequest(`http://localhost:8000/api/fitbit/weight/${formattedDate}/${date}`);
                setWeightDetails(weightData.weight_list);
            } catch (error) {
                console.error('活動情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, [date]);

    const data: ChartData<'line' | 'bar', Point[]> = {
        labels: totalCalories?.map((data) => data.dateTime) || [],
        datasets: [
            {
                type: 'bar' as const,
                label: '摂取カロリー',
                data: intakedCalories?.map((entry: Dataset) => {
                    return {
                        x: new Date(`${entry.dateTime}`).getTime(),
                        y: +entry.value,
                    } as Point;
                }) || [],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1,
                yAxisID: 'y-calories'
            },
            {
                type: 'bar' as const,
                label: '消費カロリー',
                data: consumedCalories?.map((entry: Dataset) => {
                    return {
                        x: new Date(`${entry.dateTime}`).getTime(),
                        y: +entry.value,
                    } as Point;
                }) || [],
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1,
                yAxisID: 'y-calories'
            },
            {
                type: 'bar' as const,
                label: '総合カロリー',
                data: totalCalories?.map((entry: Dataset) => {
                    return {
                        x: new Date(`${entry.dateTime}`).getTime(),
                        y: +entry.value,
                    } as Point;
                }) || [],
                backgroundColor: 'rgba(255, 206, 86, 0.2)',
                borderColor: 'rgba(255, 206, 86, 1)',
                borderWidth: 1,
                yAxisID: 'y-calories'
            },
            {
                type: 'line',
                label: '体重',
                data: weightDetails?.map((item: WeightDetail) => {
                    return {
                        x: new Date(`${item.date}`).getTime(),
                        y: item.weight,
                    } as Point;
                }) || [],
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
                borderWidth: 1,
                yAxisID: 'y-weight'
            },
            {
                type: 'line',
                label: '体脂肪率',
                data: weightDetails?.map((item: WeightDetail) => {
                    return {
                        x: new Date(`${item.date}`).getTime(),
                        y: item.fat,
                    } as Point;
                }) || [],
                backgroundColor: 'rgba(102, 240, 60, 0.4)',
                borderColor: 'rgba(102, 240, 60)',
                borderWidth: 1,
                yAxisID: 'y-fat'
            }
        ],
    };

    return (
        <div className="rounded-xl bg-gray-50 shadow-sm p-2" style={{ height: '90vh' }}>
            <div className="flex p-4">
                {Icon ? <Icon className="h-5 w-5 text-gray-700" /> : null}
                <h3 className="ml-2 text-sm font-medium">活動情報</h3>
            </div>
            <div className="h-full bg-white" style={{ height: 'calc(90vh - 4rem)' }}>
                <Chart type='bar' data={data} options={options} />
            </div>
        </div>
    );
}