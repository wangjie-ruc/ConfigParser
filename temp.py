import sys
import importlib

filename = 'config.py'
module_name = 'config'

if module_name not in sys.modules:
    module = type(sys)(module_name)
    sys.modules[module_name] = module

setattr(module, 'root', '/data/visda')

spec = None
for finder in sys.meta_path:
    t = finder.find_spec(module_name, filename)
    if t is not None:
        spec = t
        break
spec.loader.exec_module(module)



sys.path.insert(0, '.')

loader = importlib.util.find_spec('config').loader
code = loader.get_code('config')
importlib.import_module





import ast
import astunparse

filename = 'config.py'
expr = open(filename).read()

expr_tree = ast.parse(expr)
statements = [astunparse.unparse(e) for e in expr_tree.body]