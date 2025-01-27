"use client";

import React, { useEffect, useState } from 'react';
import { getRequest } from '@/app/lib/httpUtil';
import { Loading } from '../commons/loadings';
import { Dataset, CaloriesDataset } from '@/app/types/activity_detail';
import { Chart, registerables, ChartData, Point } from 'chart.js';
import 'chartjs-adapter-date-fns';
import { ChartOptions } from 'chart.js';
import { useDateStore } from '@/app/store/viewStore';
import { FaFire } from 'react-icons/fa';
import { Chart as ChartJS } from 'react-chartjs-2';

Chart.register(...registerables);

export function ActivityDetailGraph() {
    const Icon = FaFire;
    const [calories, setCalories] = useState<CaloriesDataset[] | null>(null);
    const [steps, setSteps ] = useState<Dataset[] | null>(null);
    const [distance, setDistance] = useState<Dataset[] | null>(null);
    const [heartRate, setHeartRate] = useState<Dataset[] | null>(null);
    const { date } = useDateStore();

    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRequest(`http://localhost:8000/api/fitbit/calories-step/intraday/1/${date}/1`);
                setCalories(data.calories_intraday);
                setSteps(data.step_intraday);
                setDistance(data.distance_intraday);
                setHeartRate(data.heart_rate_intraday);
            } catch (error) {
                console.error('睡眠情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, [date]);

    const data: ChartData<'line' | 'bar'> = {
        datasets: [
            {
                type: 'line',
                label: 'カロリー',
                data: calories?.map((entry: CaloriesDataset) => {
                    return {
                        x: new Date(`${date}T${entry.time}+09:00`).getTime(),
                        y: entry.value,
                    } as Point;
                }) || [],
                borderColor: 'rgb(255, 228, 72)',
                backgroundColor: 'rgba(255, 228, 72, 0.4)',
                yAxisID: 'y-calories',
            }, {
                type: 'line',
                label: '歩数',
                data: steps?.map((entry: Dataset) => {
                    return {
                        x: new Date(`${date}T${entry.time}+09:00`).getTime(),
                        y: entry.value,
                    } as Point;
                }) || [],
                borderColor: 'rgb(75,192,192)',
                backgroundColor: 'rgba(75,192,192,0.4)',
                yAxisID: 'y-steps',
            }, {
                type: 'bar',
                label: '距離',
                data: distance?.map((entry: Dataset) => {
                    return {
                        x: new Date(`${date}T${entry.time}+09:00`).getTime(),
                        y: entry.value * 1000,
                    } as Point;
                }) || [],
                borderColor: 'rgb(249, 127, 74)',
                backgroundColor: 'rgba(248, 2, 2, 0.4)',
                yAxisID: 'y-distance',
            }, {
                type: 'line',
                label: '心拍数',
                data: heartRate?.map((entry: Dataset) => {
                    return {
                        x: new Date(`${date}T${entry.time}+09:00`).getTime(),
                        y: entry.value,
                    } as Point;
                }) || [],
                borderColor: 'rgb(185, 215, 52)',
                backgroundColor: 'rgba(185, 215, 52, 0.4)',
                yAxisID: 'y-heart-rate',
            }
        ],
    };

    const options: ChartOptions<'line' | 'bar'> = {
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
            'y-calories': { // カロリー用のY軸を定義
                type: 'linear',
                position: 'right',
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'カロリー(kcal/15分)',
                },
            },
            'y-distance': { // 距離用のY軸を定義
                type: 'linear',
                position: 'right',
                beginAtZero: true,
                title: {
                    display: true,
                    text: '距離(m/分)',
                },
            },
            'y-steps': { // 歩数用のY軸を定義
                type: 'linear',
                position: 'left',
                beginAtZero: true,
                title: {
                    display: true,
                    text: '歩数(歩/分)',
                },
            },
            'y-heart-rate': { // 心拍数用のY軸を定義
                type: 'linear',
                position: 'left',
                beginAtZero: true,
                title: {
                    display: true,
                    text: '心拍数(bpm)',
                },
            },
        },
        plugins: {
            tooltip: {
                callbacks: {
                    label: function (context) {
                        let label = context.dataset.label || '';
                        if (label) {
                            label += ': ';
                        }
                        if (context.parsed.y !== null) {
                            label += context.parsed.y;
                        }
                        return label;
                    },
                },
            },
        },
    };

    return (
        <div className="rounded-xl bg-gray-50 shadow-sm p-2" style={{ height: '90vh' }}>
            <div className="flex p-4">
                {Icon ? <Icon className="h-5 w-5 text-gray-700" /> : null}
                <h3 className="ml-2 text-sm font-medium">睡眠情報</h3>
            </div>
            <div className="h-full bg-white" style={{ height: 'calc(90vh - 4rem)' }}>
                <ChartJS type='bar' data={data} options={options} />
            </div>
        </div>
    );
}