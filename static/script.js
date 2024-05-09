document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        if (document.querySelector(".flashed_msgs") != undefined) {
            document.querySelector(".flashed_msgs").remove();
        }
    }, 3000);
});

const notAvailableCheck = () => {
    document.querySelector('#notAvailable').checked = true;
    document.querySelector('#available').checked = false;
}
const availableCheck = () => {
    document.querySelector('#notAvailable').checked = false;
    document.querySelector('#available').checked = true;
}
const goToHome = () => {
    location.href="/";
}
