function setTeeDate(date, numDays){
    newDate = date.setDate(date.getDate() + numDays);
    newDate = new Date(newDate);
    dd = newDate.getDate();
    mm = newDate.getMonth() + 1;
    y = newDate.getFullYear();
    teeDate = mm + "/" + dd + "/" + y;
    return teeDate;
};



document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('teetime');
    checkPageButton.addEventListener('click', function() {
        let teeTime = document.getElementById("appt").value;
        teeHour = teeTime.split(":")[0];
        teeMin = teeTime.split(":")[1];
        let hourSet = "AM";
        
        teeHour = teeTime.split(":")[0];
        teeMin = teeTime.split(":")[1];
        console.log(teeHour, teeMin);
        hourSet = "AM";
        if (teeHour == 12){
            teeHour = 12;
            hourSet = "PM";
        }else if (teeHour >12){
            teeHour = teeHour - 12;
            hourSet = "PM";
            console.log(`${teeHour}, First IF`);
        }else if (teeHour > 10){
            teeHour = teeHour.toString()[1];
            console.log(`${teeHour} Else IF statement`);
        }
        

        let currentDate = new Date();
        newTee = setTeeDate(currentDate, 14);
        //newTee = Date(teeDate);
        
        wsite = `https://www1.foretees.com/v5/mediterra_golf_m40/Member_sheet?calDate=${newTee}&course=-ALL-&show_calendar#dp1609621626117:~:text=${teeHour}%3A${teeMin}%20${hourSet}`;

        //Have to offset month due to it being 0-11 in MOD.
        window.open(wsite);
        
      
        //Example Text
        //chrome.tabs.getSelected(null, function(tab) {
        //alert(`Your desired tee time is HR: ${teeHour} MIN: ${teeMin} ${hourSet}.  Todays date is ${currentDate}.  Desired Date: ${newTee}`);
      //});
    }, false);
  }, false);
