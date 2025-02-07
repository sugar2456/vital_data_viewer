"use client";
import { useAuthRedirect } from "@/app/hooks/useAuthRedirect";
import UsersList from "@/app/ui/users/users_list";
export default function Page() {
    useAuthRedirect();
    return <UsersList />;
}