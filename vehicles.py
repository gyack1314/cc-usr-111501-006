from common import unique
def configurations(data):
    out=unique(data['vehicles'],'config_id')
    for r in out.values():
        if r['jurisdiction'] not in data['jurisdictions'] or r['software'] not in data['software_versions'] or r['valid_to']<=r['valid_from']:raise ValueError('车型构型适用范围非法')
    return out
