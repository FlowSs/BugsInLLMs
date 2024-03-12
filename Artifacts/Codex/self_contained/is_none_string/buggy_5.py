def is_none_string(val: any) -> bool:
	return val in (None, 'None', 'none', 'NONE', '', 'Null', 'NULL', 'null', 'NULL', 'nan', 'NaN', 'NAN', 'NA', 'na')


