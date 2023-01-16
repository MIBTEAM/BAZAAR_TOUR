/* Time Class*/ 
class MyTime {
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

const time = new MyTime(1, 2, 3, 4);
var interval = setInterval(setEndingTime, 1000, time);
function setEndingTime(t) {
    if (t.isTimeEnded())
        clearInterval(interval);
    document.getElementById("days").innerHTML = t.days;
    document.getElementById("hours").innerHTML = t.hours;
    document.getElementById("minutes").innerHTML = t.minutes;
    document.getElementById("seconds").innerHTML = t.seconds;
    t.decSeconds();
}