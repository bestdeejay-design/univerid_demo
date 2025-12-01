// Общие функции для всех страниц

// Тема
const themeToggle = document.getElementById('themeToggle');
const mobileThemeToggle = document.getElementById('mobileThemeToggle');
const body = document.body;
const isDark = localStorage.getItem('univerid-theme') === 'dark';

if (isDark) {
  body.classList.add('dark');
}

function syncTheme() {
  const isNowDark = body.classList.contains('dark');
  if (mobileThemeToggle) {
    if (isNowDark) {
      mobileThemeToggle.classList.add('dark');
    } else {
      mobileThemeToggle.classList.remove('dark');
    }
  }
}

function toggleTheme() {
  body.classList.toggle('dark');
  localStorage.setItem('univerid-theme', body.classList.contains('dark') ? 'dark' : 'light');
  syncTheme();
}

if (themeToggle) {
  themeToggle.addEventListener('click', toggleTheme);
}
if (mobileThemeToggle) {
  mobileThemeToggle.addEventListener('click', toggleTheme);
}

// Мобильное меню
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const mobileNav = document.getElementById('mobileNav');

if (mobileMenuToggle && mobileNav) {
  mobileMenuToggle.addEventListener('click', () => {
    mobileNav.classList.toggle('active');
  });

  // Закрытие при клике на ссылку
  mobileNav.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileNav.classList.remove('active');
    });
  });
}

// Инициализация темы
syncTheme();