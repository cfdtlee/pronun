#!/usr/bin/env python
# coding=utf-8
import urllib2
import re
'''def get_content_by_proxy(url, proxy):
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxy}), urllib2.HTTPHandler(debuglevel=1))
    urllib2.install_opener(opener)
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", \
					"Referer": 'http://www.baidu.com'}
    req = urllib2.Request(url, headers=i_headers)
    content = urllib2.urlopen(req).read()
    return content
''' 
def get_url_content(url):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
                 "Referer": 'http://www.baidu.com'}
    req = urllib2.Request(url, headers=i_headers)
    return urllib2.urlopen(req).read()

f=open('basic_words_macmillan.txt','r')
fout=open('pron_basic','a');
wordlist=f.readlines()
word_pron=[]
word_pron_url=[]

for i in range(0,len(wordlist)):
    url='http://www.macmillandictionary.com/us/dictionary/american/'+wordlist[i];
    html_text=get_url_content(url)
    #pron_str=re.findall(r'美\s*<strong>\[</strong><strong lang="EN-US" xml:lang="EN-US">\D*</strong>',html_text)
    pron_str=re.findall(r'</span>\D*<span class="SEP" context="PRON',html_text)
    pron=pron_str[0][7:-31]
    print pron
    word_pron.append(pron)
    pron_str=re.findall(r'data-src-mp3="http://www.macmillandictionary.com/us/media/american/\D*\d*.mp3',html_text)
    pron=pron_str[0][14:len(pron_str[0])]
    print pron
    word_pron_url.append(pron)
    fout.write(wordlist[i][0:-2]+' '+word_pron[i]+' '+word_pron_url[i]+'\n')

f.close()
fout.close()
#url   = 'http://www.iciba.com/word' 
#url='http://fanyi.baidu.com/#en/zh/top'
'''
url='http://www.macmillandictionary.com/us/dictionary/american/top'
#proxy = '24.48.219.49:8080'  #ok
proxy = '54.251.183.68:2013'
#proxy = '221.204.223.38:1080'
opener = urllib2.build_opener( urllib2.ProxyHandler({'http':proxy}) ) 
urllib2.install_opener( opener ) 
sContent = urllib2.urlopen(url) 
print sContent.read()
    
    <span class="fl">美    <strong>[</strong><strong lang="EN-US" xml:lang="EN-US">tɑp</strong><strong>]</strong>
				</span>'''
