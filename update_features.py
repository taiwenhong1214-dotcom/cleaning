import re
import os

html_path = r'c:\Users\taiwe\Desktop\cleaning\index.html'
css_path = r'c:\Users\taiwe\Desktop\cleaning\style.css'
js_path = r'c:\Users\taiwe\Desktop\cleaning\script.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert Insights Section
insights_html = """
<!-- INDUSTRY INSIGHTS -->
<section id="insights" data-aos="fade-up">
  <div class="section-label" data-i18n="ins_label">Knowledge Base</div>
  <h2 class="section-title" data-i18n="ins_title">Industry Insights & Case Studies</h2>
  
  <div class="services-grid" style="margin-top: 40px;">
    <div class="service-card" data-aos="fade-up" data-aos-delay="0" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <img src="https://images.unsplash.com/photo-1584820927498-cafe2c1ddcc6?w=500" alt="Condo" style="width: 100%; height: 200px; object-fit: cover;">
      <div style="padding: 30px; flex: 1; display: flex; flex-direction: column;">
        <h3 data-i18n="ins_1_title" style="font-size: 18px; font-family: 'Playfair Display', serif; margin-bottom: 10px;">How ISO 9001:2015 Cleaners Save JMBs Hidden Costs</h3>
        <p data-i18n="ins_1_desc" style="margin-bottom: 20px; font-size: 13px; color: var(--white-dim);">Choosing the cheapest contractor often leads to damaged assets and resident complaints. Discover how our rigorous SOPs reduce long-term maintenance costs for luxury condominiums.</p>
        <a href="javascript:void(0)" style="margin-top: auto; color: var(--gold); text-decoration: none; font-weight: bold; font-size: 13px; text-transform: uppercase;" data-i18n="ins_readmore">Read More &rarr;</a>
      </div>
    </div>
    
    <div class="service-card" data-aos="fade-up" data-aos-delay="100" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <img src="https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=500" alt="Carpet" style="width: 100%; height: 200px; object-fit: cover;">
      <div style="padding: 30px; flex: 1; display: flex; flex-direction: column;">
        <h3 data-i18n="ins_2_title" style="font-size: 18px; font-family: 'Playfair Display', serif; margin-bottom: 10px;">Commercial Carpet Cleaning: Shampooing vs. Hot Water Extraction</h3>
        <p data-i18n="ins_2_desc" style="margin-bottom: 20px; font-size: 13px; color: var(--white-dim);">Not all carpet cleaning is equal. Learn why we use industrial-grade Numatic steam extractors to remove deep-seated allergens and extend the lifespan of your corporate carpets.</p>
        <a href="javascript:void(0)" style="margin-top: auto; color: var(--gold); text-decoration: none; font-weight: bold; font-size: 13px; text-transform: uppercase;" data-i18n="ins_readmore">Read More &rarr;</a>
      </div>
    </div>
    
    <div class="service-card" data-aos="fade-up" data-aos-delay="200" style="padding: 0; overflow: hidden; display: flex; flex-direction: column;">
      <img src="https://images.unsplash.com/photo-1541888081691-23d90cb0e3d0?w=500" alt="Facade" style="width: 100%; height: 200px; object-fit: cover;">
      <div style="padding: 30px; flex: 1; display: flex; flex-direction: column;">
        <h3 data-i18n="ins_3_title" style="font-size: 18px; font-family: 'Playfair Display', serif; margin-bottom: 10px;">High-Rise Facade Safety: Behind the Scenes at The Avare</h3>
        <p data-i18n="ins_3_desc" style="margin-bottom: 20px; font-size: 13px; color: var(--white-dim);">Exterior glass cleaning at 40 stories high requires more than just courage. Read our case study on how our certified rope-access technicians execute zero-accident facade washing.</p>
        <a href="javascript:void(0)" style="margin-top: auto; color: var(--gold); text-decoration: none; font-weight: bold; font-size: 13px; text-transform: uppercase;" data-i18n="ins_readmore">Read More &rarr;</a>
      </div>
    </div>
  </div>
</section>
"""
if "<!-- INDUSTRY INSIGHTS -->" not in html:
    html = html.replace('<!-- BEFORE AND AFTER -->', insights_html + '\n<!-- BEFORE AND AFTER -->')

