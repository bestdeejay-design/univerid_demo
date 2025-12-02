#!/usr/bin/env python3
"""
Script to update university pages with standard header and footer - Group 4
"""

import os
import re

def update_university_page(filepath):
    """Update a single university page with standard header and footer"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the main content between the existing header and footer
    # Find the main content section
    main_content_match = re.search(r'<main id="mainContent">(.*)</main>', content, re.DOTALL)
    
    if main_content_match:
        main_content = main_content_match.group(1)
    else:
        # If no main content section found, use the content between body tags
        body_match = re.search(r'<body>(.*)</body>', content, re.DOTALL)
        if body_match:
            main_content = body_match.group(1)
        else:
            main_content = content

    # Create the new page structure based on the template
    new_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{get_title_from_content(content)}</title>
  <link rel="stylesheet" href="styles/main.css">
</head>
<body>
  <div class="container">
        <header>
      <div class="header-content">
        <a href="index.html" class="logo" aria-label="UniveriD - Главная страница">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M2 17L12 22L22 17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M2 12L12 17L22 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          UniveriD
        </a>
        <div class="header-right">
          <nav class="desktop-nav" aria-label="Основная навигация">
            <a href="index.html">Главная</a>
            <a href="features.html">Возможности</a>
            <a href="about.html">О проекте</a>
            <a href="universities.html">Вузы</a>
            <a href="partners.html">Партнёрам</a>
          </nav>
          <button class="theme-toggle" id="themeToggle" aria-label="Сменить тему"></button>
          <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Меню">☰</button>
        </div>
      </div>
      <nav class="mobile-nav" id="mobileNav" aria-label="Мобильное меню">
        <a href="index.html">Главная</a>
        <a href="features.html">Возможности</a>
        <a href="about.html">О проекте</a>
        <a href="universities.html">Вузы</a>
        <a href="partners.html">Партнёрам</a>
        <button class="theme-toggle mobile" id="mobileThemeToggle" aria-label="Сменить тему (моб.)"></button>
      </nav>
    </header>

    <main id="mainContent">
      {main_content.strip()}
    </main>
  </div>

    <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3>UniveriD</h3>
          <ul>
            <li><a href="index.html">Главная</a></li>
            <li><a href="about.html">О проекте</a></li>
            <li><a href="universities.html">Вузы Петербурга</a></li>
            <li><a href="partners.html">Партнёрам</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Контакты</h3>
          <ul>
            <li>📧 hello@univerid.ru</li>
            <li>📱 Telegram: @univerid_support</li>
          </ul>
        </div>
        <div class="footer-section">
          <h3>Для вузов</h3>
          <ul>
            <li><a href="for-universities.html">Интеграция с СЗИ</a></li>
            <li><a href="for-universities.html">API для партнёров</a></li>
            <li><a href="for-universities.html">Техническая документация</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2025 UniveriD. Цифровая студенческая жизнь — в одном QR-коде.</p>
      </div>
    </div>
  </footer>

    <script src="js/main.js"></script>
</body>
</html>"""
    
    # Write the updated content back to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated: {filepath}")

def get_title_from_content(content):
    """Extract the title from the original content"""
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        return title_match.group(1)
    else:
        return "University Page | UniveriD"

def main():
    # List of the fourth 15 university files to update
    university_files = [
        "спбгикмт-university.html",
        "спбгикт-university.html",
        "спбгилс-university.html",
        "спбгипи-university.html",
        "спбгипср-university.html",
        "спбгисэ-university.html",
        "спбгитб-university.html",
        "спбгити-university.html",
        "спбгитмо-university.html",
        "спбгитму-морская-академия-university.html",
        "спбгиту-бывш-литмо-university.html",
        "спбгитэ-university.html",
        "спбгиу-university.html",
        "спбгиэп-university.html",
        "спбгиэу-university.html"
    ]
    
    for filename in university_files:
        filepath = os.path.join("/workspace", filename)
        if os.path.exists(filepath):
            update_university_page(filepath)
        else:
            print(f"File not found: {filepath}")

if __name__ == "__main__":
    main()