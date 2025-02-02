import { UserRolesLabel } from '@/app/constants/users';

export function getRoleName(role: number): string {
    const userRole = UserRolesLabel.find((r) => r.id === role);
    return userRole ? userRole.name : '不正なロール';
}

export function getEmailVerifiedLabel(emailVerifiedAt: string | null): string {
    return emailVerifiedAt ? '認証済み' : '未認証';
}