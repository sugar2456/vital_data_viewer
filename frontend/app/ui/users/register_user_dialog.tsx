import React, {useState} from 'react';
import Dialog from '@/app/ui/commons/dialog';
import { authenticatedGetRequest } from '@/app/lib/common/apiClient';
import { UserRole } from '@/app/constants/users';
import { useUsersViewStore } from '@/app/store/usersViewStore';

interface RegisterUserDialogProps {
    isOpen: boolean;
    onClose: () => void;
}

const RegisterUserDialog: React.FC<RegisterUserDialogProps> = (
    { isOpen, onClose }
) => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [fitbit_user_id, setFitbit_id] = useState('');
    const [role, setRole] = useState(UserRole.USER);
    const [errors, setErrors] = useState<{ name?: string; email?: string, fitbit_id?: string }>({});
    const { addUser } = useUsersViewStore();

    const validate = () => {
        const newErrors: { name?: string; email?: string, fitbit_id?: string } = {};
        if (!name) newErrors.name = '名前を入力してください';
        if (!email) {
            newErrors.email = 'メールアドレスを入力してください';
        } else if (!/\S+@\S+\.\S+/.test(email)) {
            newErrors.email = '有効なメールアドレスを入力してください';
        }
        if (!fitbit_user_id) {
            newErrors.fitbit_id = 'Fitbit IDを入力してください';
        } else if (!/^[0-9a-zA-Z]+$/.test(fitbit_user_id)) {
            newErrors.fitbit_id = '有効なFitbit IDを入力してください';
        }
        return newErrors;
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        const validationErrors = validate();
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
        } else {
            await addUser({ name, email, fitbit_user_id, role });
            onClose();
        }
    };

    return (
        <Dialog isOpen={isOpen} onClose={onClose} onSubmit={handleSubmit}>
            <div className='flex flex-col'>
                <label htmlFor='name' className='text-sm'>名前</label>
                <input
                    id='name'
                    type='text'
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className='border border-gray-300 rounded p-2 m-2'
                />
                {errors.name && <p className='text-red-500 text-sm'>{errors.name}</p>}
                
                {/* htmlデフォルトのメールの検証を使わないで、js側でメールの検証を使う*/}
                <label htmlFor='email' className='text-sm'>メールアドレス</label>
                <input
                    id='email'
                    type='text'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className='border border-gray-300 rounded p-2 m-2'
                />
                {errors.email && <p className='text-red-500 text-sm'>{errors.email}</p>}

                <label htmlFor='fitbit_id' className='text-sm'>Fitbit ID</label>
                <input
                    id='fitbit_id'
                    type='text'
                    value={fitbit_user_id}
                    onChange={(e) => setFitbit_id(e.target.value)}
                    className='border border-gray-300 rounded p-2 m-2'
                />
                {errors.fitbit_id && <p className='text-red-500 text-sm'>{errors.fitbit_id}</p>}

                <label htmlFor='role' className='text-sm'>ロール</label>
                <select
                    id='role'
                    className='border border-gray-300 rounded p-2 m-2'
                    value={role}
                    onChange={(e) => setRole(parseInt(e.target.value))}
                >
                    <option value={UserRole.ADMIN}>管理者</option>
                    <option value={UserRole.USER}>ユーザー</option>
                </select>
            </div>
        </Dialog>
    );
};

export default RegisterUserDialog;