function password_show_hide() {
    var x = document.getElementById("password");
    if (x.type === 'password') {
        x.type = 'text';
        document.getElementById("myInput").classList.remove("fa-eye-slash");
        document.getElementById("myInput").classList.add("fa-eye");
    }
    else {
        x.type = 'password';
        document.getElementById("myInput").classList.remove("fa-eye");
        document.getElementById("myInput").classList.add("fa-eye-slash");
    }
}

function password_show_hide1() {
    var x = document.getElementById("password1");
    if (x.type === 'password') {
        x.type = 'text';
        document.getElementById("myInput1").classList.remove("fa-eye-slash");
        document.getElementById("myInput1").classList.add("fa-eye");
    }
    else {
        x.type = 'password';
        document.getElementById("myInput1").classList.remove("fa-eye");
        document.getElementById("myInput1").classList.add("fa-eye-slash");
    }
}

function generateMobile() {
    if (document.getElementById('mobilenumber').value.length == 4) {
        document.getElementById('mobilenumber').value += "-";
    }
}
function generateCNIC() {
    if (document.getElementById('cnic').value.length == 5 || document.getElementById('cnic').value.length == 13) {
        document.getElementById('cnic').value += "-";
    }
}

var count = 0;
function displayBuyerID() {
    if (count == 0) {
        /*  creating unique userid = day month year hours minutes */
        var currentdate = new Date();
        var datetime = "BTB" + currentdate.getDay() + currentdate.getMonth() + currentdate.getFullYear() + currentdate.getHours()
            + currentdate.getMinutes() + currentdate.getSeconds() + currentdate.getMilliseconds();
        document.getElementById('buyerid').value = datetime;
        count++;
        console.log("inn");
        generateUsername();
    }
}
function generateUsername() {
    rand = Math.floor(Math.random() * (9999 - 1000 + 1)) + 1000;
    document.getElementById('username').value = document.getElementById('firstname').value + document.getElementById('lastname').value + rand
}
window.onload = function () {
    document.getElementById('btnModal').click();
}









let pakistan = {
    "Sindh": [
        { "Karachi": ["Korangi", "Kotli", "Shah Faisal"] },
        { "East Karachi": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Karachi": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Hyderabad": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Sukkur": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Rohri": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Malir": ["Korangi", "Kotli", "Shah Faisal"] },
    ],
    "Punjab": [
        { "Lahore": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Islamabad": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Multan": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Sahiwal": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Jhang": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Chinnot": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Rahin Yar Khan": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Dera Ghazi Khan": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Khanawal": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Faisalabad": ["Korangi", "Kotli", "Shah Faisal"] }
    ],
    "Balochistan": [
        { "Quetta": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Sibi": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Gwadar": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Chaman": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Khuzdar": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Hub": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Dera Allah Yaar": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Dera Murad Jamali": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Karakoram": ["Korangi", "Kotli", "Shah Faisal"] }
    ],
    "Khyber Pakhtunkhwa": [
        { "Peshawar": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Mardan": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Swabi": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Mingora": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Nowshera": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Abbottabad": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Chitral": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Karak": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Mansehra": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Kohat": ["Korangi", "Kotli", "Shah Faisal"] }
    ],
    "Gilgit-Baltistan": [
        { "Kundian": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Gilgit": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Skardu": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Khaplu": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Dambudas": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Chillas": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Tangir": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Aliabad": ["Korangi", "Kotli", "Shah Faisal"] },
        { "Juglot": ["Korangi", "Kotli", "Shah Faisal"] },
    ]
};
//On change of province display cities in console

function removeOptions(selectElement) {
    var i, L = selectElement.options.length - 1;
    for (i = L; i >= 0; i--) {
        selectElement.remove(i);
    }
}
/* for pickup Address*/
document.getElementById("province").onchange = function () {
    removeOptions(document.getElementById('city'));
    let cities = pakistan[this.value];
    cities.forEach(function (city) {
        let currentCity = Object.keys(city)[0];
        let option = document.createElement("option");
        option.value = currentCity;
        option.innerText = currentCity;
        document.getElementById("city").append(option);
    });
};
