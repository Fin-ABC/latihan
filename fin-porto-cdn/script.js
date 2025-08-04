// toggle menu mobile
function toggleMenu() {
  const mobileMenu = document.getElementById("mobileMenu");
  mobileMenu.classList.toggle("hidden");
}

// Hamburger
const hamburger = document.querySelector('#hamburger');
const navMenu = document.querySelector('#nav-menu');

hamburger.addEventListener('click', function () {
  hamburger.classList.toggle('hamburger-active');
  navMenu.classList.toggle('hidden');
});

// Klik di luar hamburger
window.addEventListener('click', function (e) {
  if (e.target != hamburger && e.target != navMenu) {
    hamburger.classList.remove('hamburger-active');
    navMenu.classList.add('hidden');
  }
});


// Dark mode
const darkToggle = document.querySelector("#dark-toggle");
const light_icon = document.querySelector("#light-svg");
const dark_icon = document.querySelector("#dark-svg");
const html = document.querySelector("html");

darkToggle.addEventListener("click", function () {
  if (darkToggle.checked) {
    tambahClass(html, "dark");
    tambahClass(light_icon, "hidden");
    hapusClass(light_icon, "visible");
    tambahClass(dark_icon, "visible");
    hapusClass(dark_icon, "hidden");
    localStorage.theme = "dark";
  } else {
    hapusClass(html, "dark");
    hapusClass(light_icon, "hidden");
    tambahClass(light_icon, "visible");
    hapusClass(dark_icon, "visible");
    tambahClass(dark_icon, "hidden");
    localStorage.theme = "light";
  }
});

// func tambah class
function tambahClass(id, status) {
  id.classList.add(status);
}

// func hapus class
function hapusClass(id, status) {
  id.classList.remove(status);
}

if (
  localStorage.theme === "dark" ||
  (!("theme" in localStorage) &&
    window.matchMedia("(prefers-color-scheme: dark)").matches)
) {
  darkToggle.checked = true;
} else {
  darkToggle.checked = false;
}
