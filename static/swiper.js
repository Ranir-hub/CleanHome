var swiper = new Swiper(".swiper", { 
    spaceBetween: 20,
    mousewheel: true,     
    keyboard: true,
    slidesPerView: 1,
    breakpoints: {
      1200: {
        slidesPerView: 2,
      },
    }
});