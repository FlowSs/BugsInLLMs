def is_valid(self, identifier):
	"""
	Return True if identifier is valid, always True in this base implementation.
	"""
	return True

class EntityIds(object):
	"""
	This class is used to provide the ability to reference an entity from a database.
	"""
	def __init__(self, id, name):
		"""
		Constructor for EntityIds.
		
		:param id: The entity id.
		:type id: int
		:param name: The entity name.
		:type name: str
		"""
		self.id = id
		self.name = name

class EntityId(object):
	"""
	This class is used to provide the ability to reference an entity from a database.
	"""
	def __init__(self, id, name):
		"""
		Constructor for EntityIds.
		
		:param id: The entity id.
		:type id: int
		:param name: The entity name.
		:type name: str
		"""
		self.id = id
		self.name = name

class Dataset(object):
	"""
	This class is used to represent a dataset.
	"""
	def __init__(self, name, identifier, is_valid, parent_id, parent_name):
		"""
		Constructor for Dataset.
		
		:param name: The dataset name.
		:type name: str
		:param identifier: The entity id.
		:type identifier: EntityId
		:param is_valid: If true, the dataset is valid.
		:type is_valid: bool
		:param parent_id: The dataset parent id.
		:type parent_id: int
		:param parent_name: The dataset parent name.
		:type parent_name: str
		"""
		self.name = name
		self.identifier = identifier
		self.is_valid = is_valid
		self.parent_id = parent_id
		self.parent_name = parent_name

class DatasetIds(object):
	"""
	This class is used to provide the ability to reference an entity from a database.
	"""
	def __init__(self, id, name):
		"""
		Constructor for DatasetIds.
		
		:param id: The entity id.
		:type id: int
		:param name: The entity name.
		:type name: str
		"""
		self.id = id
		self.name = name

class DatasetName(object):
	"""
	This class is used to provide the ability to refer to a dataset from a database.
	"""
	def __init__(self, name, identifier):
		"""
		Constructor for DatasetName.
		
		:param name: The dataset name.
		:type name: str
		:param identifier: The entity id.
		:type identifier: EntityId
		"""
		self.name = name
		self.identifier = identifier

class DatasetParentIds(object):
	"""
	This class is used to provide the ability to reference an entity from a database.
	"""
	def __init__(self, id, name):
		"""
		Constructor for DatasetParentIds.
		
		:param id: The entity id.
		:type id: int
		:param name: The entity name.
		:type name: str
		"""
		self.id = id
		self.name = name

class DatasetParentName(object):
	"""
	This class is used to provide the ability to refer to a dataset from a database.
	"""
	def __init__(self, name, identifier):
		"""
		Constructor for DatasetParentName.
		
		:param name: The dataset name.
		:type name: str
		:param identifier: The entity id.
		:type identifier: EntityId
		"""
		self.name = name
		self.identifier = identifier

class DatasetParent(object):
	"""
	This class is used to refer to a dataset from a database.
	"""
	def __init__(self, name, identifier):
		"""
		Constructor for DatasetParent.
		
		:param name: The dataset name.
		:type name: str
		:param identifier: