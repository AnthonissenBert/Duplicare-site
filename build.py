import os, re, sys

with open('partials/navbar.html') as f:
    navbar = f.read()
with open('partials/footer.html') as f:
    footer = f.read()

pages = {
    'index.html':        {'prefix': '',       'logo': 'assets/header/Wapenschild.png',         'active': {'HOME': 'active'}},
    'pages/club.html':   {'prefix': '../',    'logo': '../assets/header/Wapenschild.png',      'active': {'INFO': 'active', 'INFO_ROOT': 'active'}},
    'pages/bacchus.html':{'prefix': '../',    'logo': '../assets/header/Wapenschild.png',      'active': {'INFO': 'active', 'INFO_ROOT': 'active'}},
    'pages/lid.html':    {'prefix': '../',    'logo': '../assets/header/Wapenschild.png',      'active': {'LID': 'active'}},
    'pages/fotogalerij.html': {'prefix': '../','logo': '../assets/header/Wapenschild.png',     'active': {'FOTOGALERIJ': 'active'}},
    'pages/praesidium.html':  {'prefix': '../','logo': '../assets/header/Wapenschild.png',     'active': {'PRAESIDIUM': 'active', 'PRAESIDIUM_ROOT': 'active'}},
    'pages/geschiedenis.html':{'prefix': '../','logo': '../assets/header/Wapenschild.png',     'active': {'PRAESIDIUM': 'active', 'PRAESIDIUM_ROOT': 'active'}},
    'pages/prosenioren.html': {'prefix': '../','logo': '../assets/header/Wapenschild.png',     'active': {'PRAESIDIUM': 'active', 'PRAESIDIUM_ROOT': 'active'}},
    'pages/erefuncties.html': {'prefix': '../','logo': '../assets/header/Wapenschild.png',     'active': {'PRAESIDIUM': 'active', 'PRAESIDIUM_ROOT': 'active'}},
}

all_keys = ['HOME', 'INFO', 'INFO_ROOT', 'LID', 'FOTOGALERIJ', 'PRAESIDIUM', 'PRAESIDIUM_ROOT']

for file, cfg in pages.items():
    with open(file) as f:
        content = f.read()

    rendered = navbar.replace('{PREFIX}', cfg['prefix']).replace('{LOGO_PATH}', cfg['logo'])

    for key in all_keys:
        val = cfg['active'].get(key, '')
        rendered = rendered.replace('{ACTIVE_' + key + '}', val)

    content = content.replace('<!--NAVBAR-->', rendered)
    content = content.replace('<!--FOOTER-->', footer)

    with open(file, 'w') as f:
        f.write(content)
    print(f'Built: {file}')

print('All pages built.')
