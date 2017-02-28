#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fabric.api import local, run, require, settings, abort, cd
from fabric.contrib.console import confirm

REPOS = (("kerbus", "origin", "master"),)


def hello():
    print("Hello, World!")


def git_pull():
    "Updates the repository."
    run("git pull $(parent) $(branch)")


def git_reset():
    "Resets the repository to specified version."
    run("git reset --hard $(hash)")


def reload_supervisor():
    "Reloads supvervisord configuration files."
    require('fab_hosts', provided_by[production_root])
    run("supervisord reload")


def reload_nginx():
    "Reloads nginx configuration files."
    require('fab_hosts', provided_by[production_root])
    run("supervisord reload")
    run("nginx -s reload")


def production_user():
    config.fab_hosts = ['django@django',]
    config.repos = REPOS


def production_root():
    config.fab_hosts = ['root@django',]
    config.repos = REPOS


def pull():
    require('fab_hosts', provided_by=[production_user])
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

def reset(repo, hash):
    """
    Rest all git repositories to specified hash.
    Usage:
        fab reset:repo=my_repo,hash=etcetc123
    """
    require("fab_hosts", provided_by=[production_user])
    config.hash = hash
    config.repo = repo
    invoke(git_reset)


def deploy():
    code_dir = '/webapps/kerbus/'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")

