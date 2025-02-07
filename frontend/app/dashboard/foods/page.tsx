"use client";
import { useAuthRedirect } from "@/app/hooks/useAuthRedirect";
import FoodsList from "@/app/ui/foods/foods_list";

export default function Page() {
    useAuthRedirect();
    return (
        <div className="flex gap-4">
            <FoodsList />
        </div>
    );
}