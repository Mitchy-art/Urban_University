import sys
from pprint import pprint


def introspection_info(obj):
    #dict_obj = vars(obj) ???
    type_obj = type(obj).__name__
    argv_obj = sys.argv
    attr_obj = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    method_obj = [method for method in dir(obj) if callable(getattr(obj, method))]
    module_obj = obj.__class__.__module__ #getattr(obj, '__module__', 'N/A') ???
    info = {'type': type_obj, 'attributes': attr_obj, 'method': method_obj, 'module': module_obj, 'argv': argv_obj}
    return info


number_info = introspection_info(42)
pprint(number_info)
