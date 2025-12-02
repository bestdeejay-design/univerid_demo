#!/usr/bin/env python3
"""
Скрипт для унификации HTML-страниц сайта UniveriD
Приводит все страницы к единому шаблону с общей структурой, CSS и JS
"""

import os
import re
from pathlib import Path

# Основные страницы для унификации
main_pages = [
    'abiturients.html',
    'about.html',
    'alumni.html',
    'benefits.html',
    'career.html',
    'demo.html',
    'ecology.html',
    'features.html',
    'for-universities.html',
    'housing.html',
    'index.html',
    'partners.html',
    'science.html',
    'support.html',
    'template.html',
    'universities.html'
]

def get_page_title(filename):
    """Определяет заголовок страницы на основе её названия"""
    titles = {
        'abiturients.html': 'UniveriD — Для абитуриентов',
        'about.html': 'UniveriD — О проекте',
        'alumni.html': 'UniveriD — Выпускникам',
        'benefits.html': 'UniveriD — Выгоды',
        'career.html': 'UniveriD — Карьера и стажировки',
        'demo.html': 'UniveriD — Демонстрация',
        'ecology.html': 'UniveriD — Экология',
        'features.html': 'UniveriD — Возможности',
        'for-universities.html': 'UniveriD — Вузам и колледжам',
        'housing.html': 'UniveriD — Общежития',
        'index.html': 'UniveriD — Цифровая студенческая жизнь',
        'partners.html': 'UniveriD — Партнёрам',
        'science.html': 'UniveriD — Наука',
        'support.html': 'UniveriD — Поддержка',
        'template.html': 'UniveriD — Шаблон',
        'universities.html': 'UniveriD — Вузы и колледжи'
    }
    return titles.get(filename, f'UniveriD — {filename.replace(".html", "").replace("-", " ").title()}')

def create_unified_header():
    """Создает унифицированный заголовок страницы"""
    return '''  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title}</title>
  <link rel="stylesheet" href="styles/main.css">
'''

def create_unified_nav():
    """Создает унифицированную навигацию"""
    return '''    <header>
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
    </header>'''

def create_unified_footer():
    """Создает унифицированный футер"""
    return '''  <footer>
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
  </footer>'''

def create_unified_scripts():
    """Создает унифицированные скрипты"""
    return '''  <script src="js/main.js"></script>'''

def process_html_file(filepath):
    """Обрабатывает один HTML-файл для унификации"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    title = get_page_title(filename)
    
    # Заменяем заголовок документа
    head_pattern = r'<head>.*?</head>'
    new_head_content = create_unified_header().format(title=title)
    new_head = f'<head>\n{new_head_content}</head>'
    content = re.sub(head_pattern, new_head, content, flags=re.DOTALL)
    
    # Заменяем header
    header_pattern = r'<header>.*?</header>'
    new_header = create_unified_nav()
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
    
    # Заменяем footer
    footer_pattern = r'<footer>.*?</footer>'
    new_footer = create_unified_footer()
    content = re.sub(footer_pattern, new_footer, content, flags=re.DOTALL)
    
    # Заменяем скрипты
    script_pattern = r'<script\s+src="[^"]*"></script>'
    new_script = create_unified_scripts()
    content = re.sub(script_pattern, new_script, content)
    
    # Убедимся, что контейнер есть
    if '<div class="container">' not in content and '<main>' in content:
        # Оборачиваем основной контент в контейнер
        content = content.replace('<main>', '<div class="container"><main>')
        if '</main>' in content:
            content = content.replace('</main>', '</main></div>')
        else:
            # Если нет закрывающего тега main, добавим контейнер перед footer
            content = content.replace('<footer>', '</div><footer>')
    
    # Заменяем специфичные стили для определенных страниц
    if filename == 'abiturients.html':
        # Добавляем специфичные стили для абитуриентов, если их нет
        if ':root {\n      --accent: #e74c3c;' not in content:
            # Найти место перед закрывающим тегом </head>
            head_end_pos = content.find('</head>')
            if head_end_pos != -1:
                custom_styles = '''
  <style>
    :root {
      --accent: #e74c3c;
    }
    
    .abitur-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
      margin: 24px 0;
    }
    
    .abitur-card {
      background: var(--light-gray);
      padding: 20px;
      border-radius: 12px;
      border-top: 4px solid var(--accent);
    }
    
    .abitur-card h3 {
      font-size: 1.15rem;
      margin-bottom: 12px;
      color: var(--accent);
    }
  </style>'''
                content = content[:head_end_pos] + custom_styles + content[head_end_pos:]
    
    elif filename == 'features.html':
        # Добавляем специфичные стили для возможностей, если их нет
        if '.features-grid' not in content:
            # Найти место перед закрывающим тегом </head>
            head_end_pos = content.find('</head>')
            if head_end_pos != -1:
                custom_styles = '''
  <style>
    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 30px;
      margin: 40px 0;
    }
    
    .feature-category {
      background: var(--light-gray);
      padding: 25px;
      border-radius: 16px;
      border-left: 4px solid var(--accent);
    }
    
    .feature-category h3 {
      color: var(--accent);
      margin-bottom: 15px;
    }
    
    .feature-list {
      list-style: none;
      padding: 0;
    }
    
    .feature-list li {
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
    }
    
    .feature-list li:last-child {
      border-bottom: none;
    }
  </style>'''
                content = content[:head_end_pos] + custom_styles + content[head_end_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Обработан файл: {filename}")

def main():
    workspace_path = Path('/workspace')
    
    for page in main_pages:
        filepath = workspace_path / page
        if filepath.exists():
            process_html_file(filepath)
        else:
            print(f"Файл не найден: {page}")
    
    print("Все страницы унифицированы!")

if __name__ == "__main__":
    main()