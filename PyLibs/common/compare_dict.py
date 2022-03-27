from PyLibs.common.baseAssert import BaseAssert


def cmp_ad_dict(dict1: object, dict2: object) -> object:
    BaseAssert(sorted(dict1) == sorted(dict2), "预期两个字典值一直，实际不一致，分别为{0}和{1}".format(dict1, dict2))
