"use client";
import React from 'react';
import { useAuthStore } from '@/app/store/viewStore';

const ErrorDialog: React.FC = () => {
  const { error, setError } = useAuthStore();

  if (!error) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white p-6 h-44 rounded shadow-md flex items-center justify-between flex-col">
        <h2 className="text-xl font-bold">エラー</h2>
        <p>{error}</p>
        
        <button
          className="mt-4 px-4 py-2 bg-red-500 text-white rounded"
          onClick={() => setError(null)}
        >
          閉じる
        </button>
      </div>
    </div>
  );
};

export default ErrorDialog;