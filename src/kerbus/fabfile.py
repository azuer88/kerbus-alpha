#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from fabric.api import env, settings, abort, execute, roles
from fabric.api import lcd, cd, put, run, local
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


@roles('root')
def reload_supervisor():
    "Reloads supvervisord configuration files."
    run("supervisorctl reload")


@roles('root')
def reload_nginx():
    "Reloads nginx configuration files."
    run("nginx -s reload")


def reload_servers():
    execute(reload_supervisor)
    execute(reload_nginx)


def test():
    with settings(warn_only=True):
        result = local('./manage.py test', capture=True)
    if result.failed and not confirm("Tests failed.  Continue anyway?"):
       abort("Aborting at user request.")

def collectstatic():
    local('./manage.py collectstatic --no-input')

def _replace_path_stats():
    prj = _get_project_path()
    # src = os.path.join(prj, 'src') 
    src = prj
    dst = os.path.join('/webapps', _get_repo_name())
    target = os.path.join(prj, 'webpack-stats-prod.json')
    output = target + '.out'
    with open(target, 'r') as inf,  open(output, 'w') as outf:
        for line in inf:
            outf.write(line.replace(src, dst))


def create_tar():
    local('npm run build-production')
    with lcd("../../"):
         arc = _get_repo_name() + '.tar.bz2'
         local("tar cvfj " + 
                arc + ' ' + 
                "--exclude='*.pyc' " +
                "--exclude='fabfile.py' " +
                "--exclude='local_settings.py' " +
                " ".join(_get_prod_file_list()))

@roles('user')
def upload_tar():
    "upload tar of files to deploy."
    prj_name = _get_repo_name()
    target = prj_name + '.tar.bz2'
    with cd("/webapps/"), lcd("../../"):
            put(target, prj_name)


@roles('user')
def untar():
    "untar the upload archive file."
    prj_name = _get_repo_name()
    target = prj_name + '.tar.bz2'
    with cd("/webapps/" + prj_name):
         run('tar xvfj ' + target)


def deploy():
    "deploy files to the django production server."
    execute(test)
    execute(collectstatic)
    execute(create_tar)
    execute(upload_tar)
    execute(untar)
    execute(reload_servers)
