/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for entityion nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for entityion-ready output files, see mode: "entityion" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => {
  // webpackBootstrap
  /******/ var __webpack_modules__ = {
    /***/ "./src/main.js":
      /*!*********************!*\
  !*** ./src/main.js ***!
  \*********************/
      /***/ () => {
        eval(
          'const swiper = new Swiper(".swiper", {\n  // Optional parameters\n  direction: "horizontal",\n  freeMode: true,\n  loop: true,\n\n  autoplay: {\n    delay: 5000,\n  },\n\n  // If we need pagination\n  pagination: {\n    el: ".swiper-pagination",\n  },\n\n  // Navigation arrows\n  navigation: {\n    nextEl: ".swiper-button-next",\n    prevEl: ".swiper-button-prev",\n  },\n\n  // And if we need scrollbar\n  // scrollbar: {\n  //   el: ".swiper-scrollbar",\n  // },\n});\nsideBar = document.getElementById("side-menu");\nbackdrop = document.getElementById("backdrop");\ndocument.getElementById("menu-button").addEventListener("click", (e) => {\n  e.stopPropagation();\n  sideBar.classList.add("open");\n  backdrop.classList.add("open");\n});\nbackdrop.addEventListener("click", (e) => {\n  e.stopPropagation();\n  sideBar.classList.remove("open");\n  backdrop.classList.remove("open");\n});\nconst entityFilterTabHeaders = document.querySelector(\n  ".entity-filter-tab-headers"\n);\n\nconst entityFilterTabs = document.querySelectorAll(".entity-filter-tab");\nentityFilterTabHeaders.addEventListener("click", (e) => {\n  const el = e.target;\n  let i = 0;\n  [...el.parentElement.children].forEach((sib) => {\n    if (entityFilterTabs[i].id == el.id) {\n      entityFilterTabs[i].classList.add("active");\n    } else {\n      entityFilterTabs[i].classList.remove("active");\n    }\n    if (sib != el) {\n      sib.classList.remove("active");\n    }\n    i++;\n  });\n  el.classList.add("active");\n});\n\n\n//# sourceURL=webpack:///./src/main.js?'
        );

        /***/
      },

    /******/
  };
  /************************************************************************/
  /******/
  /******/ // startup
  /******/ // Load entry module and return exports
  /******/ // This entry module can't be inlined because the eval devtool is used.
  /******/ var __webpack_exports__ = {};
  /******/ __webpack_modules__["./src/main.js"]();
  /******/
  /******/
})();
