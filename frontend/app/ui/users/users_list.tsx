"use client";
import React, { useEffect, useState } from 'react';
import { useUsersViewStore } from '@/app/store/usersViewStore';
import { FaPlus } from 'react-icons/fa';
import { getRoleName, getEmailVerifiedLabel } from '@/app/lib/users/usersUtil';
import RegisterUserDialog from './register_user_dialog';

const UsersList: React.FC = () => {
    const { users, fetchUsers } = useUsersViewStore();
    const [isModalOpen, setIsModalOpen] = useState(false);

    useEffect(() => {
        fetchUsers();
    }, [fetchUsers]);

    const handleOpenModal = () => {
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
    };
    
    if (!users || users.length === 0) {
        return <div>No users found.</div>;
    }

    return (
        <div className="container mx-auto p-4 bg-white rounded shadow-sm">
            <div className='flex justify-between items-center'>
                <h2 className='text-xl font-bold'>ユーザー一覧</h2>
                <button
                    className="bg-gray text-gray-500 border border-gray-500 rounded-full p-2 m-2 shadow hover:bg-blue-100 focus:outline-none"
                    onClick={handleOpenModal}
                >
                    <FaPlus className="h-5 w-5" />
                </button>
            </div>
            <table className='w-full'>
                <thead className='bg-blue-100'>
                    <tr>
                        <th className='p-2'>ID</th>
                        <th className='p-2'>名前</th>
                        <th className='p-2'>メールアドレス</th>
                        <th className='p-2'>メール認証</th>
                        <th className='p-2'>ロール</th>
                        <th className='p-2'>作成日時</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((user) => {
                        return (
                            <tr key={user.id} className='border-b border-gray-200'>
                                <td className='p-2 text-center'>{user.id}</td>
                                <td className='p-2 text-center'>{user.name}</td>
                                <td className='p-2 text-center'>{user.email}</td>
                                <td className='p-2 text-center'>{getEmailVerifiedLabel(user.email_verified_at)}</td>
                                <td className='p-2 text-center'>{getRoleName(user.role)}</td>
                                <td className='p-2 text-center'>{user.created_at}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
            <RegisterUserDialog isOpen={isModalOpen} onClose={handleCloseModal} />
        </div>
    );
};

export default UsersList;