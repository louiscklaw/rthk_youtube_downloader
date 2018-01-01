#!/usr/bin/env python
# coding:utf-8
import os
import sys
import traceback
from pprint import pprint

from fabric.api import cd, local, task, lcd, settings, env, run

CWD = os.path.dirname(os.path.abspath(__file__))
DOC_DIR = os.path.sep.join([CWD,'docs'])


env.hosts=['192.168.88.6']
env.user='logic'

def get_current_branch_name():
    temp = local("git branch | sed -n '/\* /s///p'", capture=True)
    return temp.strip()

def test_download():
    local('git push')
    current_branch = get_current_branch_name()
    with cd('/mnt/backup/tmp/rthk_youtube_downloader'):
        run('git reset --hard %s' % current_branch)
        run('git pull')
        run('pipenv --three')
        run('pipenv update')
        run('pipenv shell python3 test.py')
