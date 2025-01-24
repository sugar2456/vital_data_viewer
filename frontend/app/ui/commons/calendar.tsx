"use client"
import React, { useState } from 'react';
import { FaCalendar } from "react-icons/fa";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { registerLocale } from 'react-datepicker';
import {ja} from 'date-fns/locale/ja';

// 日本語ロケールを登録
registerLocale('ja', ja);

export default function Calendar() {
    const Icon = FaCalendar;
    const [selectedDate, setSelectedDate] = useState<Date | null>(new Date());

    return (
        <DatePicker
            selected={selectedDate}
            onChange={(date: Date | null) => setSelectedDate(date)}
            inline
            dateFormat="yyyy/MM/dd"
            locale="ja"
        />
    );
}