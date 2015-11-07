
try:
	import numpy
except ImportError:
	NUMPY_MODE = False
	from .nonp import dumps, dump, loads, load, strip_hash_comments
else:
	NUMPY_MODE = True
	from .np import dumps, dump, loads, load, strip_hash_comments


__all__ = ['dumps', 'dump', 'loads', 'load', 'strip_hash_comments']


