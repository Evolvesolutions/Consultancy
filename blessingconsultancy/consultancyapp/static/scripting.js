// Toggle menu (already added earlier)
  function toggleMenu() {
    const menu = document.getElementById('menu');
    menu.classList.toggle('show');
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

/* form validation */

  function validateForm() {
    const mobile = document.getElementById("mobile").value.trim();
    const email = document.getElementById("email").value.trim();
    const mobileRegex = /^[0-9]{10}$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!mobileRegex.test(mobile)) {
      alert("Please enter a valid 10-digit mobile number.");
      return false;
    }

    if (!emailRegex.test(email)) {
      alert("Please enter a valid email address.");
      return false;
    }

    return true; // submit form
  }