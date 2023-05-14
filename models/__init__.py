#!/usr/bin/env python3
""" __init__ magic method initializes the package"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
