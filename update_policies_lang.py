import os

privacy_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy - HC Cleaning Services</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    body { padding: 80px 5%; max-width: 900px; margin: 0 auto; color: var(--white-dim); font-size: 15px; line-height: 1.8; }
    h1 { font-family: 'Playfair Display', serif; font-size: 40px; color: var(--gold); margin-bottom: 5px; }
    h2 { font-family: 'Playfair Display', serif; font-size: 22px; color: var(--white); margin-top: 40px; margin-bottom: 15px; }
    p { margin-bottom: 15px; }
    ul { margin-bottom: 20px; padding-left: 20px; }
    li { margin-bottom: 8px; }
    strong { color: var(--gold); }
    .effective-date { font-size: 13px; color: rgba(255,255,255,0.4); margin-bottom: 40px; }
    .back-btn { display: inline-block; margin-bottom: 30px; color: var(--gold); text-decoration: none; font-weight: bold; border: 1px solid var(--gold); padding: 8px 20px; border-radius: 4px; transition: 0.3s; }
    .back-btn:hover { background: var(--gold-dim); }
    .lang-content { display: none; }
  </style>
</head>
<body>
  <a href="index.html" class="back-btn" id="backBtn">&larr; Back to Home</a>
  
  <div class="lang-content en">
    <h1>Privacy Policy</h1>
    <div class="effective-date">Effective Date: June 18, 2026</div>

    <h2>1. Introduction</h2>
    <p>Welcome to the official website of HC Cleaning Services Sdn Bhd (399404-K) and its subsidiaries, HTC Ecoresources Sdn Bhd and Friendly Eco Services Sdn Bhd (collectively referred to as "HC Cleaning", "we", "us", or "our").</p>
    <p>We respect your privacy and are committed to protecting your personal data in compliance with the Personal Data Protection Act 2010 (PDPA) of Malaysia. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website (hc-cleaning-services.com) or interact with our web forms.</p>

    <h2>2. Information We Collect</h2>
    <p>We may collect personal identification information from you in various ways, primarily when you fill out our "Request Quotation" or "Download Company Profile" forms. The data we collect includes:</p>
    <ul>
      <li><strong>Contact Information:</strong> Name, Job Title / Designation.</li>
      <li><strong>Business Details:</strong> Company Name, Property Name, or Joint Management Body (JMB) / Management Corporation (MC) details.</li>
      <li><strong>Contact Data:</strong> Phone numbers and email addresses.</li>
      <li><strong>Service Requirements:</strong> Details regarding the specific facility management or cleaning services you require.</li>
    </ul>

    <h2>3. Purpose of Data Collection</h2>
    <p>The personal data we collect is solely used for legitimate business purposes, including:</p>
    <ul>
      <li>To process your request for a site inspection or corporate quotation.</li>
      <li>To provide access to our 60-page Company Profile PDF.</li>
      <li>To communicate with you regarding our cleaning, landscaping, and maintenance services.</li>
      <li>To improve our customer service and tailor our facility management solutions to your specific needs.</li>
      <li>To send official correspondence via email or WhatsApp as requested by you.</li>
    </ul>

    <h2>4. Data Sharing and Disclosure</h2>
    <p>We do not sell, trade, or rent your personal data to any third parties. Your information may only be shared within our corporate group (including our subsidiaries) to fulfill your service requests.</p>
    <p>We may also disclose your data if required by law, court order, or governmental regulations.</p>

    <h2>5. Data Security</h2>
    <p>As an ISO 9001:2015 certified corporation, we implement strict operational guidelines and security measures to protect your personal data against unauthorized access, alteration, disclosure, or destruction. However, please note that no method of transmission over the internet or electronic storage is 100% secure.</p>

    <h2>6. Your Rights</h2>
    <p>Under the PDPA, you have the right to:</p>
    <ul>
      <li>Request access to the personal data we hold about you.</li>
      <li>Request corrections to any inaccurate or outdated information.</li>
      <li>Withdraw your consent for us to use your data for communication purposes.</li>
    </ul>

    <h2>7. Contact Us</h2>
    <p>If you have any questions about this Privacy Policy or wish to exercise your data protection rights, please contact our administrative office:</p>
    <p>
      <strong>Address:</strong> Suite 18.01, 18th Floor, Plaza Pengkalan, Jalan Tiong, Off BT 3, Jalan Sultan Azlan Shah, 51100 Kuala Lumpur.<br>
      <strong>Phone:</strong> 03-4043 8599<br>
      <strong>Email:</strong> hc.cleaning@hotmail.com
    </p>
  </div>

  <div class="lang-content ms">
    <h1>Dasar Privasi</h1>
    <div class="effective-date">Tarikh Kuat Kuasa: 18 Jun 2026</div>

    <h2>1. Pengenalan</h2>
    <p>Selamat datang ke laman web rasmi HC Cleaning Services Sdn Bhd (399404-K) dan anak syarikatnya, HTC Ecoresources Sdn Bhd dan Friendly Eco Services Sdn Bhd (secara kolektif dirujuk sebagai "HC Cleaning", "kami", atau "kita").</p>
    <p>Kami menghormati privasi anda dan komited untuk melindungi data peribadi anda selaras dengan Akta Perlindungan Data Peribadi 2010 (PDPA) Malaysia. Dasar Privasi ini menerangkan cara kami mengumpul, menggunakan, mendedahkan dan melindungi maklumat anda apabila anda melayari laman web kami (hc-cleaning-services.com) atau berinteraksi dengan borang web kami.</p>

    <h2>2. Maklumat Yang Kami Kumpul</h2>
    <p>Kami mungkin mengumpul maklumat pengenalan peribadi daripada anda melalui pelbagai cara, terutamanya apabila anda mengisi borang "Minta Sebut Harga" atau "Muat Turun Profil Syarikat" kami. Data yang kami kumpul termasuk:</p>
    <ul>
      <li><strong>Maklumat Hubungan:</strong> Nama, Jawatan.</li>
      <li><strong>Butiran Perniagaan:</strong> Nama Syarikat, Nama Hartanah, atau butiran Badan Pengurusan Bersama (JMB) / Perbadanan Pengurusan (MC).</li>
      <li><strong>Data Hubungan:</strong> Nombor telefon dan alamat e-mel.</li>
      <li><strong>Keperluan Perkhidmatan:</strong> Butiran mengenai perkhidmatan pengurusan fasiliti atau pembersihan khusus yang anda perlukan.</li>
    </ul>

    <h2>3. Tujuan Pengumpulan Data</h2>
    <p>Data peribadi yang kami kumpul hanya digunakan untuk tujuan perniagaan yang sah, termasuk:</p>
    <ul>
      <li>Untuk memproses permohonan anda bagi pemeriksaan tapak atau sebut harga korporat.</li>
      <li>Untuk memberi akses kepada PDF Profil Syarikat 60 halaman kami.</li>
      <li>Untuk berkomunikasi dengan anda mengenai perkhidmatan pembersihan, landskap dan penyelenggaraan kami.</li>
      <li>Untuk meningkatkan perkhidmatan pelanggan kami dan menyesuaikan penyelesaian pengurusan fasiliti mengikut keperluan khusus anda.</li>
      <li>Untuk menghantar surat-menyurat rasmi melalui e-mel atau WhatsApp seperti yang diminta oleh anda.</li>
    </ul>

    <h2>4. Perkongsian dan Pendedahan Data</h2>
    <p>Kami tidak menjual, berdagang atau menyewa data peribadi anda kepada mana-mana pihak ketiga. Maklumat anda hanya boleh dikongsi dalam kumpulan korporat kami (termasuk anak syarikat kami) untuk memenuhi permintaan perkhidmatan anda.</p>
    <p>Kami juga mungkin mendedahkan data anda jika dikehendaki oleh undang-undang, perintah mahkamah atau peraturan kerajaan.</p>

    <h2>5. Keselamatan Data</h2>
    <p>Sebagai syarikat yang disahkan ISO 9001:2015, kami melaksanakan garis panduan operasi dan langkah keselamatan yang ketat untuk melindungi data peribadi anda daripada akses yang tidak dibenarkan, pengubahan, pendedahan atau kemusnahan. Walau bagaimanapun, sila ambil perhatian bahawa tiada kaedah penghantaran melalui internet atau storan elektronik yang 100% selamat.</p>

    <h2>6. Hak Anda</h2>
    <p>Di bawah PDPA, anda berhak untuk:</p>
    <ul>
      <li>Meminta akses kepada data peribadi yang kami simpan mengenai anda.</li>
      <li>Meminta pembetulan bagi sebarang maklumat yang tidak tepat atau lapuk.</li>
      <li>Menarik balik persetujuan anda untuk kami menggunakan data anda bagi tujuan komunikasi.</li>
    </ul>

    <h2>7. Hubungi Kami</h2>
    <p>Jika anda mempunyai sebarang soalan tentang Dasar Privasi ini atau ingin menggunakan hak perlindungan data anda, sila hubungi pejabat pentadbiran kami:</p>
    <p>
      <strong>Alamat:</strong> Suite 18.01, Tingkat 18, Plaza Pengkalan, Jalan Tiong, Off BT 3, Jalan Sultan Azlan Shah, 51100 Kuala Lumpur.<br>
      <strong>Telefon:</strong> 03-4043 8599<br>
      <strong>E-mel:</strong> hc.cleaning@hotmail.com
    </p>
  </div>

  <div class="lang-content zh">
    <h1>隐私政策</h1>
    <div class="effective-date">生效日期：2026年6月18日</div>

    <h2>1. 简介</h2>
    <p>欢迎访问 HC Cleaning Services Sdn Bhd (399404-K) 及其子公司 HTC Ecoresources Sdn Bhd 和 Friendly Eco Services Sdn Bhd（统称为“HC Cleaning”、“我们”或“我们的”）的官方网站。</p>
    <p>我们尊重您的隐私，并承诺依据马来西亚《2010年个人数据保护法》(PDPA) 保护您的个人数据。本隐私政策解释了当您访问我们的网站 (hc-cleaning-services.com) 或使用我们的网页表单时，我们如何收集、使用、披露和保护您的信息。</p>

    <h2>2. 我们收集的信息</h2>
    <p>我们可能会通过多种方式收集您的个人身份信息，主要是在您填写“获取报价”或“下载公司简介”表单时。我们收集的数据包括：</p>
    <ul>
      <li><strong>联系信息：</strong> 姓名、职位/头衔。</li>
      <li><strong>业务详情：</strong> 公司名称、物业名称，或联合管理机构 (JMB) / 管理机构 (MC) 详情。</li>
      <li><strong>联系数据：</strong> 电话号码和电子邮件地址。</li>
      <li><strong>服务需求：</strong> 有关您所需的特定设施管理或清洁服务的详细信息。</li>
    </ul>

    <h2>3. 数据收集目的</h2>
    <p>我们收集的个人数据仅用于合法的业务目的，包括：</p>
    <ul>
      <li>处理您的现场检查或企业报价请求。</li>
      <li>提供我们长达 60 页的公司简介 PDF 文件的访问权限。</li>
      <li>就我们的清洁、景观美化和维护服务与您进行沟通。</li>
      <li>改善我们的客户服务，并根据您的具体需求量身定制设施管理解决方案。</li>
      <li>根据您的要求通过电子邮件或 WhatsApp 发送官方信函。</li>
    </ul>

    <h2>4. 数据共享与披露</h2>
    <p>我们不会向任何第三方出售、交易或出租您的个人数据。您的信息仅在我们的企业集团（包括我们的子公司）内部共享，以满足您的服务请求。</p>
    <p>如果法律、法院命令或政府法规要求，我们也可能会披露您的数据。</p>

    <h2>5. 数据安全</h2>
    <p>作为一家通过 ISO 9001:2015 认证的企业，我们实施严格的运营准则和安全措施，以保护您的个人数据免遭未经授权的访问、篡改、披露或销毁。但是请注意，任何通过互联网传输或电子存储的方法都无法做到 100% 绝对安全。</p>

    <h2>6. 您的权利</h2>
    <p>根据 PDPA，您有权：</p>
    <ul>
      <li>要求访问我们持有的关于您的个人数据。</li>
      <li>要求更正任何不准确或过时的信息。</li>
      <li>撤回您对我们出于通信目的使用您数据的同意。</li>
    </ul>

    <h2>7. 联系我们</h2>
    <p>如果您对本隐私政策有任何疑问，或希望行使您的数据保护权利，请联系我们的行政办公室：</p>
    <p>
      <strong>地址：</strong> Suite 18.01, 18th Floor, Plaza Pengkalan, Jalan Tiong, Off BT 3, Jalan Sultan Azlan Shah, 51100 Kuala Lumpur.<br>
      <strong>电话：</strong> 03-4043 8599<br>
      <strong>电子邮箱：</strong> hc.cleaning@hotmail.com
    </p>
  </div>

  <br><br><br>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('hc_lang') || 'en';
      document.querySelectorAll('.lang-content').forEach(el => el.style.display = 'none');
      
      const targetDivs = document.querySelectorAll('.lang-content.' + savedLang);
      if(targetDivs.length > 0) {
        targetDivs.forEach(el => el.style.display = 'block');
      } else {
        document.querySelectorAll('.lang-content.en').forEach(el => el.style.display = 'block');
      }

      const btn = document.getElementById('backBtn');
      if(savedLang === 'ms') btn.innerHTML = '&larr; Kembali ke Laman Utama';
      else if(savedLang === 'zh') btn.innerHTML = '&larr; 返回首页';
    });
  </script>
