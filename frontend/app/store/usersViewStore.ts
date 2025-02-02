import { create } from 'zustand';
import { User } from '@/app/types/users';
import { getRequest, postRequest } from '@/app/lib/httpUtil';

interface UsersViewState {
    users: User[];
    fetchUsers: () => Promise<void>;
    addUser: (user: Partial<User>) => Promise<void>;
    setUsers: (users: User[]) => void;
}

export const useUsersViewStore = create<UsersViewState>((set) => ({
    users: [],
    fetchUsers: async () => {
        try {
            const data = await getRequest('http://localhost:8000/api/users');
            set({ users: data.users });
        } catch (error) {
            console.error('ユーザー情報の取得に失敗しました:', error);
        }
    },
    addUser: async (user) => {
        try {
            const newUser = await postRequest('http://localhost:8000/api/users/create', user);
            console.log('Sending user data:', newUser);
            set((state) => ({ users: [...state.users, newUser.user] }));
        } catch (error) {
            console.error('ユーザーの追加に失敗しました:', error);
        }
    },
    setUsers: (users) => set({ users }),
}));