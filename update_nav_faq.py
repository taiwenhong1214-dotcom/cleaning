import re

js_path = r'c:\Users\taiwe\Desktop\cleaning\script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace in EN
js = js.replace('nav_awards: "Awards", nav_quote: "Request Quotation",', 'nav_awards: "Awards", nav_faq: "FAQ", nav_quote: "Request Quotation",')

# Replace in MS
js = js.replace('nav_awards: "Anugerah", nav_quote: "Minta Sebut Harga",', 'nav_awards: "Anugerah", nav_faq: "Soalan Lazim", nav_quote: "Minta Sebut Harga",')

# Replace in ZH
js = js.replace('nav_awards: "荣誉奖项", nav_quote: "获取报价",', 'nav_awards: "荣誉奖项", nav_faq: "常见问题", nav_quote: "获取报价",')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Nav FAQ translation strings added.")
