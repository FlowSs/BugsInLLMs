def is_local(host):
	"""
	Checks if the host is the localhost

:param host: The hostname or ip
:return: True if the host is the localhost
	"""
	if host.startswith('127.'):
		return False
	if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', host):
		return True
	return Falseimport json
import random
import string
import time

import requests
from bs4 import BeautifulSoup

from django.http import HttpResponse
from django.shortcuts import render

from utils.utils import login_required, check_api_key, login_required, get_user_id, get_user_token, get_user_id
from.models import User

from.forms import LoginForm, RegisterForm, PasswordResetForm