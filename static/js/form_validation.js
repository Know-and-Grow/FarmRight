// Validate all input values, if all are filled.
function validateinput(){
    var valid = false;
    // array of all input options: Season types
    var seasons = document.predictionform.season; 
    
    for(var i=0; i<seasons.length; i++){
        if(seasons[i].checked){
            valid = true;
            break;
        }
    }
    if(valid){
        alert("Validation Successful. Predicting the right crop for you.");
    }
    else{
        alert("Validation Failure. Please fill all fields.");
        return false;
    }
    // call predict function to predict based on input values
    alert("calling predictinput");
    alert(predictinput());
}

// predict based on input values
function predictinput(){
    var state = document.getElementById("state");
    var district = document.getElementById("district");
    var nitrogen = document.getElementById("nitrogen");
    var phosphorus = document.getElementById("phosphorus");
    var potassium = document.getElementById("potassium");
    var organiccarbon = document.getElementById("organiccarbon");
    var ph = document.getElementById("ph");
    var rainfall = document.getElementById("rainfall");
    var temperature = document.getElementById("temperature");

    var kharif = document.getElementById("kharif");
    var rabi = document.getElementById("rabi");
    var summer = document.getElementById("summer");
    var winter = document.getElementById("winter");
    var autumn = document.getElementById("autumn");
    var wholeyear = document.getElementById("wholeyear");
    var seasontype;
    if(kharif.checked == true) {
        seasontype = kharif.value;
    }
    else if(rabi.checked == true) {
        seasontype = rabi.value;
    }
    else if(summer.checked == true) {
        seasontype = summer.value;
    }
    else if(winter.checked == true) {
        seasontype = winter.value;
    }
    else if(autumn.checked == true) {
        seasontype = autumn.value;
    }
    else if(wholeyear.checked == true) {
        seasontype = wholeyear.value;
    }
    else {
        alert("Not able to get season");
    }
    var a = seasontype.value;
    alert(a);
    return true;
}
