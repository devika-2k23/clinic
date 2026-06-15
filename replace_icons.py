import re

html_path = 'c:\\madhavika\\joy\\joyy\\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

icons_map = {
    'icon_1.png': ('lucide:wind', 'Allergic Rhinitis and Sinusitis icon'),
    'icon_2.png': ('lucide:stethoscope', 'Asthma and Bronchitis icon'),
    'icon_3.png': ('lucide:sparkles', 'Skin Diseases icon'),
    'icon_4.png': ('lucide:utensils', 'Gastric and Liver Issues icon'),
    'icon_5.png': ('lucide:droplet', 'Kidney Stones and UTI icon'),
    'icon_6.png': ('lucide:brain', 'Migraine and Headaches icon'),
    'icon_7.png': ('lucide:bone', 'Arthritis and Joint Pain icon'),
    'icon_8.png': ('lucide:heart-pulse', 'Diabetes Management icon'),
    'icon_9.png': ('lucide:user', 'Hair and Scalp Issues icon'),
    'icon_10.png': ('lucide:flower-2', 'PCOD and Hormonal Imbalance icon'),
    'icon_11.png': ('lucide:moon', 'Stress, Anxiety and Insomnia icon'),
    'icon_12.png': ('lucide:shield-plus', 'Thyroid Disorders icon'),
}

for icon_file, (lucide_name, alt_text) in icons_map.items():
    pattern = r'<img src="assets/images/icons/' + icon_file + r'"[^>]*>'
    replacement = f'<img src="https://api.iconify.design/{lucide_name}.svg?color=%233D7A4A" alt="{alt_text}" style="width: 45%; height: 45%; object-fit: contain;" />'
    content = re.sub(pattern, replacement, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Icons successfully replaced.')
