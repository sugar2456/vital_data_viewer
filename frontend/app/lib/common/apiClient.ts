import { useAuthStore } from '@/app/store/viewStore';

const apiHostUrl = process.env.NEXT_PUBLIC_API_URL;
if (!apiHostUrl) {
    throw new Error('NEXT_PUBLIC_API_URLが設定されていません');
}

/**
 * 認証トークンを含むGETリクエストを送信する関数
 * @param {string} uri - リクエストを送信するURL
 * @returns {Promise<any>} - レスポンスデータ
 * @throws {Error} - リクエストが失敗した場合
 */
export async function authenticatedGetRequest(uri: string): Promise<any> {
    const token = useAuthStore.getState().token;
    const headers: Record<string, string> = token ? { 'Authorization': `Bearer ${token}` } : {};
    return getRequestWithHeaders(uri, headers);
}

/**
 * 認証トークンを含むPOSTリクエストを送信する関数
 * @param {string} uri - リクエストを送信するURL
 * @param {any} data - リクエストボディに含めるデータ
 * @returns {Promise<any>} - レスポンスデータ
 * @throws {Error} - リクエストが失敗した場合
 */
export async function authenticatedPostRequest(uri: string, data: any): Promise<any> {
    const token = useAuthStore.getState().token;
    const headers = {
        'Content-Type': 'application/json',
        ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
    };
    return postRequestWithHeaders(uri, data, headers);
}

async function getRequestWithHeaders(uri: string, headers: Record<string, string>): Promise<any> {
    const { setError, removeToken } = useAuthStore.getState();
    
    const response = await fetch(apiHostUrl + uri, { headers });
    if (response.status === 401) {
        removeToken();
        window.location.href = '/auth/login';
    } else if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.message || '通信エラーが発生しました');
        throw new Error(`HTTPエラー! status: ${response.status}`);
    }
    return response.json();
}

async function postRequestWithHeaders(uri: string, data: any, headers: Record<string, string>): Promise<any> {
    const { setError, removeToken } = useAuthStore.getState();
    const response = await fetch(apiHostUrl + uri, {
        method: 'POST',
        headers,
        body: JSON.stringify(data),
    });
    if (response.status === 401) {
        removeToken();
        window.location.href = '/auth/login';
    } else if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.message || '通信エラーが発生しました');
        throw new Error(`HTTPエラー! status: ${response.status}`);
    }
    return response.json();
}