# 2. Insert FAQ Section
faq_html = """
        <div class="faq-section" style="margin-top: 40px;">
          <h3 style="font-family: 'Playfair Display', serif; color: var(--gold); font-size: 22px; margin-bottom: 20px;" data-i18n="faq_title">Frequently Asked Questions</h3>
          
          <div class="faq-item active">
            <div class="faq-q" onclick="toggleFaq(this)" data-i18n="faq_q1">Are your cleaners legally employed and fully insured?</div>
            <div class="faq-a" data-i18n="faq_a1">Yes. With an operational workforce of over 300 dedicated personnel, we strictly comply with Malaysia’s labor laws. All our cleaners hold valid permits, are fully covered by SOCSO and CIDB, and undergo continuous training under our ISO 9001:2015 Quality Management System.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="toggleFaq(this)" data-i18n="faq_q2">Do you provide your own cleaning machinery and chemicals?</div>
            <div class="faq-a" data-i18n="faq_a2">Absolutely. We supply commercial-grade machinery, including UK-imported Numatic extractors and Virco high-speed burnishers. We also provide all necessary standardized chemicals (e.g., 3M Polish, Wax Strippers) accompanied by Material Safety Data Sheets (MSDS) to comply with stringent ESG and safety standards.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="toggleFaq(this)" data-i18n="faq_q3">How much does a commercial cleaning contract usually cost?</div>
            <div class="faq-a" data-i18n="faq_a3">Contract pricing depends on property size and required headcount. For ISO-certified B2B cleaning, our transparent quotation typically reflects direct labor costs (approx. RM 2,500 - RM 3,500 per headcount monthly, covering minimum wage, EPF, SOCSO, and Levy), plus the amortization of heavy machinery. We do not engage in price wars; instead, we guarantee audit-ready standards and zero hidden charges.</div>
          </div>
          <div class="faq-item">
            <div class="faq-q" onclick="toggleFaq(this)" data-i18n="faq_q4">What is your response time for emergencies or ad-hoc issues?</div>
            <div class="faq-a" data-i18n="faq_a4">HC Cleaning operates with a highly experienced management team. Our Operation Manager (38 years experience) and Area Supervisors (averaging 15-30 years of experience) monitor specific zones daily. We guarantee a prompt response to any complaints or emergency ad-hoc cleaning requests within the Klang Valley.</div>
          </div>
        </div>
"""
if "class=\"faq-section\"" not in html:
    html = html.replace('<div style="margin-top: 40px; border-radius: 8px;', faq_html + '\n        <div style="margin-top: 40px; border-radius: 8px;')

