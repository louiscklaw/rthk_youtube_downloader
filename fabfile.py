#!/usr/bin/env python
# coding:utf-8
import os
import sys
import traceback
from pprint import pprint

from fabric.api import cd, local, task, lcd, settings

CWD = os.path.dirname(os.path.abspath(__file__))
DOC_DIR = os.path.sep.join([CWD,'docs'])


def gen_doc():
    with settings(warn_only=True):
        local('mkdir docs')

    SPHINE_QUICISTART_PARAMS=[
        '-q -a louis -v 1'
        '--ext-autodoc',
        '--dot=.',
        '--project=youtube_rthk_downloader',
        '--sep'
    ]

    with lcd(DOC_DIR):
        local('sphinx-quickstart %s' % ' '.join(SPHINE_QUICISTART_PARAMS))
        local('make html')

def del_doc():
    local('rm -rf %s' % DOC_DIR)

def regen_doc():
    with settings(warn_only=True):
        del_doc()
        gen_doc()
