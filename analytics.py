"""当前资料入口；不实现统计分析目标。"""
import json
from common import read
from rules import registry
from vehicles import configurations
from evidence import coverage
def prepare_sources():
    data=read()
    return {'registry': registry(data), 'configurations': configurations(data), 'coverage': coverage(data)}
if __name__=="__main__":print(json.dumps(prepare_sources(),ensure_ascii=False,default=str,indent=2))