# 3. Insert Access Menu
access_html = """
<!-- ACCESSIBILITY MENU -->
<div class="access-panel" id="accessPanel">
  <h4 data-i18n="acc_title">Accessibility Options</h4>
  <button onclick="toggleAccessClass('large-text')" data-i18n="acc_text">Large Text</button>
  <button onclick="toggleAccessClass('high-contrast')" data-i18n="acc_contrast">High Contrast</button>
  <button onclick="toggleAccessClass('highlight-links')" data-i18n="acc_links">Highlight Links</button>
</div>
<button class="access-btn" onclick="toggleAccessPanel()">&#9855;</button>
"""
if "class=\"access-panel\"" not in html:
    html = html.replace('<!-- SCRIPTS -->', access_html + '\n<!-- SCRIPTS -->')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# CSS Update
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if "/* ── FAQ ── */" not in css:
    css_add = """
  /* ── FAQ ── */
  .faq-item { border: 1px solid var(--border); border-radius: 6px; margin-bottom: 10px; background: rgba(255,255,255,0.02); overflow: hidden; }
  .faq-q { padding: 15px 20px; cursor: pointer; font-weight: 600; font-size: 14px; position: relative; color: var(--white); transition: 0.3s; }
  .faq-q::after { content: '+'; position: absolute; right: 20px; top: 15px; font-size: 18px; color: var(--gold); transition: 0.3s; line-height: 1;}
  .faq-item.active .faq-q { color: var(--gold); }
  .faq-item.active .faq-q::after { content: '\\2212'; transform: rotate(180deg); }
  .faq-a { padding: 0 20px; max-height: 0; font-size: 13px; color: var(--white-dim); transition: all 0.4s ease; opacity: 0; line-height: 1.6; }
  .faq-item.active .faq-a { padding: 0 20px 20px; max-height: 500px; opacity: 1; }

  /* ── ACCESSIBILITY ── */
  .access-btn { position: fixed; bottom: 30px; left: 30px; width: 60px; height: 60px; background: var(--navy-mid); border: 1px solid var(--border); border-radius: 50%; color: var(--white); font-size: 30px; display: flex; align-items: center; justify-content: center; cursor: pointer; z-index: 10000; transition: 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
  .access-btn:hover { background: var(--gold); color: var(--navy); transform: scale(1.1); }
  .access-panel { position: fixed; bottom: 105px; left: 30px; background: var(--navy-mid); border: 1px solid var(--border); border-radius: 8px; padding: 20px; z-index: 10000; display: none; flex-direction: column; gap: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.6); min-width: 200px;}
  .access-panel.show { display: flex; }
  .access-panel h4 { color: var(--gold); font-size: 15px; margin-bottom: 5px; font-family: 'Playfair Display', serif; }
  .access-panel button { background: rgba(255,255,255,0.05); color: var(--white); border: 1px solid var(--border); padding: 10px 15px; border-radius: 4px; cursor: pointer; font-size: 13px; text-align: left; transition: 0.3s; }
  .access-panel button:hover, .access-panel button.active { background: var(--gold); color: var(--navy); font-weight: bold;}

  /* Accessibility Classes */
  body.large-text { font-size: 110%; }
  body.large-text h1, body.large-text h2, body.large-text h3 { font-size: 110%; }
  body.large-text .nav-links a { font-size: 15px; }
  body.large-text .faq-q { font-size: 16px; }
  body.large-text .faq-a { font-size: 15px; }
  
  body.high-contrast { background: #000; color: #fff; }
  body.high-contrast * { border-color: #fff !important; }
  body.high-contrast .hero::after { opacity: 0; }
  body.high-contrast .service-card, body.high-contrast .faq-item, body.high-contrast .form-box { background: #000; }
  
  body.highlight-links a { text-decoration: underline !important; background: yellow !important; color: black !important; padding: 2px; }
  body.highlight-links .btn-primary { background: yellow !important; color: black !important; border: 2px solid black !important;}
"""
    css = css + css_add
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# JS Updates
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

if "function toggleFaq" not in js:
    js_add = """
  // FAQ Accordion
  function toggleFaq(el) {
    const item = el.parentElement;
    // Optional: close other open items
    // document.querySelectorAll('.faq-item').forEach(i => { if(i !== item) i.classList.remove('active'); });
    item.classList.toggle('active');
  }

  // Accessibility Panel
  function toggleAccessPanel() {
    document.getElementById('accessPanel').classList.toggle('show');
  }
  function toggleAccessClass(className) {
    document.body.classList.toggle(className);
    event.target.classList.toggle('active');
  }
"""
    js = js + js_add

# I18N additions
def replace_i18n(lang_key, new_strings):
    global js
    # Find where the lang ends, usually just before the next lang key or end of object
    # It's a bit tricky to parse JSON-like JS object with regex easily, let's just append to the chat_err_net line
    target = f'chat_err_net: "Network error. Please try again."\n    }},'
    if lang_key == 'en':
        target = f'chat_err_net: "Network error. Please try again."\n    }},'
        replacement = f'chat_err_net: "Network error. Please try again.",\n      {new_strings}\n    }},'
    elif lang_key == 'ms':
        target = f'chat_err_net: "Ralat rangkaian. Sila cuba lagi."\n    }},'
        replacement = f'chat_err_net: "Ralat rangkaian. Sila cuba lagi.",\n      {new_strings}\n    }},'
    elif lang_key == 'zh':
        target = f'chat_err_net: "网络错误，请重试。"\n    }}'
        replacement = f'chat_err_net: "网络错误，请重试。",\n      {new_strings}\n    }}'
        
    if new_strings[:10] not in js:
        js = js.replace(target, replacement)

