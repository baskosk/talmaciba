let images = ["bilde1.jpg", "bilde2.jpg", "bilde3.jpg"];
let currentIndex = 0;
let slider = document.getElementById("slider");

function nextSlide() {
    currentIndex = (currentIndex + 1) % images.length;
    slider.innerHTML = `<img src="${images[currentIndex]}" alt="attēls">`;
}

setInterval(nextSlide, 3000); // Bildes mainās ik pēc 3 sekundēm
