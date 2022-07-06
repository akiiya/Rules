#!/usr/bin/env python
# coding=utf-8

import json
import codecs 

host_list = []
rule_list = []

with codecs.open('./Custom.sorl','rb',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.replace('\n','')
        line = line.replace('\r','')
        rule_list.append(line)
        if line.startswith(';'):
            continue
        if line.startswith('*.'):
            host_list.append(line[2:])

with codecs.open('./CustomExtend.txt','rb',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.replace('\n','')
        line = line.replace('\r','')
        if line.startswith(';'):
            continue
        
        if not line.startswith('*.'):
            continue
        
        rule = line
        host = rule[2:]
        
        if host in host_list:
            continue
        
        rule_list.append(rule)
        host_list.append(host)

with codecs.open('./SmartProxy-RulesBackup.json','rb',encoding='utf-8') as f:
    for item in json.load(f)['proxyRules']:
        host = item['hostName']
        rule = '*.{host}'.format(host=host)
        if host in host_list:
            continue
        host_list.append(host)
        rule_list.append(rule)

with codecs.open('./Custom.sorl','wb',encoding='utf-8') as f:
    f.write('\n'.join(rule_list))