en_str = 'faq_title: "Frequently Asked Questions", faq_q1: "Are your cleaners legally employed and fully insured?", faq_a1: "Yes. With an operational workforce of over 300 dedicated personnel, we strictly comply with Malaysia’s labor laws. All our cleaners hold valid permits, are fully covered by SOCSO and CIDB, and undergo continuous training under our ISO 9001:2015 Quality Management System.", faq_q2: "Do you provide your own cleaning machinery and chemicals?", faq_a2: "Absolutely. We supply commercial-grade machinery, including UK-imported Numatic extractors and Virco high-speed burnishers. We also provide all necessary standardized chemicals (e.g., 3M Polish, Wax Strippers) accompanied by Material Safety Data Sheets (MSDS) to comply with stringent ESG and safety standards.", faq_q3: "How much does a commercial cleaning contract usually cost?", faq_a3: "Contract pricing depends on property size and required headcount. For ISO-certified B2B cleaning, our transparent quotation typically reflects direct labor costs (approx. RM 2,500 - RM 3,500 per headcount monthly, covering minimum wage, EPF, SOCSO, and Levy), plus the amortization of heavy machinery. We do not engage in price wars; instead, we guarantee audit-ready standards and zero hidden charges.", faq_q4: "What is your response time for emergencies or ad-hoc issues?", faq_a4: "HC Cleaning operates with a highly experienced management team. Our Operation Manager (38 years experience) and Area Supervisors (averaging 15-30 years of experience) monitor specific zones daily. We guarantee a prompt response to any complaints or emergency ad-hoc cleaning requests within the Klang Valley.", ins_label: "Knowledge Base", ins_title: "Industry Insights & Case Studies", ins_1_title: "How ISO 9001:2015 Cleaners Save JMBs Hidden Costs", ins_1_desc: "Choosing the cheapest contractor often leads to damaged assets and resident complaints. Discover how our rigorous SOPs reduce long-term maintenance costs for luxury condominiums.", ins_2_title: "Commercial Carpet Cleaning: Shampooing vs. Hot Water Extraction", ins_2_desc: "Not all carpet cleaning is equal. Learn why we use industrial-grade Numatic steam extractors to remove deep-seated allergens and extend the lifespan of your corporate carpets.", ins_3_title: "High-Rise Facade Safety: Behind the Scenes at The Avare", ins_3_desc: "Exterior glass cleaning at 40 stories high requires more than just courage. Read our case study on how our certified rope-access technicians execute zero-accident facade washing.", ins_readmore: "Read More &rarr;", acc_title: "Accessibility Options", acc_text: "Large Text", acc_contrast: "High Contrast", acc_links: "Highlight Links"'

ms_str = 'faq_title: "Soalan Lazim", faq_q1: "Adakah pekerja pembersihan anda digaji secara sah dan dilindungi insurans sepenuhnya?", faq_a1: "Ya. Dengan tenaga kerja operasi lebih 300 kakitangan, kami mematuhi undang-undang buruh Malaysia dengan ketat. Semua pekerja kami memegang permit sah, dilindungi sepenuhnya oleh PERKESO dan CIDB, serta menjalani latihan berterusan di bawah Sistem Pengurusan Kualiti ISO 9001:2015 kami.", faq_q2: "Adakah anda menyediakan jentera dan bahan kimia pembersihan anda sendiri?", faq_a2: "Sudah tentu. Kami membekalkan jentera gred komersial, termasuk pengekstrak Numatic yang diimport dari UK dan penggilap kelajuan tinggi Virco. Kami juga menyediakan semua bahan kimia piawai (cth., 3M Polish, Wax Strippers) berserta dengan Helaian Data Keselamatan Bahan (MSDS) untuk mematuhi piawaian ESG dan keselamatan yang ketat.", faq_q3: "Berapakah biasanya kos kontrak pembersihan komersial?", faq_a3: "Harga kontrak bergantung kepada saiz hartanah dan jumlah pekerja yang diperlukan. Untuk pembersihan B2B yang disahkan ISO, sebut harga telus kami biasanya mencerminkan kos buruh langsung (anggaran RM 2,500 - RM 3,500 setiap pekerja sebulan, meliputi gaji minimum, KWSP, PERKESO, dan Levi), ditambah dengan pelunasan mesin berat. Kami tidak terlibat dalam perang harga; sebaliknya, kami menjamin standard sedia audit dan sifar caj tersembunyi.", faq_q4: "Berapakah masa tindak balas anda untuk kecemasan atau isu ad-hoc?", faq_a4: "HC Cleaning beroperasi dengan pasukan pengurusan yang sangat berpengalaman. Pengurus Operasi kami (pengalaman 38 tahun) dan Penyelia Kawasan (purata pengalaman 15-30 tahun) memantau zon khusus setiap hari. Kami menjamin tindak balas segera kepada sebarang aduan atau permintaan pembersihan ad-hoc kecemasan di sekitar Lembah Klang.", ins_label: "Pangkalan Pengetahuan", ins_title: "Wawasan Industri & Kajian Kes", ins_1_title: "Bagaimana Pencuci ISO 9001:2015 Menyelamatkan JMB Daripada Kos Tersembunyi", ins_1_desc: "Memilih kontraktor termurah sering kali menyebabkan kerosakan aset dan aduan penduduk. Temui bagaimana SOP ketat kami mengurangkan kos penyelenggaraan jangka panjang untuk kondominium mewah.", ins_2_title: "Pembersihan Permaidani Komersial: Syampu vs. Pengekstrakan Air Panas", ins_2_desc: "Tidak semua pembersihan permaidani adalah sama. Ketahui mengapa kami menggunakan pengekstrak wap Numatic gred industri untuk membuang alergen yang terperangkap dalam dan memanjangkan jangka hayat permaidani korporat anda.", ins_3_title: "Keselamatan Fasad Bangunan Tinggi: Di Sebalik Tabir The Avare", ins_3_desc: "Pembersihan kaca luaran pada ketinggian 40 tingkat memerlukan lebih daripada sekadar keberanian. Baca kajian kes kami mengenai bagaimana juruteknik capaian tali kami yang disahkan melaksanakan cucian fasad sifar kemalangan.", ins_readmore: "Baca Lanjut &rarr;", acc_title: "Pilihan Aksesibiliti", acc_text: "Teks Besar", acc_contrast: "Kontras Tinggi", acc_links: "Serlahkan Pautan"'

