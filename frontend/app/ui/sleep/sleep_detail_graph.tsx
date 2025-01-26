"use client";

import React, { useEffect, useState } from 'react';
import { getRequest } from '@/app/lib/httpUtil';
import { Loading } from '../commons/loadings';
// import sleep_data from '@/app/ui/data/sleep/sleep_detail.json';
import { SleepDetail, SleepData } from '@/app/types/sleep_detail';
import { Line } from 'react-chartjs-2';
import { Chart, TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import 'chartjs-adapter-date-fns';
import { ChartOptions } from 'chart.js';
import { useDateStore } from '@/app/store/viewStore';
import { FaMoon } from 'react-icons/fa';

Chart.register(TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

export function SleepDetailGraph() {
    const Icon = FaMoon;
    const [sleepInfo, setSleepInfo] = useState<SleepData[][] | null>(null);
    const { date } = useDateStore();
    const sleep_data_list: SleepData[][] = [];

    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRequest(`http://localhost:8000/api/fitbit/sleep/detail/1/${date}`);
                data.sleep.map((entry: SleepDetail) => {
                    const sleep_dataset: SleepData[] = entry.levels.data;
                    sleep_data_list.push(sleep_dataset);
                });
                setSleepInfo(sleep_data_list);
            } catch (error) {
                console.error('睡眠情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, [date]);

    const sleep_level_defines = ['deep', 'light', 'rem', 'wake', 'asleep', 'restless', 'awake'];
    let count = sleepInfo ? sleepInfo.length : 0;
    const sleepGraphBorderColors: { [key: number]: string } = {
        1: 'rgba(75,192,192,0.4)',
        2: 'rgba(94, 197, 95, 0.4)',
        3: 'rgba(185, 215, 52, 0.4)',
        4: 'rgba(189, 127, 108, 0.4)',
        5: 'rgba(205, 96, 96, 0.4)',
        6: 'rgba(114, 73, 185, 0.4)',

    };
    const sleepGraphColors: { [key: number]: string } = {
        1: 'rgba(75,192,192,1)',
        2: 'rgba(94, 197, 95, 1)',
        3: 'rgba(185, 215, 52, 1)',
        4: 'rgba(189, 127, 108, 1)',
        5: 'rgba(205, 96, 96, 1)',
        6: 'rgba(114, 73, 185, 1)',
    };
    const datasets = sleepInfo?.map((entry: SleepData[]) => {
        const dataItem = entry.flatMap((data: SleepData) => {
            const startTime = new Date(data.dateTime);
            const endTime = new Date(startTime.getTime() + data.seconds * 1000);
            return [
                {
                    y: sleep_level_defines.indexOf(data.level),
                    x: startTime,
                },
                {
                    y: sleep_level_defines.indexOf(data.level),
                    x: endTime,
                },
            ];
        });
        const ret = {
            label: `${count}回目の睡眠`,
            data: dataItem,
            fill: false,
            backgroundColor: sleepGraphBorderColors[count],
            borderColor: sleepGraphColors[count],
        };
        count--;
        return ret;
    });

    const data = {
        datasets: datasets  || [],
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
                ticks: {
                    callback: function(tickValue: string | number) {
                        const labels =['deep', 'light', 'rem', 'wake', 'awake', 'restless', 'asleep'];
                        return sleep_level_defines[tickValue as number];
                    }
                },
            },
        },
        plugins: {
            tooltip: {
                callbacks:{
                    label: function(context: any) {
                        const labels = ['deep', 'light', 'rem', 'wake', 'awake', 'restless', 'asleep'];
                        return sleep_level_defines[context.parsed.y as number];
                    }
                }
            }
        }
    };

    return (
        <div className="rounded-xl bg-gray-50 shadow-sm p-2" style={{ height: '50vh' }}>
            <div className="flex p-4">
                {Icon ? <Icon className="h-5 w-5 text-gray-700" /> : null}
                <h3 className="ml-2 text-sm font-medium">睡眠情報</h3>
            </div>
            <div className="h-full bg-white" style={{ height: 'calc(50vh - 4rem)' }}>
                <Line data={data} options={options} />
            </div>
        </div>
    );
}