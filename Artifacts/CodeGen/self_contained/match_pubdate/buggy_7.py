def match_pubdate(node, pubdate_xpaths):
	"""
	Returns the first match in the pubdate_xpaths list
	"""
	
	for pubdate_xpath in pubdate_xpaths:
		if re.match(r'\d+', pubdate_xpath):
			pubdate_xpath = '//span[contains(@class, "date") and contains(text(), "%s")]' % pubdate_xpath
		match = re.search(r'\d+', pubdate_xpath)
		if match:
			return "".join(match.groups())
	return None
	
	
	
	
	
	
	
	
	import os
import sys

from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QActionGroup

import resources.icons as icons
from resources.logger import logger