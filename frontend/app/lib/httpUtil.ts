/**
 * GETリクエストを送信する関数
 * @param {string} url - リクエストを送信するURL
 * @returns {Promise<any>} - レスポンスデータ
 * @throws {Error} - リクエストが失敗した場合
 */
export async function getRequest(url: string): Promise<any> {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`HTTPエラー! status: ${response.status}`);
    }
    return response.json();
}

/**
 * POSTリクエストを送信する関数
 * @param {string} url - リクエストを送信するURL
 * @param {any} data - リクエストボディに含めるデータ
 * @returns {Promise<any>} - レスポンスデータ
 * @throws {Error} - リクエストが失敗した場合
 */
export async function postRequest(url: string, data: any): Promise<any> {
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    if (!response.ok) {
        throw new Error(`HTTPエラー! status: ${response.status}`);
    }
    return response.json();
}

/**
 * PUTリクエストを送信する関数
 * @param {string} url - リクエストを送信するURL
 * @param {any} data - リクエストボディに含めるデータ
 * @returns {Promise<any>} - レスポンスデータ
 * @throws {Error} - リクエストが失敗した場合
 */
export async function putRequest(url: string, data: any): Promise<any> {
    const response = await fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    if (!response.ok) {
        throw new Error(`HTTPエラー! status: ${response.status}`);
    }
    return response.json();
}

/**
 * DELETEリクエストを送信する関数
 * @param {string} url - リクエストを送信するURL
 * @returns {Promise<any>} - レスポンスデータ
 * @throws {Error} - リクエストが失敗した場合
 */
export async function deleteRequest(url: string): Promise<any> {
    const response = await fetch(url, {
        method: 'DELETE',
    });
    if (!response.ok) {
        throw new Error(`HTTPエラー! status: ${response.status}`);
    }
    return response.json();
}