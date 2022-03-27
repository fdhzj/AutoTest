import os
import importlib

DIR = '/scripts'


class PyLibs(object):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self._keywords = self._scan_name_and_keywords()
        #print(self._keywords)

    def get_keyword_names(self):
        return list(self._keywords.keys())

    def __getattr__(self, name):
        try:
            return self._keywords[name]
        except KeyError:
            raise AttributeError

    def _scan_name_and_keywords(self):
        kw_name_and_obj_dict = {}
        keywords = self._scan_class()
        for keyword in keywords:
            name = keyword.__name__
            if name == "test_测试1加1等于0":
                print(keyword)
            if name in kw_name_and_obj_dict:
                raise Exception("{0} already exist, the name of method must be unique".format(name))
            kw_name_and_obj_dict[name] = keyword
        return kw_name_and_obj_dict

    def _scan_class(self):
        kws = []
        script_files = self._scan_files()
        for script_file in script_files:
            dir_list = script_file.split(os.sep)
            dir_list = dir_list[dir_list.index("PyLibs"):]
            dir_list[len(dir_list)-1] = '__init__'
            mod = __import__(".".join(dir_list), globals(), fromlist=dir_list[:-1])
            for item in dir(mod):
                if item.startswith('_'):
                    continue
                attr = getattr(mod, item)
                self._scan_keywords(kws, attr)
        return kws

    def _scan_files(self):
        script_files = []
        basedir = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'scripts'
        for root, dirs, files in os.walk(basedir):
            for file in files:
                if file == '__init__.py':
                    script_files.append(os.path.join(root, file))
        return script_files

    def _scan_keywords(self, kws, attr):
        class_obj = attr()
        for keywords in dir(class_obj):
            if keywords.startswith("test") or keywords.startswith("setup") or keywords.startswith("teardown"):
                kws.append(getattr(class_obj, keywords))
        return kws


if __name__ == '__main__':
    test = PyLibs()
