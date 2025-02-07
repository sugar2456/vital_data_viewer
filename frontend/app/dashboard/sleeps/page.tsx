"use client";
import { useAuthRedirect } from "@/app/hooks/useAuthRedirect";
import { SleepDetailGraph } from "@/app/ui/sleep/sleep_detail_graph";

export default function Page() {
    useAuthRedirect();
    return <SleepDetailGraph />;
}