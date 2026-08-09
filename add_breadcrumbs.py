from pathlib import Path
import re

root = Path('.')
updated = []
for f in sorted(root.rglob('*.html')):
    text = f.read_text(encoding='utf-8')
    if '<p class="breadcrumbs">' in text:
        continue
    if '<header>' not in text:
        continue
    title_match = re.search(r'<title>(.*?)</title>', text, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else f.stem
    title = re.sub(r'^(KSC|KCN)\s*\|\s*', '', title, flags=re.IGNORECASE).strip()
    if title.lower() in ['home', 'index', 'page']:
        crumb = '<p class="breadcrumbs"><a href="/">Home</a></p>'
    else:
        crumb = f'<p class="breadcrumbs"><a href="/">Home</a> / <span>{title}</span></p>'
    if '</header>' in text:
        new_text = text.replace('</header>', '</header>\n\n' + crumb, 1)
        f.write_text(new_text, encoding='utf-8')
        updated.append(str(f))

print('UPDATED', len(updated))
for path in updated:
    print(path)
