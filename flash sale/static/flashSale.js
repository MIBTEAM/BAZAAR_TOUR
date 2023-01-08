import { MyTime } from './MyTime.js'

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