/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/main.js":
/*!*********************!*\
  !*** ./src/main.js ***!
  \*********************/
/***/ (() => {

eval("const swiper = new Swiper(\".swiper\", {\n  // Optional parameters\n  direction: \"horizontal\",\n  freeMode: true,\n  loop: true,\n\n  autoplay: {\n    delay: 5000,\n  },\n\n  // If we need pagination\n  pagination: {\n    el: \".swiper-pagination\",\n  },\n\n  // Navigation arrows\n  navigation: {\n    nextEl: \".swiper-button-next\",\n    prevEl: \".swiper-button-prev\",\n  },\n\n  // And if we need scrollbar\n  // scrollbar: {\n  //   el: \".swiper-scrollbar\",\n  // },\n});\ntry {\n  sideBar = document.getElementById(\"side-menu\");\n  backdrop = document.getElementById(\"backdrop\");\n  document.getElementById(\"menu-button\").addEventListener(\"click\", (e) => {\n    e.stopPropagation();\n    sideBar.classList.add(\"open\");\n    backdrop.classList.add(\"open\");\n  });\n  backdrop.addEventListener(\"click\", (e) => {\n    e.stopPropagation();\n    sideBar.classList.remove(\"open\");\n    backdrop.classList.remove(\"open\");\n  });\n} catch (error) {}\n\n// filter\ntry {\n  const entityFilterTabHeaders = document.querySelector(\n    \".entity-filter-tab-headers\"\n  );\n  const entityFilterTabs = document.querySelectorAll(\".entity-filter-tab\");\n  entityFilterTabHeaders.addEventListener(\"click\", (e) => {\n    const el = e.target;\n    let i = 0;\n    [...el.parentElement.children].forEach((sib) => {\n      if (entityFilterTabs[i].id == el.id) {\n        entityFilterTabs[i].classList.add(\"active\");\n      } else {\n        entityFilterTabs[i].classList.remove(\"active\");\n      }\n      if (sib != el) {\n        sib.classList.remove(\"active\");\n      }\n      i++;\n    });\n    el.classList.add(\"active\");\n  });\n} catch (error) {\n  console.log(error);\n}\n\n// contact-us scroll\ntry {\n  const contactUsButtonDesktop = document.getElementById(\"contact-us-desktop\");\n  const contactUsButtonMobile = document.getElementById(\"contact-us-mobile\");\n  function scrollToButton(e) {\n    e.stopPropagation();\n    e.preventDefault();\n    window.scrollTo(0, document.body.scrollHeight);\n  }\n  function scrollToTop(e) {\n    e.stopPropagation();\n    e.preventDefault();\n    window.scrollTo(0, 0);\n  }\n  contactUsButtonDesktop.addEventListener(\"click\", scrollToButton);\n  contactUsButtonMobile.addEventListener(\"click\", scrollToButton);\n} catch (error) {}\n\n// top-top scroll\nconst toTopButton = document.getElementById(\"to-top\");\ntoTopButton.addEventListener(\"click\", scrollToTop);\n\n\n//# sourceURL=webpack:///./src/main.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/main.js"]();
/******/ 	
/******/ })()
;