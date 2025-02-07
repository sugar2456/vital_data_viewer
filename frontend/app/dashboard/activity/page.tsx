"use client";
import { useAuthRedirect } from "@/app/hooks/useAuthRedirect";
import { ActivityDetailGraph } from "@/app/ui/activity/activity_detail_graph";

export default function Page() {
    useAuthRedirect();
    return <ActivityDetailGraph />;
}