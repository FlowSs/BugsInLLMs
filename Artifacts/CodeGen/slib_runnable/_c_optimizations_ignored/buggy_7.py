def _c_optimizations_ignored():
	"""
	The opposite of `_c_optimizations_required`.
	"""
	return [
		'__global__',
		'_c_map_handler',
		'_c_map_handler_python_api'
	]
import os
import json
import csv
import pandas as pd

from data_processing import read_csv, read_samples, read_samples_as_dict, read_samples_as_list
from data_processing import read_labels_csv, read_labels_json

