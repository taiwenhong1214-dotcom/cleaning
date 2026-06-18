import re

html_path = r'c:\Users\taiwe\Desktop\cleaning\index.html'
css_path = r'c:\Users\taiwe\Desktop\cleaning\style.css'
js_path = r'c:\Users\taiwe\Desktop\cleaning\script.js'

# 1. Remove Access Menu from HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

access_pattern = re.compile(r'<!-- ACCESSIBILITY MENU -->.*?</button>', re.DOTALL)
html = re.sub(access_pattern, '', html)

# Cleanup any stray newlines left by the replacement before <!-- SCRIPTS -->
html = html.replace('\n\n\n<!-- SCRIPTS -->', '\n\n<!-- SCRIPTS -->')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Remove Access CSS from style.css
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Using regex to remove from /* ── ACCESSIBILITY ── */ down to the end of the file
access_css_pattern = re.compile(r'/\* ── ACCESSIBILITY ── \*/.*', re.DOTALL)
css = re.sub(access_css_pattern, '', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css.strip())

# 3. Remove Access JS functions and translations from script.js
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

js_func_pattern = re.compile(r'// Accessibility Panel.*?\}', re.DOTALL)
js = re.sub(js_func_pattern, '', js)

# Remove the translation strings
js = js.replace(', acc_title: "Accessibility Options", acc_text: "Large Text", acc_contrast: "High Contrast", acc_links: "Highlight Links"', '')
js = js.replace(', acc_title: "Pilihan Aksesibiliti", acc_text: "Teks Besar", acc_contrast: "Kontras Tinggi", acc_links: "Serlahkan Pautan"', '')
js = js.replace(', acc_title: "无障碍选项", acc_text: "放大字体", acc_contrast: "高对比度", acc_links: "高亮链接"', '')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Wheelchair (accessibility) features successfully removed.")
