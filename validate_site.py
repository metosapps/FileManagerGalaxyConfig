#!/usr/bin/env python3
"""Validate the local static site's routes/assets and preserve signed app control data."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parent
SITE=ROOT/'site'
class Page(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=[];self.h1=0;self.shots=0;self.main=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='main':self.main+=1
        if 'data-shot' in a:self.shots+=1;self.refs.append(a['data-shot'])
        for name in ['href','src']:
            if name in a:self.refs.append(a[name])
parsed={}
for path in SITE.glob('*.html'):
    p=Page();p.feed(path.read_text());parsed[path.name]=p
for filename,p in parsed.items():
    assert p.h1==1 and p.main==1,filename
    assert len(p.ids)==len(set(p.ids)),filename
    for ref in p.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc:continue
        target=unquote(url.path) or filename
        path=(SITE/target).resolve();assert path.is_relative_to(SITE.resolve()) and path.is_file(),(filename,ref)
        if url.fragment and path.suffix=='.html':assert url.fragment in parsed[path.name].ids,(filename,ref)
assert parsed['index.html'].shots==8
for filename in ['index.html','privacy.html','terms.html','support.html']:
    source=(SITE/filename).read_text();assert 'chennoufo11@gmail.com' in source and 'com.filegx.appsmanager' in source
    assert 'https://galaxystore.samsung.com/detail/com.filegx.appsmanager' in source
assert 'Galaxy Store release in progress' in (SITE/'index.html').read_text()
for name in ['config.json','payload.json']:
    tracked=subprocess.check_output(['git','show','HEAD:site/'+name],cwd=ROOT)
    assert (SITE/name).read_bytes()==tracked,name
print('PASS: four pages, eight gallery items, all local routes/assets/anchors, package/contact, release status and unchanged signed configuration.')
