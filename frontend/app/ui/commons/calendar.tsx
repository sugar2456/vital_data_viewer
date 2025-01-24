"use client"
import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { registerLocale } from 'react-datepicker';
import {ja} from 'date-fns/locale/ja';
import { useDateStore } from '@/app/store/viewStore';

// 日本語ロケールを登録
registerLocale('ja', ja);

export default function Calendar() {
    const { date, setDate } = useDateStore();
    const selectedDate = new Date(date);
    const today = new Date();
    return (
        <DatePicker
            selected={selectedDate}
            onChange={(date: Date | null) => {
                if (date) {
                    setDate(date.toISOString().split('T')[0]);
                }
            }}
            inline
            dateFormat="yyyy/MM/dd"
            locale="ja"
            maxDate={today}
        />
    );
}