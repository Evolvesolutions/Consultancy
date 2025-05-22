// Toggle menu (already added earlier)
function toggleMenu() {
  const navbar = document.getElementById('navbar');
  navbar.classList.toggle('show');
}

// Carousel slideshow
const slides = document.querySelector('.slides');
const slideCount = document.querySelectorAll('.slide').length;
let currentIndex = 0;

function showNextSlide() {
  if (currentIndex < slideCount - 1) {
    // Move to next slide with animation
    currentIndex++;
    slides.style.transition = 'transform 1s ease';
    slides.style.transform = `translateX(-${currentIndex * 100}vw)`;
  } else {
    // Jump instantly back to first slide without animation
    currentIndex = 0;
    slides.style.transition = 'none';
    slides.style.transform = `translateX(0)`;

    // Force reflow so next animation works
    void slides.offsetWidth;

    // Re-enable animation for next slides
    slides.style.transition = 'transform 1s ease';
  }
}

// Slide every 3 seconds
setInterval(showNextSlide, 3000);

