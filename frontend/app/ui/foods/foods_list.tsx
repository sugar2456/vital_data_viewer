"use client";
import React from 'react';
import foodsRow from '@/app/ui/data/foods/foods_period.json';
import { useFoodViewDataStore } from '@/app/store/foodViewStore';
import { FaTrash } from 'react-icons/fa';

const foodsPeriod = foodsRow.foods_period;
const FoodsList: React.FC = () => {
    const { setFoodId } = useFoodViewDataStore();
    const handleClick = (id: number) => {
        setFoodId(id);
    }
    const handleDeleteClick = (foodId: number) => {
        // ゴミ箱アイコンがクリックされたときの処理をここに追加
        console.log(`Food with ID ${foodId} deleted`);
    };
    return (
        <div className="container mx-auto p-4 bg-white rounded shadow-sm">
            <h1 className="text-2xl font-bold mb-4">摂取した食品リスト</h1>
            {
                foodsPeriod.map((foodRecord) => {
                    return (
                        <div key={foodRecord.date} className="mb-4">
                            <div className="bg-yellow-100 p-2 rounded">
                                <h2 className="text-lg font-bold">{foodRecord.date}</h2>
                            </div>
                            {
                                foodRecord.foods.map((food) => {
                                    return (
                                        <div
                                            key={food.logId}
                                            className="flex justify-between border-b border-gray-200 p-2"
                                            onClick={() => handleClick(food.loggedFood.foodId)}
                                        >
                                            <div>
                                                <h3 className="font-bold">{food.loggedFood.name}</h3>
                                                <h3 className="text-gray-500">{food.loggedFood.brand}</h3>
                                            </div>
                                            <div className="flex justify-between gap-4">
                                                <div className="flex flex-col items-end">
                                                    <p>{food.loggedFood.amount} {food.loggedFood.unit.name}</p>
                                                    <p>{food.loggedFood.calories} kcal</p>
                                                </div>
                                                <div className="flex items-center">
                                                    <FaTrash
                                                        className="text-red-500 cursor-pointer"
                                                        onClick={(e) => {
                                                            e.stopPropagation(); // 親のクリックイベントが発火しないようにする
                                                            handleDeleteClick(food.logId);
                                                        }}
                                                    />
                                                </div>
                                            </div>
                                        </div>
                                    );
                                })
                            }
                        </div>
                    );
                })
            }
        </div>
    );
};

export default FoodsList;