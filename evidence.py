from common import unique
from rules import registry
from vehicles import configurations
def coverage(data):
    rr=registry(data)['rows'];vv=configurations(data);rows=unique(data['evidence'],'evidence_id')
    for r in rows.values():
        if r['config_id'] not in vv or r['rule_id'] not in rr or r['valid_to']<=r['valid_from']:raise ValueError('验证证据范围非法')
        if r['report_version'] not in data['report_versions']:raise ValueError('报告版本未知')
    return {'evidence':rows,'uncovered_rules':sorted(set(rr)-{r['rule_id'] for r in rows.values()}),'configurations':vv}
