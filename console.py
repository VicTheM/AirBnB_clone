#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import re
import cmd
import json
from models import storage, MODELS

# A regular expression to catch object patternes
regex = [
    r'^(\w+)\.(\w+)\(\)$',
    r'^(\w+)\.(\w+)\("([^"|.]*?)"\)$',
    r'^(\w+)\.(\w+)\("(.*?)",\s"(.*?)",\s(".*?")\)$',
    r'^(\w+)\.(\w+)\("(.*?)",\s"(.*?)",\s([0-9].*?)\)$',
    r'^(\w+)\.(\w+)\("(.*?)",\s(\{.*?\})\)$'
    ]
