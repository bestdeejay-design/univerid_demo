#!/usr/bin/env python3
"""
Скрипт для обновления HTML-файлов с использованием внешних CSS и JS файлов
"""

import os
import re

def update_html_file(filepath):
    """Обновляет HTML-файл, заменяя встроенные стили и скрипты на внешние"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Обновление head: замена встроенных стилей на внешние
    # Находим начало и конец встроенных стилей
    head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
    if head_match:
        head_content = head_match.group(1)
        
        # Удаляем встроенные стили и добавляем внешние
        updated_head = re.sub(r'\s*<style[^>]*>.*?</style>\s*', '', head_content, flags=re.DOTALL)
        # Удаляем возможные ссылки на main.css, если они есть, чтобы избежать дублирования
        updated_head = re.sub(r'<link rel="stylesheet" href="styles/main\.css"[^>]*/?>\s*', '', updated_head)
        
        # Добавляем ссылку на main.css
        if '<link rel="stylesheet"' not in updated_head:
            # Найти позицию для вставки после meta тегов
            meta_end_pos = updated_head.rfind('>')
            if meta_end_pos != -1:
                insert_pos = meta_end_pos + 1
                updated_head = updated_head[:insert_pos] + '\n  <link rel="stylesheet" href="styles/main.css">' + updated_head[insert_pos:]
        
        # Заменяем старый head на обновленный
        content = content.replace(head_match.group(0), f'<head>{updated_head}</head>')
    
    # Обновление footer: замена встроенных скриптов на внешний
    if '<script src="js/main.js"></script>' not in content:
        # Заменяем встроенные скрипты на внешний файл
        content = re.sub(r'\s*<script>\s*// Тема.*?</script>\s*</body>', '  <script src="js/main.js"></script>\n</body>', content, flags=re.DOTALL)
        content = re.sub(r'\s*<script>\s*// Общие функции для всех страниц.*?</script>\s*</body>', '  <script src="js/main.js"></script>\n</body>', content, flags=re.DOTALL)
        content = re.sub(r'\s*<script>\s*[^<]*const themeToggle.*?</script>\s*</body>', '  <script src="js/main.js"></script>\n</body>', content, flags=re.DOTALL)
        content = re.sub(r'\s*<script>\s*[^<]*// Тема[^<]*</script>\s*</body>', '  <script src="js/main.js"></script>\n</body>', content, flags=re.DOTALL)
    
    # Обновляем header, если он не содержит SVG
    if '<svg width="24" height="24"' not in content:
        # Заменяем старый header на стандартный
        header_pattern = r'<header>.*?</header>'
        standard_header = '''    <header>
      <div class=\"header-content\">
        <a href=\"index.html\" class=\"logo\" aria-label=\"UniveriD - Главная страница\">
          <svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" xmlns=\"http://www.w3.org/2000/svg\">
            <path d=\"M12 2L2 7L12 12L22 7L12 2Z\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>
            <path d=\"M2 17L12 22L22 17\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>
            <path d=\"M2 12L12 17L22 12\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"/>
          </svg>
          UniveriD
        </a>
        <div class=\"header-right\">
          <nav class=\"desktop-nav\" aria-label=\"Основная навигация\">
            <a href=\"index.html\">Главная</a>
            <a href=\"features.html\">Возможности</a>
            <a href=\"about.html\">О проекте</a>
            <a href=\"universities.html\">Вузы</a>
            <a href=\"partners.html\">Партнёрам</a>
          </nav>
          <button class=\"theme-toggle\" id=\"themeToggle\" aria-label=\"Сменить тему\"></button>
          <button class=\"mobile-menu-toggle\" id=\"mobileMenuToggle\" aria-label=\"Меню\">☰</button>
        </div>
      </div>
      <nav class=\"mobile-nav\" id=\"mobileNav\" aria-label=\"Мобильное меню\">
        <a href=\"index.html\">Главная</a>
        <a href=\"features.html\">Возможности</a>
        <a href=\"about.html\">О проекте</a>
        <a href=\"universities.html\">Вузы</a>
        <a href=\"partners.html\">Партнёрам</a>
        <button class=\"theme-toggle mobile\" id=\"mobileThemeToggle\" aria-label=\"Сменить тему (моб.)\"></button>
      </nav>
    </header>'''
        
        content = re.sub(header_pattern, standard_header, content, flags=re.DOTALL)
    
    # Обновляем footer, если в нем отсутствует правильная навигация
    if '<li><a href="features.html">Возможности</a></li>' in content:
        # Это означает, что в footer есть ссылка на features, значит footer уже правильный
        pass
    else:
        # Заменяем footer на стандартный
        footer_pattern = r'<footer>.*?</footer>'
        standard_footer = '''  <footer>
    <div class=\"container\">
      <div class=\"footer-content\">
        <div class=\"footer-section\">
          <h3>UniveriD</h3>
          <ul>
            <li><a href=\"index.html\">Главная</a></li>
            <li><a href=\"about.html\">О проекте</a></li>
            <li><a href=\"universities.html\">Вузы Петербурга</a></li>
            <li><a href=\"partners.html\">Партнёрам</a></li>
          </ul>
        </div>
        <div class=\"footer-section\">
          <h3>Контакты</h3>
          <ul>
            <li>📧 hello@univerid.ru</li>
            <li>📱 Telegram: @univerid_support</li>
          </ul>
        </div>
        <div class=\"footer-section\">
          <h3>Для вузов</h3>
          <ul>
            <li><a href=\"for-universities.html\">Интеграция с СЗИ</a></li>
            <li><a href=\"for-universities.html\">API для партнёров</a></li>
            <li><a href=\"for-universities.html\">Техническая документация</a></li>
          </ul>
        </div>
      </div>
      <div class=\"footer-bottom\">
        <p>© 2025 UniveriD. Цифровая студенческая жизнь — в одном QR-коде.</p>
      </div>
    </div>
  </footer>'''
        
        content = re.sub(footer_pattern, standard_footer, content, flags=re.DOTALL)
    
    # Записываем обновленный контент обратно в файл
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Обновлен файл: {filepath}")

def main():
    # Список файлов для обновления
    files_to_update = [
        'alumni.html',
        'benefits.html',
        'career.html',
        'demo.html',
        'ecology.html',
        'for-universities.html',
        'housing.html',
        'partners.html',
        'science.html',
        'support.html',
        'universities.html',
        'about.html',
        'features.html',
        'index.html'
    ]
    
    for filename in files_to_update:
        filepath = f'/workspace/{filename}'
        if os.path.exists(filepath):
            update_html_file(filepath)
        else:
            print(f"Файл не найден: {filepath}")

if __name__ == '__main__':
    main()