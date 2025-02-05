import { formatTime, formatDateTimeToSeconds } from '../common/timeUtil';

describe('formatTime', () => {
    it('should format date to HH:mm:ss', () => {
        const date = new Date('2025-01-22T12:34:32.000');
        const formattedTime = formatTime(date, 'HH:mm:ss');
        expect(formattedTime).toBe('12:34:32');
    });

    it('should throw an error for invalid date object', () => {
        expect(() => formatTime(new Date('invalid-date'), 'HH:mm:ss')).toThrow('不正な日付情報です');
    });
});

describe('formatDateTimeToSeconds', () => {
    it('should format dateTimeString to HH:mm:ss', () => {
        const dateTimeString = '2025-01-22T12:34:32.000';
        const formattedTime = formatDateTimeToSeconds(dateTimeString);
        expect(formattedTime).toBe('2025/01/22 12:34:32');
    });

    it('should throw an error for invalid dateTimeString', () => {
        const invalidDateTimeString = 'invalid-date';
        expect(() => formatDateTimeToSeconds(invalidDateTimeString)).toThrow('不正な日付情報です');
    });
});