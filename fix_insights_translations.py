import re

html_path = r'c:\Users\taiwe\Desktop\cleaning\index.html'
js_path = r'c:\Users\taiwe\Desktop\cleaning\script.js'

# 1. Remove Insights section from HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Use regex to find and remove the <section id="insights"> block
insights_pattern = re.compile(r'<!-- INDUSTRY INSIGHTS -->\s*<section id="insights".*?</section>', re.DOTALL)
html = re.sub(insights_pattern, '', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Fix JS Translations for MS and ZH
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Clean up EN translations to remove 'ins_' keys since insights is deleted
en_to_remove = r', ins_label: "Knowledge Base", ins_title: "Industry Insights & Case Studies", ins_1_title: "How ISO 9001:2015 Cleaners Save JMBs Hidden Costs", ins_1_desc: "Choosing the cheapest contractor often leads to damaged assets and resident complaints. Discover how our rigorous SOPs reduce long-term maintenance costs for luxury condominiums.", ins_2_title: "Commercial Carpet Cleaning: Shampooing vs. Hot Water Extraction", ins_2_desc: "Not all carpet cleaning is equal. Learn why we use industrial-grade Numatic steam extractors to remove deep-seated allergens and extend the lifespan of your corporate carpets.", ins_3_title: "High-Rise Facade Safety: Behind the Scenes at The Avare", ins_3_desc: "Exterior glass cleaning at 40 stories high requires more than just courage. Read our case study on how our certified rope-access technicians execute zero-accident facade washing.", ins_readmore: "Read More &rarr;"'
js = js.replace(en_to_remove, '')

# We need to inject faq_ and acc_ for ms and zh
ms_str = ', faq_title: "Soalan Lazim", faq_q1: "Adakah pekerja pembersihan anda digaji secara sah dan dilindungi insurans sepenuhnya?", faq_a1: "Ya. Dengan tenaga kerja operasi lebih 300 kakitangan, kami mematuhi undang-undang buruh Malaysia dengan ketat. Semua pekerja kami memegang permit sah, dilindungi sepenuhnya oleh PERKESO dan CIDB, serta menjalani latihan berterusan di bawah Sistem Pengurusan Kualiti ISO 9001:2015 kami.", faq_q2: "Adakah anda menyediakan jentera dan bahan kimia pembersihan anda sendiri?", faq_a2: "Sudah tentu. Kami membekalkan jentera gred komersial, termasuk pengekstrak Numatic yang diimport dari UK dan penggilap kelajuan tinggi Virco. Kami juga menyediakan semua bahan kimia piawai (cth., 3M Polish, Wax Strippers) berserta dengan Helaian Data Keselamatan Bahan (MSDS) untuk mematuhi piawaian ESG dan keselamatan yang ketat.", faq_q3: "Berapakah biasanya kos kontrak pembersihan komersial?", faq_a3: "Harga kontrak bergantung kepada saiz hartanah dan jumlah pekerja yang diperlukan. Untuk pembersihan B2B yang disahkan ISO, sebut harga telus kami biasanya mencerminkan kos buruh langsung (anggaran RM 2,500 - RM 3,500 setiap pekerja sebulan, meliputi gaji minimum, KWSP, PERKESO, dan Levi), ditambah dengan pelunasan mesin berat. Kami tidak terlibat dalam perang harga; sebaliknya, kami menjamin standard sedia audit dan sifar caj tersembunyi.", faq_q4: "Berapakah masa tindak balas anda untuk kecemasan atau isu ad-hoc?", faq_a4: "HC Cleaning beroperasi dengan pasukan pengurusan yang sangat berpengalaman. Pengurus Operasi kami (pengalaman 38 tahun) dan Penyelia Kawasan (purata pengalaman 15-30 tahun) memantau zon khusus setiap hari. Kami menjamin tindak balas segera kepada sebarang aduan atau permintaan pembersihan ad-hoc kecemasan di sekitar Lembah Klang.", acc_title: "Pilihan Aksesibiliti", acc_text: "Teks Besar", acc_contrast: "Kontras Tinggi", acc_links: "Serlahkan Pautan"'

zh_str = ', faq_title: "常见问题解答", faq_q1: "贵公司的清洁员工是否合法受雇且享有全额保险？", faq_a1: "是的。我们拥有超过 300 名运营人员，严格遵守马来西亚劳工法。所有清洁工均持有合法准证，享有 SOCSO 和 CIDB 的全面保障，并在我们的 ISO 9001:2015 质量管理体系下接受持续培训。", faq_q2: "你们提供自己的清洁机械和化学品吗？", faq_a2: "绝对提供。我们供应商业级机械，包括英国进口的 Numatic 抽洗机和 Virco 高速抛光机。我们还提供所有必要的标准化化学品（例如，3M 抛光剂、起蜡水），并附带材料安全数据表（MSDS），以符合严格的 ESG 和安全标准。", faq_q3: "商业清洁合约通常需要多少费用？", faq_a3: "合约价格取决于物业面积和所需人数。对于通过 ISO 认证的 B2B 清洁服务，我们透明的报价通常反映直接劳动力成本（按每月每人约 RM 2,500 - RM 3,500 计算，涵盖最低工资、EPF、SOCSO 和外劳人头税），再加上重型机械的折旧。我们不参与价格战；相反，我们保证符合审计标准，绝无隐形收费。", faq_q4: "对于紧急或临时问题，你们的响应时间是多长？", faq_a4: "HC Cleaning 拥有一支经验丰富的管理团队。我们的运营经理（38年经验）和区域主管（平均15-30年经验）每天监控特定区域。我们保证对巴生谷范围内的任何投诉或紧急临时清洁请求做出迅速响应。", acc_title: "无障碍选项", acc_text: "放大字体", acc_contrast: "高对比度", acc_links: "高亮链接"'

# Insert for MS
# Find chat_err_net: "Ralat rangkaian. Sila cuba lagi."
js = js.replace('chat_err_net: "Ralat rangkaian. Sila cuba lagi."', 'chat_err_net: "Ralat rangkaian. Sila cuba lagi."' + ms_str)

# Insert for ZH
# Find chat_err_net: "网络错误，请重试。"
js = js.replace('chat_err_net: "网络错误，请重试。"', 'chat_err_net: "网络错误，请重试。"' + zh_str)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Insights deleted and translations fixed.")
