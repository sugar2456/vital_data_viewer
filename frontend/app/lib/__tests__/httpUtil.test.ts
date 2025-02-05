import { getRequest, postRequest } from '../common/httpUtil';

describe('httpUtil', () => {
    beforeEach(() => {
        // 各テストの前に fetch をモック
        global.fetch = jest.fn();
    });

    afterEach(() => {
        // 各テストの後にモックをクリア
        jest.clearAllMocks();
    });

    describe('getRequest', () => {
        it('should return data when the response is successful', async () => {
            const mockData = { message: 'success' };
            (global.fetch as jest.Mock).mockResolvedValue({
                ok: true,
                json: jest.fn().mockResolvedValue(mockData),
            });

            const data = await getRequest('http://example.com');
            expect(data).toEqual(mockData);
            expect(global.fetch).toHaveBeenCalledWith('http://example.com');
        });

        it('should throw an error when the response is not successful', async () => {
            (global.fetch as jest.Mock).mockResolvedValue({
                ok: false,
                status: 500,
            });

            await expect(getRequest('http://example.com')).rejects.toThrow('HTTPエラー! status: 500');
            expect(global.fetch).toHaveBeenCalledWith('http://example.com');
        });
    });

    describe('postRequest', () => {
        it('should return data when the response is successful', async () => {
            const mockData = { message: 'success' };
            const postData = { key: 'value' };
            (global.fetch as jest.Mock).mockResolvedValue({
                ok: true,
                json: jest.fn().mockResolvedValue(mockData),
            });

            const data = await postRequest('http://example.com', postData);
            expect(data).toEqual(mockData);
            expect(global.fetch).toHaveBeenCalledWith('http://example.com', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(postData),
            });
        });

        it('should throw an error when the response is not successful', async () => {
            const postData = { key: 'value' };
            (global.fetch as jest.Mock).mockResolvedValue({
                ok: false,
                status: 500,
            });

            await expect(postRequest('http://example.com', postData)).rejects.toThrow('HTTPエラー! status: 500');
            expect(global.fetch).toHaveBeenCalledWith('http://example.com', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(postData),
            });
        });
    });
});