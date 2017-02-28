#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from fabric.api import env, local, run, settings, abort, cd, roles
from fabric.contrib.console import confirm



env.roledefs = {
   'root': ['root@django',],
   'user': ['django@django',],
}

def _get_repo_name():
    fname = os.path.realpath(__file__)
    dirname = os.path.dirname(fname)
    return os.path.basename(dirname)

def hello():
    print("Hello, World!")


@roles('user')
def git_pull():
    "Updates the repository."
    run("git pull $(parent) $(branch)")


@roles('user')
def git_reset():
    "Resets the repository to specified version."
    run("git reset --hard $(hash)")


def reload_supervisor():
    "Reloads supvervisord configuration files."
    run("supervisord reload")


def reload_nginx():
    "Reloads nginx configuration files."
    run("supervisord reload")
    run("nginx -s reload")


@roles('user')
def pull():
    for repo, parent, branch in config.repos:
        config.repo = repo
        config.parent = parent
        config.branch = branch
        invoke(git_pull)

def test():
    with settings(warn_only=True):
        result = local('./manage.py test', capture=True)
    if result.failed and not confirm("Tests failed.  Continue anyway?"):
       abort("Aborting at user request.")


@roles('user')
def reset(repo, hash):
    """
    Rest all git repositories to specified hash.
    Usage:
        fab reset:repo=my_repo,hash=etcetc123
    """
    config.hash = hash
    config.repo = repo
    invoke(git_reset)


@roles('user')
def deploy_stage1():
    code_dir = '/webapps/%s/' % _get_repo_name()
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")

