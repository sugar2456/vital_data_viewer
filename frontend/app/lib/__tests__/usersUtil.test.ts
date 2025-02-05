import { getRoleName, getEmailVerifiedLabel } from '@/app/lib/users/usersUtil';

describe('getRoleName', () => {
    it('should return role name', () => {
        const roleAdminName = getRoleName(1);
        expect(roleAdminName).toBe('管理者');

        const roleUserName = getRoleName(2);
        expect(roleUserName).toBe('ユーザー');
    });

    it('should return "不正なロール" for invalid role', () => {
        const roleName = getRoleName(99);
        expect(roleName).toBe('不正なロール');
    });
});

describe('getEmailVerifiedLabel', () => {
    it('should return "認証済み" for emailVerifiedAt', () => {
        const emailVerifiedLabel = getEmailVerifiedLabel('2025-01-22T12:34:32.000');
        expect(emailVerifiedLabel).toBe('認証済み');
    });

    it('should return "未認証" for null emailVerifiedAt', () => {
        const emailVerifiedLabel = getEmailVerifiedLabel(null);
        expect(emailVerifiedLabel).toBe('未認証');
    });
});