import re

with open(r'c:\Users\taiwe\Desktop\cleaning\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract <style>
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    style_content = style_match.group(1).strip()
    with open(r'c:\Users\taiwe\Desktop\cleaning\style.css', 'w', encoding='utf-8') as f:
        f.write(style_content)
    
    # Replace style with link and add AOS CSS
    aos_css = '<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n<link rel="stylesheet" href="style.css">'
    content = content[:style_match.start()] + aos_css + content[style_match.end():]

# 2. Extract <script> (the main one at the bottom, careful there might be multiple, but we saw it starting at 573)
script_match = re.search(r'<script>\s*/\* =======================================\s*🌐 多语言字典 & 逻辑(.*?)</body>', content, re.DOTALL)
if script_match:
    # Actually, we can just find the last <script> block, but let's be more robust
    scripts = list(re.finditer(r'<script>(.*?)</script>', content, re.DOTALL))
    main_script_match = scripts[-1]
    
    script_content = main_script_match.group(1).strip()
    with open(r'c:\Users\taiwe\Desktop\cleaning\script.js', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    aos_js = '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n<script>\n  AOS.init({ once: true });\n</script>\n<script src="script.js"></script>'
    content = content[:main_script_match.start()] + aos_js + content[main_script_match.end():]

# 3. Add AOS attributes
content = content.replace('class="hero-content"', 'class="hero-content" data-aos="fade-up"')
content = content.replace('class="hero-stats"', 'class="hero-stats" data-aos="fade-up"')
content = content.replace('class="about-grid"', 'class="about-grid" data-aos="fade-up"')

# Staggered for service-card
service_cards = list(re.finditer(r'class="service-card"', content))
offset = 0
for i, match in enumerate(service_cards):
    delay = (i % 3) * 100
    replacement = f'class="service-card" data-aos="fade-up" data-aos-delay="{delay}"'
    content = content[:match.start() + offset] + replacement + content[match.end() + offset:]
    offset += len(replacement) - (match.end() - match.start())

content = content.replace('class="awards-grid"', 'class="awards-grid" data-aos="fade-up"')

# 4. Add name attributes to profileModal inputs
content = content.replace('id="dlName"', 'id="dlName" name="dlName"')
content = content.replace('id="dlCompany"', 'id="dlCompany" name="dlCompany"')
content = content.replace('id="dlEmail"', 'id="dlEmail" name="dlEmail"')

with open(r'c:\Users\taiwe\Desktop\cleaning\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 5. Fix submitProfileForm in script.js
with open(r'c:\Users\taiwe\Desktop\cleaning\script.js', 'r', encoding='utf-8') as f:
    script_content = f.read()

old_func = """function submitProfileForm(e) {
    e.preventDefault(); 
    document.getElementById('dlSuccess').style.display = 'block';
    setTimeout(() => {
      const fileID = '1_X34pLPo7ygidZ4nH71aRKlt9bIIitUC'; 
      window.location.href = 'https://drive.google.com/uc?export=download&id=' + fileID; 
      closeProfileModal();
    }, 2000);
  }"""

new_func = """function submitProfileForm(e) {
    e.preventDefault(); 
    
    const form = e.target;
    const formData = new FormData(form);
    
    fetch('https://formspree.io/f/YOUR_FORM_ID', {
      method: 'POST',
      body: formData,
      headers: {
        'Accept': 'application/json'
      }
    }).then(response => {
      if (response.ok) {
        document.getElementById('dlSuccess').style.display = 'block';
        setTimeout(() => {
          const fileID = '1_X34pLPo7ygidZ4nH71aRKlt9bIIitUC'; 
          window.location.href = 'https://drive.google.com/uc?export=download&id=' + fileID; 
          closeProfileModal();
        }, 2000);
      } else {
        alert("Oops! There was a problem submitting your form");
      }
    }).catch(error => {
      alert("Oops! There was a problem submitting your form");
    });
  }"""

script_content = script_content.replace(old_func, new_func)

with open(r'c:\Users\taiwe\Desktop\cleaning\script.js', 'w', encoding='utf-8') as f:
    f.write(script_content)

print("Done")
