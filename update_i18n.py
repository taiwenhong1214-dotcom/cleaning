import re

with open(r'c:\Users\taiwe\Desktop\cleaning\script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Add to EN
en_add = 'dl_btn: "Get PDF File", dl_pdpa: "By submitting, you agree to our Privacy Policy regarding the storage of your contact details.", dl_success:'
content = content.replace('dl_btn: "Get PDF File", dl_success:', en_add)

en_footer = 'footer_copy: "© 2026 All Rights Reserved. ISO 9001:2015 Certified.", footer_privacy: "Privacy Policy", footer_terms: "Terms of Service",'
content = content.replace('footer_copy: "© 2026 All Rights Reserved. ISO 9001:2015 Certified.",', en_footer)

# Add to MS
ms_add = 'dl_btn: "Dapatkan Fail PDF", dl_pdpa: "Dengan menyerahkan borang ini, anda bersetuju dengan Dasar Privasi kami mengenai penyimpanan butiran hubungan anda.", dl_success:'
content = content.replace('dl_btn: "Dapatkan Fail PDF", dl_success:', ms_add)

ms_footer = 'footer_copy: "© 2026 Hak Cipta Terpelihara. Disahkan ISO 9001:2015.", footer_privacy: "Dasar Privasi", footer_terms: "Terma Perkhidmatan",'
content = content.replace('footer_copy: "© 2026 Hak Cipta Terpelihara. Disahkan ISO 9001:2015.",', ms_footer)

# Add to ZH
zh_add = 'dl_btn: "获取 PDF 文件", dl_pdpa: "提交即表示您同意我们关于存储您联系方式的隐私政策。", dl_success:'
content = content.replace('dl_btn: "获取 PDF 文件", dl_success:', zh_add)

zh_footer = 'footer_copy: "© 2026 版权所有。ISO 9001:2015 认证企业。", footer_privacy: "隐私政策", footer_terms: "服务条款",'
content = content.replace('footer_copy: "© 2026 版权所有。ISO 9001:2015 认证企业。",', zh_footer)

with open(r'c:\Users\taiwe\Desktop\cleaning\script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Translation strings added.")
