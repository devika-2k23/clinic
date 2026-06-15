import re

html_path = 'c:\\madhavika\\joy\\joyy\\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

icons_map = {
    'lucide:wind': ('healthicons:nose-outline', 'Allergic Rhinitis and Sinusitis icon'),
    'lucide:stethoscope': ('healthicons:lungs-outline', 'Asthma and Bronchitis icon'),
    'lucide:sparkles': ('lucide:scan-face', 'Skin Diseases and Analysis icon'),
    'lucide:utensils': ('healthicons:stomach-outline', 'Gastric and Liver Issues icon'),
    'lucide:droplet': ('healthicons:kidneys-outline', 'Kidney Stones and UTI icon'),
    'lucide:brain': ('healthicons:headache-outline', 'Migraine and Headaches icon'),
    'lucide:bone': ('healthicons:joints-outline', 'Arthritis and Joint Pain icon'),
    'lucide:heart-pulse': ('healthicons:diabetes-outline', 'Diabetes Management icon'),
    'lucide:user': ('mdi:face-woman-profile', 'Hair and Scalp Issues icon'),
    'lucide:flower-2': ('icon-park-outline:uterus', 'PCOD and Hormonal Imbalance icon'),
    'lucide:moon': ('healthicons:mental-health-outline', 'Stress, Anxiety and Insomnia icon'),
    'lucide:shield-plus': ('healthicons:thyroid-outline', 'Thyroid Disorders icon'),
}

for old_icon, (new_icon, alt_text) in icons_map.items():
    pattern = r'<img src="https://api\.iconify\.design/' + old_icon + r'\.svg[^>]*>'
    replacement = f'<img src="https://api.iconify.design/{new_icon}.svg?color=%233D7A4A" alt="{alt_text}" style="width: 55%; height: 55%; object-fit: contain;" />'
    content = re.sub(pattern, replacement, content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Icons successfully replaced.')