</body>
</html>"""

terms_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms of Service - HC Cleaning Services</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    body { padding: 80px 5%; max-width: 900px; margin: 0 auto; color: var(--white-dim); font-size: 15px; line-height: 1.8; }
    h1 { font-family: 'Playfair Display', serif; font-size: 40px; color: var(--gold); margin-bottom: 5px; }
    h2 { font-family: 'Playfair Display', serif; font-size: 22px; color: var(--white); margin-top: 40px; margin-bottom: 15px; }
    p { margin-bottom: 15px; }
    strong { color: var(--gold); }
    .effective-date { font-size: 13px; color: rgba(255,255,255,0.4); margin-bottom: 40px; }
    .back-btn { display: inline-block; margin-bottom: 30px; color: var(--gold); text-decoration: none; font-weight: bold; border: 1px solid var(--gold); padding: 8px 20px; border-radius: 4px; transition: 0.3s; }
    .back-btn:hover { background: var(--gold-dim); }
    .lang-content { display: none; }
  </style>
</head>
<body>
  <a href="index.html" class="back-btn" id="backBtn">&larr; Back to Home</a>
  
  <div class="lang-content en">
    <h1>Terms of Service</h1>
    <div class="effective-date">Effective Date: June 18, 2026</div>

    <h2>1. Acceptance of Terms</h2>
    <p>By accessing and using the website of HC Cleaning Services Sdn Bhd (hc-cleaning-services.com), you accept and agree to be bound by these Terms of Service. If you do not agree with any part of these terms, please do not use our website or download our corporate materials.</p>

    <h2>2. Scope of Web Services</h2>
    <p>Our website provides general information about our commercial cleaning, high-rise facade cleaning, and condominium maintenance services.</p>
    <p>Please note that utilizing our "Request Quotation" form does not constitute a legally binding service contract. All final pricing, service scope, and legal agreements are subject to a formal site inspection by our Operation Executives and the subsequent signing of an official Contract Agreement.</p>

    <h2>3. Intellectual Property Rights</h2>
    <p>All content on this website—including but not limited to text, graphics, logos, images, before/after photographs, ISO 9001 certificates, and the downloadable Company Profile PDF—is the exclusive property of HC Cleaning Services Sdn Bhd and is protected by Malaysian and international copyright laws.</p>
    <p>You may download our Company Profile for personal or B2B evaluation purposes only. You may not reproduce, distribute, modify, or commercially exploit our proprietary content without explicit written permission from our management.</p>

    <h2>4. User Conduct</h2>
    <p>When interacting with our website, particularly when filling out forms or using our AI Chatbot, you agree to provide accurate and truthful information (e.g., authentic company names and contact details). You must not use our website to transmit any malicious software, spam, or unlawful materials.</p>

    <h2>5. Disclaimer of Warranties and Limitation of Liability</h2>
    <p>While we strive to keep the information on our website accurate and up-to-date, HC Cleaning makes no representations or warranties of any kind, express or implied, regarding the completeness or accuracy of the website content.</p>
    <p>In no event shall HC Cleaning Services Sdn Bhd, its directors, employees, or subsidiaries be liable for any direct, indirect, incidental, or consequential damages arising out of your use of, or inability to use, this website.</p>

    <h2>6. External Links</h2>
    <p>Our website may contain links to third-party platforms (e.g., Google Maps, WhatsApp API, Google Drive for PDF downloads). We do not control these third-party platforms and are not responsible for their content or privacy practices.</p>

    <h2>7. Governing Law</h2>
    <p>These Terms of Service shall be governed by and construed in accordance with the laws of Malaysia. Any disputes arising in connection with these terms shall be subject to the exclusive jurisdiction of the courts of Malaysia.</p>

    <h2>8. Contact Information</h2>
    <p>For any legal inquiries or issues regarding these terms, please contact our headquarters:</p>
    <p>
      <strong>HC Cleaning Services Sdn Bhd (399404-K)</strong><br>
      <strong>Address:</strong> Suite 18.01, 18th Floor, Plaza Pengkalan, Jalan Tiong, Off BT 3, Jalan Sultan Azlan Shah, 51100 Kuala Lumpur.<br>
      <strong>Phone:</strong> 03-4043 8599
    </p>
  </div>

  <div class="lang-content ms">
    <h1>Terma Perkhidmatan</h1>
    <div class="effective-date">Tarikh Kuat Kuasa: 18 Jun 2026</div>

    <h2>1. Penerimaan Terma</h2>
    <p>Dengan mengakses dan menggunakan laman web HC Cleaning Services Sdn Bhd (hc-cleaning-services.com), anda menerima dan bersetuju untuk terikat dengan Terma Perkhidmatan ini. Jika anda tidak bersetuju dengan mana-mana bahagian terma ini, sila jangan gunakan laman web kami atau memuat turun bahan korporat kami.</p>

    <h2>2. Skop Perkhidmatan Web</h2>
    <p>Laman web kami menyediakan maklumat umum tentang perkhidmatan pembersihan komersial, pembersihan fasad bangunan tinggi dan penyelenggaraan kondominium kami.</p>
    <p>Sila ambil perhatian bahawa penggunaan borang "Minta Sebut Harga" kami tidak membentuk kontrak perkhidmatan yang mengikat di sisi undang-undang. Semua harga akhir, skop perkhidmatan dan perjanjian undang-undang tertakluk pada pemeriksaan tapak rasmi oleh Eksekutif Operasi kami dan pemeteraian Perjanjian Kontrak rasmi yang berikutnya.</p>

    <h2>3. Hak Harta Intelek</h2>
    <p>Semua kandungan di laman web ini—termasuk tetapi tidak terhad kepada teks, grafik, logo, imej, gambar sebelum/selepas, sijil ISO 9001, dan PDF Profil Syarikat yang boleh dimuat turun—adalah hak milik eksklusif HC Cleaning Services Sdn Bhd dan dilindungi oleh undang-undang hak cipta Malaysia dan antarabangsa.</p>
    <p>Anda boleh memuat turun Profil Syarikat kami untuk tujuan peribadi atau penilaian B2B sahaja. Anda tidak boleh mengeluarkan semula, mengedar, mengubah suai atau mengeksploitasi kandungan proprietari kami secara komersial tanpa kebenaran bertulis yang jelas daripada pengurusan kami.</p>

    <h2>4. Tingkah Laku Pengguna</h2>
    <p>Apabila berinteraksi dengan laman web kami, terutamanya semasa mengisi borang atau menggunakan Chatbot AI kami, anda bersetuju untuk memberikan maklumat yang tepat dan benar (cth., nama syarikat dan butiran hubungan yang tulen). Anda tidak dibenarkan menggunakan laman web kami untuk menghantar sebarang perisian berniat jahat, spam atau bahan yang menyalahi undang-undang.</p>

    <h2>5. Penafian Waranti dan Had Liabiliti</h2>
    <p>Walaupun kami berusaha untuk memastikan maklumat di laman web kami tepat dan terkini, HC Cleaning tidak membuat sebarang representasi atau waranti dalam apa jua bentuk, tersurat atau tersirat, berkenaan dengan kesempurnaan atau ketepatan kandungan laman web.</p>
    <p>Dalam apa jua keadaan sekalipun, HC Cleaning Services Sdn Bhd, pengarah, pekerja atau anak syarikatnya tidak akan bertanggungjawab ke atas sebarang kerosakan langsung, tidak langsung, kebetulan atau berbangkit yang timbul daripada penggunaan anda, atau ketidakupayaan untuk menggunakan, laman web ini.</p>

    <h2>6. Pautan Luar</h2>
    <p>Laman web kami mungkin mengandungi pautan ke platform pihak ketiga (cth., Peta Google, API WhatsApp, Google Drive untuk muat turun PDF). Kami tidak mengawal platform pihak ketiga ini dan tidak bertanggungjawab ke atas kandungan atau amalan privasi mereka.</p>

    <h2>7. Undang-undang yang Mengawal Selia</h2>
    <p>Terma Perkhidmatan ini hendaklah dikawal oleh dan ditafsirkan selaras dengan undang-undang Malaysia. Sebarang pertikaian yang timbul berkaitan dengan terma ini hendaklah tertakluk kepada bidang kuasa eksklusif mahkamah Malaysia.</p>

    <h2>8. Maklumat Hubungan</h2>
    <p>Untuk sebarang pertanyaan undang-undang atau isu mengenai terma ini, sila hubungi ibu pejabat kami:</p>
    <p>
      <strong>HC Cleaning Services Sdn Bhd (399404-K)</strong><br>
      <strong>Alamat:</strong> Suite 18.01, Tingkat 18, Plaza Pengkalan, Jalan Tiong, Off BT 3, Jalan Sultan Azlan Shah, 51100 Kuala Lumpur.<br>
      <strong>Telefon:</strong> 03-4043 8599
    </p>
  </div>

  <div class="lang-content zh">
    <h1>服务条款</h1>
    <div class="effective-date">生效日期：2026年6月18日</div>

    <h2>1. 接受条款</h2>
    <p>访问和使用 HC Cleaning Services Sdn Bhd 网站 (hc-cleaning-services.com)，即表示您接受并同意受这些服务条款的约束。如果您不同意本条款的任何部分，请不要使用我们的网站或下载我们的企业资料。</p>

    <h2>2. 网络服务范围</h2>
    <p>我们的网站提供有关我们的商业清洁、高层建筑外墙清洁和公寓维护服务的一般信息。</p>
    <p>请注意，使用我们的“获取报价”表单并不构成具有法律约束力的服务合同。所有最终定价、服务范围和法律协议均需由我们的运营主管进行正式的现场检查，并随后签署正式的合同协议。</p>

    <h2>3. 知识产权</h2>
    <p>本网站上的所有内容（包括但不限于文本、图形、徽标、图像、清洁前后对比照片、ISO 9001 证书以及可下载的公司简介 PDF）均是 HC Cleaning Services Sdn Bhd 的专有财产，受马来西亚及国际版权法的保护。</p>
    <p>您只能出于个人或 B2B 评估目的下载我们的公司简介。未经我们管理层的明确书面许可，您不得复制、分发、修改或商业性地利用我们的专有内容。</p>

    <h2>4. 用户行为</h2>
    <p>当您与我们的网站互动时，特别是在填写表单或使用我们的 AI 聊天机器人时，您同意提供准确真实的信息（例如，真实的公司名称和联系方式）。您不得使用我们的网站传输任何恶意软件、垃圾邮件或非法材料。</p>

    <h2>5. 免责声明和责任限制</h2>
    <p>虽然我们尽力保持网站上信息的准确性和最新性，但 HC Cleaning 对网站内容的完整性或准确性不作任何形式的明示或暗示的陈述或保证。</p>
    <p>在任何情况下，HC Cleaning Services Sdn Bhd 及其董事、员工或子公司均不对因您使用或无法使用本网站而引起的任何直接、间接、附带或后果性损害负责。</p>

    <h2>6. 外部链接</h2>
    <p>我们的网站可能包含指向第三方平台的链接（例如 Google 地图、WhatsApp API、用于下载 PDF 的 Google 云端硬盘）。我们无法控制这些第三方平台，也不对其内容或隐私做法负责。</p>

    <h2>7. 适用法律</h2>
    <p>这些服务条款受马来西亚法律的管辖，并依其解释。任何与这些条款相关的争议均应提交马来西亚法院专属管辖。</p>

    <h2>8. 联系方式</h2>
    <p>有关这些条款的任何法律咨询或问题，请联系我们的总部：</p>
    <p>
      <strong>HC Cleaning Services Sdn Bhd (399404-K)</strong><br>
      <strong>地址：</strong> Suite 18.01, 18th Floor, Plaza Pengkalan, Jalan Tiong, Off BT 3, Jalan Sultan Azlan Shah, 51100 Kuala Lumpur.<br>
      <strong>电话：</strong> 03-4043 8599
    </p>
  </div>

  <br><br><br>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('hc_lang') || 'en';
      document.querySelectorAll('.lang-content').forEach(el => el.style.display = 'none');
      
      const targetDivs = document.querySelectorAll('.lang-content.' + savedLang);
      if(targetDivs.length > 0) {
        targetDivs.forEach(el => el.style.display = 'block');
      } else {
        document.querySelectorAll('.lang-content.en').forEach(el => el.style.display = 'block');
      }

      const btn = document.getElementById('backBtn');
      if(savedLang === 'ms') btn.innerHTML = '&larr; Kembali ke Laman Utama';
      else if(savedLang === 'zh') btn.innerHTML = '&larr; 返回首页';
    });
  </script>
</body>
</html>"""

with open(r'c:\Users\taiwe\Desktop\cleaning\privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_html)
    
with open(r'c:\Users\taiwe\Desktop\cleaning\terms-of-service.html', 'w', encoding='utf-8') as f:
    f.write(terms_html)

print("Policy pages successfully updated with multi-language capability.")
