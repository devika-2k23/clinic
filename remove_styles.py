import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove specific inline styles and add classes where necessary
replacements = [
    (r'class="hero-title" style="color: #3D7A4A; text-wrap: balance;"', r'class="hero-title"'),
    (r'<span style="color: #3D7A4A;">', r'<span>'),
    (r'class="hero-subtitle" style="font-size: 0.95rem; font-weight: 600; color: #8B6F47;"', r'class="hero-subtitle"'),
    (r'class="about-heading" id="about-title" style="text-wrap: balance;"', r'class="about-heading" id="about-title"'),
    (r'class="section-label" style="margin-bottom: 8px;"', r'class="section-label"'),
    (r'class="about-heading" id="doctor-title" style="margin-bottom: 0;"', r'class="about-heading" id="doctor-title"'),
    (r'class="doctor-degree-badge" style="margin-bottom: 0;"', r'class="doctor-degree-badge"'),
    (r'class="expertise-accordion-section" style="margin-top: 0;"', r'class="expertise-accordion-section"'),
    (r'class="why-subtitle" style="text-align: justify;"', r'class="why-subtitle"'),
    (r'<div style="font-size:0.78rem;color:#8B6F47;text-transform:uppercase;letter-spacing:0.08em;">', r'<div class="contact-item-label">'),
    (r'<a href="tel:\+917395960233" style="color:#3D7A4A;font-weight:700;font-size:1.1rem;text-decoration:none;background:rgba\(61, 122, 74, 0.08\);padding:6px 14px;border-radius:8px;display:inline-block;margin-top:4px;">', r'<a href="tel:+917395960233" class="contact-item-link">'),
    (r'<a href="https://maps.google.com/\?q=Joy\+Homoeo\+Care\+Mandavelipakkam\+Chennai" target="_blank" rel="noopener noreferrer" style="color:#3D7A4A;font-size:0.82rem;display:inline-block;margin-top:4px;text-decoration:underline;">', r'<a href="https://maps.google.com/?q=Joy+Homoeo+Care+Mandavelipakkam+Chennai" target="_blank" rel="noopener noreferrer" class="contact-item-link-maps">')
]

for old, new in replacements:
    content = re.sub(old, new, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Inline styles removed.")
