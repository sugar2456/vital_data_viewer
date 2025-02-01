"use client";
import React, { useEffect, useState } from 'react';
import { getRequest } from '@/app/lib/httpUtil';
import { FaPlus } from 'react-icons/fa';
import { User } from '@/app/types/users';
import Dialog from '@/app/ui/commons/dialog';
import RegisterUserDialog from './register_user_dialog';

const UsersList: React.FC = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [users, setUsers] = useState<User[] | null>(null);
    useEffect(() => {
        async function fetchData() {
            try {
                const data = await getRequest('http://localhost:8000/api/users');
                setUsers(data.users);
            } catch (error) {
                console.error('ユーザー情報の取得に失敗しました:', error);
            }
        }

        fetchData();
    }, []);

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
                        <th className='p-2'>作成日時</th>
                        <th className='p-2'>更新日時</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map((user) => {
                        return (
                            <tr key={user.id} className='border-b border-gray-200'>
                                <td className='p-2 text-center'>{user.id}</td>
                                <td className='p-2 text-center'>{user.name}</td>
                                <td className='p-2 text-center'>{user.email}</td>
                                <td className='p-2 text-center'>{user.created_at}</td>
                                <td className='p-2 text-center'>{user.updated_at}</td>
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