"use client";

import { FaMobileAlt } from "react-icons/fa";
import { Card } from '@/app/ui/commons/card';
import devicesData from '@/app/ui/data/devices/devices.json';
import { lusitana } from '@/app/ui/fonts';
import { formatDateTimeToSeconds } from "@/app/lib/timeUtil";

export function DevicesCard() {
    const Icon = FaMobileAlt;
    const devicesInfo = devicesData.devices;
    return (
        <Card title="デバイス" icon={Icon}>
            {devicesInfo.map((device, index) => (
                <MainInnerCard
                    key={index}
                    batteryLevel={device.battery_level}
                    deviceName={device.device_version}
                    lastSyncTime={formatDateTimeToSeconds(device.last_sync_time)}
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