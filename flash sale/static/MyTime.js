export class MyTime {
    constructor(days, hours, minutes, seconds) {
        this.days = days;
        this.hours = hours;
        this.minutes = minutes;
        this.seconds = seconds;
    }
    isTimeEnded() {
        return this.days == 0 && this.hours == 0 && this.minutes == 0 && this.seconds == 0;
    }
    decSeconds() {
        if (this.isTimeEnded())
            return;
        else if (this.seconds == 0) {
            this.seconds = 59;
            this.decMinutes();
        }
        else
            this.seconds -= 1;
    }
    decMinutes() {
        if (this.minutes == 0) {
            this.minutes = 59;
            this.decHours();
        }
        else
            this.minutes -= 1;
    }
    decHours() {
        if (this.hours == 0) {
            this.hours = 23;
            this.decDays();
        }
        else
            this.hours -= 1;
    }
    decDays() {
        if (this.days == 0)
            return;
        else
            this.days -= 1;
    }
}
