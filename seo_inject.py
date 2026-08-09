import glob
import os
import re

root = os.path.abspath(os.path.dirname(__file__))
html_files = sorted(glob.glob(os.path.join(root, '**', '*.html'), recursive=True))

META_TEMPLATE = '''    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{og_description}">
    <meta property="og:url" content="{og_url}">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "{site_name}",
      "url": "{og_url}",
      "description": "{og_description}"
    }}
    </script>
'''

for path in html_files:
    rel = os.path.relpath(path, root).replace('\\', '/')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    head_match = re.search(r'<head>(.*?)</head>', text, re.I | re.S)
    if not head_match:
        continue
    head_content = head_match.group(1)
    lower = head_content.lower()
    if '<meta name="viewport"' not in lower and "<meta name='viewport'" not in lower:
        head_content = '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + head_content
    if '<meta name="description"' in lower or "<meta name='description'" in lower:
        has_desc = True
    else:
        has_desc = False
    if '<meta name="keywords"' in lower or "<meta name='keywords'" in lower:
        has_keywords = True
    else:
        has_keywords = False
    if '<meta property="og:' in lower or "<meta property='og:" in lower:
        has_og = True
    else:
        has_og = False
    if '<script type="application/ld+json"' in lower or "<script type='application/ld+json'" in lower:
        has_jsonld = True
    else:
        has_jsonld = False

    if has_desc and has_keywords and has_og and has_jsonld:
        continue

    title_match = re.search(r'<title>(.*?)</title>', head_content, re.I | re.S)
    title = title_match.group(1).strip() if title_match else os.path.splitext(os.path.basename(path))[0].title()
    if title.lower() == 'page':
        title = 'Kato Sports Cards'
    site_name = title if title != 'Index' else 'Kato Sports Cards'
    page_url = 'https://kscmn.com/' + rel.replace('index.html', '').lstrip('/')
    if page_url.endswith('/'):
        page_url = page_url[:-1] if page_url != 'https://kscmn.com/' else page_url
    description = f"{title} from Kato Sports Cards. Explore sports card news, rookie cards, release dates, comps, and shop listings from Mankato, Minnesota."
    keywords = 'Kato Sports Cards, sports cards, rookie cards, card release dates, card comps, trading cards, hobby boxes, sports card news'
    og_title = title
    og_description = description
    insert_block = META_TEMPLATE.format(
        description=description.replace('"', '&quot;'),
        keywords=keywords,
        og_title=og_title.replace('"', '&quot;'),
        og_description=og_description.replace('"', '&quot;'),
        og_url=page_url,
        site_name=site_name.replace('"', '&quot;')
    )

    if title_match:
        insert_pos = head_match.start(1) + title_match.end(0)
        new_head = head_content[:title_match.end(0)] + '\n' + insert_block + head_content[title_match.end(0):]
    else:
        new_head = insert_block + head_content

    # preserve existing viewport if added above
    text = text[:head_match.start(1)] + new_head + text[head_match.end(1):]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated:', rel)
PY