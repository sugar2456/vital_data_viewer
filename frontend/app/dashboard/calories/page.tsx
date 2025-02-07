"use client";
import { useAuthRedirect } from "@/app/hooks/useAuthRedirect";
import { CaloriesDetailGraph } from "@/app/ui/calories/calories_detail_graph";

export default function Page() {
    useAuthRedirect();
    return <CaloriesDetailGraph />;
}