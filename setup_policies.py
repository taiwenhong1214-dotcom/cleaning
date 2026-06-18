import os
import re

privacy_content = """<!DOCTYPE html>
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
  </style>
</head>
<body>
  <a href="index.html" class="back-btn">&larr; Back to Home</a>
  
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
  
  <br><br><br>
</body>
</html>"""

terms_content = """<!DOCTYPE html>
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
  </style>
</head>
<body>
  <a href="index.html" class="back-btn">&larr; Back to Home</a>
  
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

  <br><br><br>
</body>
</html>"""

with open(r'c:\Users\taiwe\Desktop\cleaning\privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_content)
    
with open(r'c:\Users\taiwe\Desktop\cleaning\terms-of-service.html', 'w', encoding='utf-8') as f:
    f.write(terms_content)

# Update index.html links
index_path = r'c:\Users\taiwe\Desktop\cleaning\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('href="privacy.html"', 'href="privacy-policy.html"')
html = html.replace('href="terms.html"', 'href="terms-of-service.html"')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Delete old placeholder files if they exist
try:
    os.remove(r'c:\Users\taiwe\Desktop\cleaning\privacy.html')
except OSError:
    pass

try:
    os.remove(r'c:\Users\taiwe\Desktop\cleaning\terms.html')
except OSError:
    pass

print("New policy pages created, links updated, and old placeholders removed.")
