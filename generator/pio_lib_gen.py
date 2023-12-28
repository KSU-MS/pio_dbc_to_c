# TODO get and build dbcppp if needed
# TODO get dbc file from url or local file
# TODO run dbcppp on supplied dbc file

import os
import hashlib
import pathlib

import subprocess

import docker
import SCons.Action

import tarfile
from platformio import fs

# based on https://github.com/nanopb/nanopb/blob/master/generator/platformio_generator.py

Import("env")

python_exe = env.subst("$PYTHONEXE")
project_dir = env.subst("$PROJECT_DIR")
build_dir = env.subst("$BUILD_DIR")

generated_src_dir = os.path.join(build_dir, 'dbcppp', 'generated-src')
generated_build_dir = os.path.join(build_dir, 'dbcppp', 'generated-build')

user_dbc_file =  env.subst(env.GetProjectOption("user_dbc", ""))
drvname=  env.subst(env.GetProjectOption("drvname", ""))
dbc_file = fs.match_src_files(project_dir, user_dbc_file)
rel_dir_dbc_path = os.path.dirname(dbc_file[0])

dbc_file_name = os.path.basename(dbc_file[0])

import tarfile

def copy_to(src, dst):
    name, dst = dst.split(':')
    container = client.containers.get(name)

    os.chdir(os.path.dirname(src))
    srcname = os.path.basename(src)
    tar = tarfile.open(src + '.tar', mode='w')
    try:
        tar.add(srcname)
    finally:
        tar.close()

    data = open(src + '.tar', 'rb').read()
    container.put_archive(os.path.dirname(dst), data)


if not len(dbc_file):
    print("[nanopb] ERROR: No file matched pattern:")
    print(f"user_dbcs: {user_dbc_file}")
    exit(1)

print("yo")
print(user_dbc_file)

abs_path_to_dbc = project_dir+'/'+rel_dir_dbc_path

print(abs_path_to_dbc)
print(generated_src_dir)
client = docker.from_env()

client.containers.run('asdf:asdf', './scr.sh '+drvname+' '+,volumes=[abs_path_to_dbc+":/data"], working_dir='/app')
print("hello from lib2")
