/**
 * 時間を指定したフォーマットに変換する関数
 * @param {Date} date - 日付オブジェクト
 * @param {string} format - フォーマット文字列
 * @returns {string} - フォーマットされた時間文字列
 * @throws {Error} - 不正な日付オブジェクトが渡された場合
 */
export function formatTime(date: Date, format: string): string {
    if (!(date instanceof Date) || isNaN(date.getTime())) {
        throw new Error('不正な日付情報です');
    }

    const options: Intl.DateTimeFormatOptions = {};

    if (format.includes('YYYY')) options.year = 'numeric';
    if (format.includes('MM')) options.month = '2-digit';
    if (format.includes('DD')) options.day = '2-digit';
    if (format.includes('HH')) options.hour = '2-digit';
    if (format.includes('mm')) options.minute = '2-digit';
    if (format.includes('ss')) options.second = '2-digit';

    return new Intl.DateTimeFormat('ja-JP', options).format(date);
}

/**
 * 時間情報を秒まで含むフォーマットに変換する関数
 * @param {string} dateTimeString - 時間情報の文字列
 * @returns {string} - 秒まで含むフォーマットされた時間文字列
 * @throws {Error} - 不正な時間情報の文字列が渡された場合
 */
export function formatDateTimeToSeconds(dateTimeString: string): string {
    const date = new Date(dateTimeString);
    if (isNaN(date.getTime())) {
        throw new Error('不正な日付情報です');
    }
    return formatTime(date, 'YYYY-MM-DD HH:mm:ss');
}