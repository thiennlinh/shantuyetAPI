from __future__ import absolute_import, unicode_literals

import environ

environ.Env.read_env("environments.env")

from .base import *
from .apps import *
from .database import *