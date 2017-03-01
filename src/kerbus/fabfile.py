#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from fabric.api import env, local, run, settings, abort, lcd, cd, roles, put
from fabric.contrib.console import confirm


env.roledefs = {
   'root': ['root@django',],
   'user': ['django@django',],
}

def _get_prod_file_list():
    return [
             os.path.join('src', _get_repo_name()),
             'src/static/',
             'requirements.txt',
             'webpack-stats-prod.json',
             'LICENSE',
             'README.md',
           ]


def _get_django_path():
    fname = os.path.realpath(__file__)
    return os.path.dirname(fname)
    

def _get_project_path():
    django = _get_django_path()
    return os.path.normpath(os.path.join(django, '../../'))


def _get_repo_name():
    return os.path.basename(_get_django_path())


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


def replace_path_stats():
    prj = _get_project_path()
    # src = os.path.join(prj, 'src') 
    src = prj
    dst = os.path.join('/webapps', _get_repo_name())
    target = os.path.join(prj, 'webpack-stats-prod.json')
    output = target + '.out'
    with open(target, 'r') as inf:
        with open(output, 'w') as outf:
             for line in inf:
                 outf.write(line.replace(src, dst))
    print "output file: ", output


def create_tar():
    with lcd("../../"):
         arc = _get_repo_name() + '.tar.bz2'
         local("tar cvfj " + 
                arc + ' ' + 
                "--exclude='*.pyc' " +
                "--exclude='local_settings.py' " +
                " ".join(_get_prod_file_list()))

@roles('user')
def upload_tar():
    prj_name = _get_repo_name()
    target = prj_name + '.tar.bz2'
    with cd("/webapps/"):
        with lcd("../../"):
            put(target, prj_name)


@roles('user')
def untar():
    prj_name = _get_repo_name()
    target = prj_name + '.tar.bz2'
    with cd("/webapps/" + prj_name):
         run('tar xvfj ' + target)
