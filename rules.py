from common import unique
def registry(data):
    rows=unique(data['rules'],'rule_id')
    for r in rows.values():
        if r['valid_to']<=r['valid_from'] or r['jurisdiction'] not in data['jurisdictions']:raise ValueError('条款时效或辖区非法')
    for r in rows.values():
        if any(i not in rows for i in r['references']):raise ValueError('条款引用不存在')
    return {'rows':rows,'references':{k:tuple(v['references']) for k,v in rows.items()}}
