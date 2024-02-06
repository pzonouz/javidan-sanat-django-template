const swiper = new Swiper(".swiper", {
  // Optional parameters
  direction: "horizontal",
  freeMode: true,
  loop: true,

  autoplay: {
    delay: 5000,
  },

  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
  },

  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  // And if we need scrollbar
  // scrollbar: {
  //   el: ".swiper-scrollbar",
  // },
});
sideBar = document.getElementById("side-menu");
backdrop = document.getElementById("backdrop");
document.getElementById("menu-button").addEventListener("click", (e) => {
  e.stopPropagation();
  sideBar.classList.add("open");
  backdrop.classList.add("open");
});
backdrop.addEventListener("click", (e) => {
  e.stopPropagation();
  sideBar.classList.remove("open");
  backdrop.classList.remove("open");
});
const entityFilterTabHeaders = document.querySelector(
  ".entity-filter-tab-headers"
);

// filter
const entityFilterTabs = document.querySelectorAll(".entity-filter-tab");
entityFilterTabHeaders.addEventListener("click", (e) => {
  const el = e.target;
  let i = 0;
  [...el.parentElement.children].forEach((sib) => {
    if (entityFilterTabs[i].id == el.id) {
      entityFilterTabs[i].classList.add("active");
    } else {
      entityFilterTabs[i].classList.remove("active");
    }
    if (sib != el) {
      sib.classList.remove("active");
    }
    i++;
  });
  el.classList.add("active");
});
