const DAYS_AHEAD = 14;
const SHEET_URL = "https://www1.foretees.com/v5/mediterra_golf_m40/Member_sheet";

// Returns the date numDays from `date` as M/D/YYYY (the format ForeTees expects).
function setTeeDate(date, numDays) {
    const newDate = new Date(date);
    newDate.setDate(newDate.getDate() + numDays);
    return `${newDate.getMonth() + 1}/${newDate.getDate()}/${newDate.getFullYear()}`;
}

// Converts "HH:MM" (24h, from <input type="time">) to ForeTees' "H:MM AM/PM".
function formatTeeTime(value) {
    const [hourStr, teeMin] = value.split(":");
    const hour24 = Number(hourStr);
    const hourSet = hour24 >= 12 ? "PM" : "AM";
    const teeHour = hour24 % 12 || 12;
    return `${teeHour}:${teeMin} ${hourSet}`;
}

function buildTeeSheetUrl(teeTime, now = new Date()) {
    const calDate = setTeeDate(now, DAYS_AHEAD);
    // The :~:text= fragment makes Chrome scroll to and highlight the tee time on the sheet.
    return `${SHEET_URL}?calDate=${calDate}&course=-ALL-&show_calendar#:~:text=${encodeURIComponent(formatTeeTime(teeTime))}`;
}

if (typeof document !== "undefined") {
    document.addEventListener("DOMContentLoaded", () => {
        document.getElementById("teeform").addEventListener("submit", (event) => {
            event.preventDefault();
            const teeTime = document.getElementById("appt").value;
            chrome.tabs.create({ url: buildTeeSheetUrl(teeTime) });
        });
    });
}

if (typeof module !== "undefined") {
    module.exports = { setTeeDate, formatTeeTime, buildTeeSheetUrl };
}
