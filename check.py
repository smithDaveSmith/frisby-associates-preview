#!/usr/bin/env python3
"""Check the actual export: routes, local assets, anchors and preview protections."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
ROOT=Path(__file__).resolve().parent; OUT=ROOT/'dist'; errors=[]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.h1=0;self.robots=False;self.images=[];self.labels=set();self.controls=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:
   if d['id'] in self.ids:errors.append('duplicate id '+d['id'])
   self.ids.add(d['id'])
  if t=='h1':self.h1+=1
  if t=='meta' and d.get('name')=='robots':self.robots='noindex' in d.get('content','')
  if t in ['a','link'] and d.get('href'):self.refs.append(d['href'])
  if t in ['script','img'] and d.get('src'):self.refs.append(d['src'])
  if t=='img' and not ('alt' in d and 'width' in d and 'height' in d):errors.append('image missing alt or dimensions')
  if t=='label':self.labels.add(d.get('for'))
  if t in ['input','textarea','select']:self.controls.append(d)
files=list(OUT.rglob('*.html')); pages={}
for f in files:
 p=Page();p.feed(f.read_text());pages[f.resolve()]=p
 if p.h1!=1:errors.append(str(f.relative_to(OUT))+': expected one H1')
 if not p.robots:errors.append(str(f)+': noindex missing')
 for d in p.controls:
  if not (d.get('id') in p.labels or d.get('aria-label')):errors.append(str(f)+': unlabelled form control')
# Derive base from the stylesheet URL in the real output, independent of environment.
sample=pages[(OUT/'index.html').resolve()];css=next(r for r in sample.refs if r.endswith('assets/styles.css'));base=css[:-len('assets/styles.css')]
for f,p in pages.items():
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  raw=unquote(u.path)
  if raw.startswith('/'):
   if not raw.startswith(base):errors.append(str(f)+': outside repository '+ref);continue
   target=OUT/raw[len(base):]
  else:target=f.parent/raw if raw else f
  if target.is_dir() or raw.endswith('/'):target=target/'index.html'
  if not target.is_file():errors.append(str(f)+': missing '+ref);continue
  if u.fragment and target.suffix=='.html' and u.fragment not in pages[target.resolve()].ids:errors.append(str(f)+': missing anchor '+ref)
for f in (OUT/'assets/archive').glob('*.pdf'):
 if not f.read_bytes().startswith(b'%PDF-'):errors.append(str(f)+': invalid PDF')
if errors:
 print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(files)} HTML pages, all internal links/assets/anchors, form labels, image dimensions, and noindex. Base {base}')