zh_str = 'faq_title: "常见问题解答", faq_q1: "贵公司的清洁员工是否合法受雇且享有全额保险？", faq_a1: "是的。我们拥有超过 300 名运营人员，严格遵守马来西亚劳工法。所有清洁工均持有合法准证，享有 SOCSO 和 CIDB 的全面保障，并在我们的 ISO 9001:2015 质量管理体系下接受持续培训。", faq_q2: "你们提供自己的清洁机械和化学品吗？", faq_a2: "绝对提供。我们供应商业级机械，包括英国进口的 Numatic 抽洗机和 Virco 高速抛光机。我们还提供所有必要的标准化化学品（例如，3M 抛光剂、起蜡水），并附带材料安全数据表（MSDS），以符合严格的 ESG 和安全标准。", faq_q3: "商业清洁合约通常需要多少费用？", faq_a3: "合约价格取决于物业面积和所需人数。对于通过 ISO 认证的 B2B 清洁服务，我们透明的报价通常反映直接劳动力成本（按每月每人约 RM 2,500 - RM 3,500 计算，涵盖最低工资、EPF、SOCSO 和外劳人头税），再加上重型机械的折旧。我们不参与价格战；相反，我们保证符合审计标准，绝无隐形收费。", faq_q4: "对于紧急或临时问题，你们的响应时间是多长？", faq_a4: "HC Cleaning 拥有一支经验丰富的管理团队。我们的运营经理（38年经验）和区域主管（平均15-30年经验）每天监控特定区域。我们保证对巴生谷范围内的任何投诉或紧急临时清洁请求做出迅速响应。", ins_label: "知识库", ins_title: "行业洞察与案例研究", ins_1_title: "ISO 9001:2015 清洁工如何为 JMB 节省隐形成本", ins_1_desc: "选择最便宜的承包商通常会导致资产损坏和居民投诉。了解我们严格的 SOP 如何降低豪华公寓的长期维护成本。", ins_2_title: "商业地毯清洗：洗发水洗与热水提取", ins_2_desc: "并非所有的地毯清洗都一样。了解为什么我们使用工业级 Numatic 蒸汽抽洗机来去除深层过敏原并延长您企业地毯的使用寿命。", ins_3_title: "高空外墙安全：The Avare 幕后花絮", ins_3_desc: "在 40 层高空进行外墙玻璃清洗需要的不仅仅是勇气。阅读我们的案例研究，了解我们经过认证的高空绳索技术人员如何执行零事故的高空清洗。", ins_readmore: "阅读更多 &rarr;", acc_title: "无障碍选项", acc_text: "放大字体", acc_contrast: "高对比度", acc_links: "高亮链接"'

replace_i18n('en', en_str)
replace_i18n('ms', ms_str)
replace_i18n('zh', zh_str)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Features and translations successfully added.")
