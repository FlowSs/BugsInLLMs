def files_list_from_zipfile(zip_path):
	"""
	Return the files in `zip_path`

Example:

```
[
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200069.pdf',
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200069.xml',
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200071.pdf',
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200071.xml',
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200071-gf01.tif',
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200071-gf02.tif',
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200071-gf03.tif',
    '2318-0889-tinf-33-0421/2318-0889-tinf-33-e200071-gf04.tif',
]
```
	"""
	files = [f for f in os.listdir(zip_path) if os.path.isfile(os.path.join(zip_path, f))]
	return files

