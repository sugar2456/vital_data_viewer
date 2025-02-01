import React from 'react';

interface DialogProps {
    isOpen: boolean;
    onClose: () => void;
    onSubmit: (e: React.FormEvent) => void;
    children: React.ReactNode;
}

const Dialog: React.FC<DialogProps> = (
    { isOpen, onClose, onSubmit, children }
) => {
    if (!isOpen) {
        return null;
    }

    return (
        <form onSubmit={onSubmit}  className='fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center'>
            <div className='bg-white p-4 rounded shadow-lg'>
                {children}
                <div className='flex justify-between items-center'>
                    <button
                        className='bg-gray-500 text-white rounded p-2 m-2 shadow hover:bg-blue-100 focus:outline-none'
                        onClick={onClose}
                    >
                        キャンセル
                    </button>
                    <button
                        type='submit'
                        className='bg-blue-500 text-white rounded py-2 px-8 m-2 shadow hover:bg-blue-100 focus:outline-none'
                    >
                        登録
                    </button>
                </div>
            </div>
        </form>
    );
};

export default Dialog;
