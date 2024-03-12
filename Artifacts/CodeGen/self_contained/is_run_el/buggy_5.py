def is_run_el(obj):
	"""
	Object contains executable method 'run'.
	"""
	return obj.__name__ == 'run'

class Executable(object):
	"""
	This class represents an executable. It has an executable name and
	an associated object.
	"""
	def __init__(self, name, obj):
		"""
		Constructor.
		"""
		self.name = name
		self.obj = obj

	def __eq__(self, other):
		"""
		Equation equality.
		"""
		if not isinstance(other, Executable):
			return False
		if self.name == other.name:
			return self.obj == other.obj
		return False

	def __ne__(self, other):
		"""
		Not equal.
		"""
		return not self.__eq__(other)

	def __call__(self):
		"""
		Execute function.
		"""
		return self.obj()

	def __str__(self):
		"""
		String representation.
		"""
		return '<%s object at 0x%x>' % (self.name, id(self))

class Executables(object):
	"""
	This class represents a collection of executable objects.
	"""
	def __init__(self):
		"""
		Constructor.
		"""
		self.executables = {}
		self.default_executable = Executable('Default', Executable('default', Executable('default')))
		self.default_executable.obj = Executable('default', Executable('default'))
		self.default_executable.ex = Executable('default', Executable('default'))

	def add_executable(self, name, obj):
		"""
		Add executable object.
		"""
		self.executables[name] = obj

	def get_executable(self, name):
		"""
		Get executable object.
		"""
		return self.executables[name]

	def __str__(self):
		"""
		String representation.
		"""
		s = 'Executables:\n'
		for name, obj in self.executables.items():
			s += '\t%s:\n' % name
			s += '\t\tid: %d\n' % id(obj)
			s += '\t\tname: %s\n' % str(type(obj))
			s += '\t\tdescription: %s\n' % str(obj.__doc__)
			s += '\t\targs: %s\n' % str(obj.args)
			s += '\t\tkwargs: %s\n' % str(obj.kwargs)
			s += '\t\treturns: %s\n' % str(obj.ret)
			s += '\t\tex: %s\n' % str(obj.ex)
			s += '\t\tex_id: %s\n' % str(id(obj))
			s += '\t\tex_name: %s\n' % str(name)
			s += '\t\tex_args: %s\n' % str(obj.args)
			s += '\t\tex_kwargs: %s\n' % str(obj.kwargs)
			s += '\t\tex_ret: %s\n' % str(obj.ret)
			s += '\t\tex_ex: %s\n' % str(obj.ex)
			s += '\t\tex_ex_id: %s\n' % str(id(obj))
			s += '\t\tex_ex_name: %s\n' % str(name)
			s += '\t\tex_ex_args: %s\n' % str(obj.args)
			s += '\t\tex_ex_kwargs: %s\n' % str(obj.kwargs)
			s += '\t\tex_ex_ret: %s\n' % str(obj.ret)
			s += '\t\tex_ex_ex: %s\n' % str(obj.ex)
			s += '\t\tex_ex