"use client";

import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import 'chartjs-adapter-date-fns';
import { toZonedTime } from 'date-fns-tz';
import stepsData from '@/app/ui/data/step/steps_intraday.json';
import { ChartOptions } from 'chart.js';

Chart.register(TimeScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

const StepsChart: React.FC = () => {
    const timeZone = 'Asia/Tokyo';

    // データの整形
    const times = stepsData.steps_intraday.map((entry: { time: string }) => {
      const utcDate = new Date(`1970-01-01T${entry.time}Z`);
      return toZonedTime(utcDate, timeZone);
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
        //   adapters: {
        //     date: {
        //       locale: 'ja-JP',
        //     },
        //   },
        },
        y: {
          beginAtZero: true,
        },
      },
    };


    return (
        <div className="p-4 bg-white border border-gray-200 rounded-lg shadow-md">
            <h2 className="text-lg font-semibold mb-4">Steps Intraday</h2>
            <Line data={data} options={options} />
        </div>
    );
};

export default StepsChart;