"use client";

import { IconType } from "react-icons/lib";

export function Card({
    title,
    icon,
    children
}: {
    title: string;
    icon: IconType;
    children: React.ReactNode[];
}) {
    const Icon = icon;

    return (
        <div className="rounded-xl bg-gray-50 p-2 shadow-sm">
            <div className="flex p-4">
                {Icon ? <Icon className="h-5 w-5 text-gray-700" /> : null}
                <h3 className="ml-2 text-sm font-medium">{title}</h3>
            </div>
            <div className="flex flex-col gap-2">
                {...children}
            </div>
        </div>
    );
}
