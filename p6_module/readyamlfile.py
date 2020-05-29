# coding: utf-8
import sys, yaml, time

def read_conf(file):
    """Permet la Lecture de fichiers yaml"""
    with open(file, 'r') as stream:
      try:
        return yaml.safe_load(stream)
      except yaml.YAMLError as exc:
          print(exc)
