"use client";

import React, { useEffect, useState } from 'react';
import { FaMobileAlt } from "react-icons/fa";
import { Card } from '@/app/ui/commons/card';
import { lusitana } from '@/app/ui/fonts';
import { formatDateTimeToSeconds } from "@/app/lib/common/timeUtil";
import { authenticatedGetRequest } from '@/app/lib/common/apiClient';
import { Loading } from '../commons/loadings';
import { DeviceInfo } from '@/app/types/device_info';

export function DevicesCard() {
    const Icon = FaMobileAlt;
    const [devicesInfo, setDevicesInfo] = useState<DeviceInfo[] | null>(null);

    useEffect(() => {
        async function fetchData() {
            try {
                const data = await authenticatedGetRequest("http://localhost:8000/api/fitbit/devices");
                const bindDevicesInfo: DeviceInfo[] = data.devices.map((device: any) => {
                    return {
                        id: device.id,
                        batteryLevel: device.battery_level,
                        deviceName: device.device_version,
                        lastSyncTime: device.last_sync_time,
                    };
                });
                setDevicesInfo(bindDevicesInfo);
            } catch (error) {
                console.error('デバイス情報の取得に失敗しました:', error);
            }
        }
        fetchData();
    }, []);

    if (!devicesInfo) {
        return (
            <Card title="デバイス" icon={Icon}>
                <Loading />
            </Card>
        );
    }
    return (
        <Card title="デバイス" icon={Icon}>
            {devicesInfo.map((device, index) => (
                <MainInnerCard
                    key={index}
                    batteryLevel={device.batteryLevel}
                    deviceName={device.deviceName}
                    lastSyncTime={formatDateTimeToSeconds(device.lastSyncTime)}
                />
            ))}
        </Card>
    );
}

interface MainInnerCardProps {
    batteryLevel: string;
    deviceName: string;
    lastSyncTime: string;
}

const MainInnerCard: React.FC<MainInnerCardProps> = ({
    batteryLevel,
    deviceName,
    lastSyncTime,
}) => {
    return (
        <div className="rounded-xl bg-white px-4 py-4 shadow-sm">
            <ul>
                <li
                    className={`${lusitana.className}
                truncate text-l`}
                >
                    製品名：{deviceName}
                </li>
                <li
                    className={`${lusitana.className}
                truncate text-l`}
                >
                    バッテリー残量：{batteryLevel}
                </li>
                <li
                    className={`${lusitana.className}
                truncate text-l`}
                >
                    最終同期日時：{lastSyncTime}
                </li>
            </ul>
        </div>
    );
}