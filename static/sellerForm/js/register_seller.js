/* Form 1 javascript */
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

var counter = 0;
function displayUSerID() {
    if (counter == 0) {
        /*  creating unique userid = day month year hours minutes */
        var currentdate = new Date();
        var datetime = "BTS" + currentdate.getDay() + currentdate.getMonth() + currentdate.getFullYear() + currentdate.getHours()
            + currentdate.getMinutes() + currentdate.getSeconds() + currentdate.getMilliseconds();
        document.getElementById('userid').value = datetime;
        counter++;
        generateUsername();
    }

}
function generateUsername() {
    rand = Math.floor(Math.random() * (9999 - 1000 + 1)) + 1000;
    document.getElementById('username').value = document.getElementById('firstname').value + document.getElementById('lastname').value + rand
}
function passwordMatching() {
    if (password2 = document.getElementById('password1').value !== '') {
        password1 = document.getElementById('password').value;
        password2 = document.getElementById('password1').value;
        if (password1 === password2 && (password1 !== '' && password2 !== '') && password1.length >= 8) {
            password1 = document.getElementById('password').style.borderColor = 'green';
            password1 = document.getElementById('password1').style.borderColor = 'green';
            document.getElementById('submission').style.display = 'block';

        }
        else {
            password1 = document.getElementById('password').style.borderColor = 'red';
            password1 = document.getElementById('password1').style.borderColor = 'red';
            document.getElementById('submission').style.display = 'none';
        }
    }
}
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

/* Form 3 javascript */

$("#switch").on('change', function () {
    if ($(this).is(':checked')) {
        $(this).attr('value', 'true');
        document.getElementById('return').style.display = 'none';
    }
    else {
        $(this).attr('value', 'false');
        document.getElementById('return').style.display = 'block';
    }
});
//Create javascript object with pakistan provinces
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

/* for return Address*/
document.getElementById("returnprovince").onchange = function () {
    removeOptions(document.getElementById('returncity'));
    let cities = pakistan[this.value];
    cities.forEach(function (returncity) {
        let currentCity = Object.keys(returncity)[0];
        let option = document.createElement("option");
        option.value = currentCity;
        option.innerText = currentCity;
        document.getElementById("returncity").append(option);
    });
};

/* Form 4 javascript */
function startTimer() {
    var count = 10;
    const interval = setInterval(function () {
        if (count == 110) {
            display();
            console.log("i am running !!!");
        }
        document.getElementById('percentage').innerHTML = (count + "%");
        count = count + 20
    }, 400);
}
function display() {
    document.getElementById('spinner').style.display = 'none';
    document.getElementById('percentage').style.display = 'none';
    document.getElementById('close').style.display = 'block';
    document.getElementById('tick').style.display = 'block';
    document.getElementById('msg').style.display = 'block';
    clearInterval(interval);

}


/* over javascripts for 1-4 form*/
function displayForm2() {
    if (document.getElementById("firstname").value !== "" && document.getElementById("lastname").value !== "" && document.getElementById("userid").value !== "" && document.getElementById("email").value !== "" && document.getElementById("mobilenumber").value !== "" && document.getElementById("cnic").value !== "" && document.getElementById("userimg").value !== "") {
        document.getElementById("form1").style.display = 'none';
        document.getElementById("form2").style.display = 'block';
    }
}
function displayForm3() {
    if (document.getElementById("cnicfrontside").value !== "" && document.getElementById("cnicbackside").value !== "" && document.getElementById("brandlogo").value !== "" && document.getElementById("storename").value !== "") {
        document.getElementById("form2").style.display = 'none';
        document.getElementById("form3").style.display = 'block';
    }
}
function displayForm4() {
    if (document.getElementById("town").value !== "" && document.getElementById("province").value !== "" && document.getElementById("city").value !== "") {
        if (document.getElementById('return').style.display === 'none') {
            document.getElementById("form3").style.display = 'none';
            document.getElementById("form4").style.display = 'block';
            startTimer();

        }
        else if (document.getElementById("returnarea").value !== "" && document.getElementById("returnprovince").value !== "" && document.getElementById("returncity").value !== "") {
            document.getElementById("form3").style.display = 'none';
            document.getElementById("form4").style.display = 'block';
            startTimer();
        }
    }
}