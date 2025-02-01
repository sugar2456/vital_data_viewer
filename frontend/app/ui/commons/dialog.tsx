import React from 'react';

interface DialogProps {
    isOpen: boolean;
    onClose: () => void;
    children: React.ReactNode;
}

const Dialog: React.FC<DialogProps> = ({ isOpen, onClose, children }) => {
    if (!isOpen) {
        return null;
    }

    return (
        <div className='fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center'>
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
                        className='bg-blue-500 text-white rounded py-2 px-8 m-2 shadow hover:bg-blue-100 focus:outline-none'
                        onClick={onClose}
                    >
                        登録
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Dialog;
