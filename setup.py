
import codecs
import os
import sys

from distutils.util import convert_path
from fnmatch import fnmatchcase
from setuptools import setup, find_packages


PACKAGE = "."
NAME = "mercury-community"
DESCRIPTION = "mercury-community 1.2.0"
AUTHOR = "taotao.li"
AUTHOR_EMAIL = "taotao.li@datayes.com"
URL = "www.datayes.com"
VERSION = "1.2.0"

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


# Provided as an attribute, so you can append to these instead
# of replicating them:
standard_exclude = ["*.py", "*.pyc", "*$py.class", "*~", ".*", "*.bak"]
standard_exclude_directories = [
    ".*", "CVS", "_darcs", "./build", "./dist", "EGG-INFO", "*.egg-info"
]


# (c) 2005 Ian Bicking and contributors; written for Paste (http://pythonpaste.org)
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
# Note: you may want to copy this into your setup.py file verbatim, as
# you can't import this from another package, when you don't know if
# that package is installed yet.
def find_package_data(
    where=".",
    package="",
    exclude=standard_exclude,
    exclude_directories=standard_exclude_directories,
    only_in_packages=True,
    show_ignored=False):
    """
    Return a dictionary suitable for use in ``package_data``
    in a distutils ``setup.py`` file.

    The dictionary looks like::

        {"package": [files]}

    Where ``files`` is a list of all the files in that package that
    don"t match anything in ``exclude``.

    If ``only_in_packages`` is true, then top-level directories that
    are not packages won"t be included (but directories under packages
    will).

    Directories matching any pattern in ``exclude_directories`` will
    be ignored; by default directories with leading ``.``, ``CVS``,
    and ``_darcs`` will be ignored.

    If ``show_ignored`` is true, then all the files that aren"t
    included in package data are shown on stderr (for debugging
    purposes).

    Note patterns use wildcards, or can be exact paths (including
    leading ``./``), and all searching is case-insensitive.
    """
    out = {}
    stack = [(convert_path(where), "", package, only_in_packages)]
    while stack:
        where, prefix, package, only_in_packages = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "Directory %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                if (os.path.isfile(os.path.join(fn, "__init__.py"))
                    and not prefix):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + "." + name
                    stack.append((fn, "", new_package, False))
                else:
                    stack.append((fn, prefix + name + "/", package, only_in_packages))
            elif package or not only_in_packages:
                # is a file
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        if show_ignored:
                            print >> sys.stderr, (
                                "File %s ignored by pattern %s"
                                % (fn, pattern))
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data=find_package_data(PACKAGE, only_in_packages=False),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)


# from distutils.core import setup
# from setuptools import find_packages
# import os, time





# file_paths = []
# snap_shot = time.strftime('%Y%m%d%H%M%S')


# def filter_files(dir, suffix_end, suffix_contains, topdown=True):
#     for root, dirs, files in os.walk(dir, topdown):
#         for path in files:
            
#             path = '%s/%s' %(root, path)
#             path = path.replace(root_dir + '/', '')

#             if any([path.endswith(suf) for suf in suffix_end]) or \
#                any([path.find(suf)!=-1 for suf in suffix_contains]):
#                continue
#             file_paths.append(path)

#         for dir_f in dirs:
#             dir_f = '%s/%s' %(root, dir_f)
#             filter_files(dir_f, suffix_end, suffix_contains)


# root_dir = os.getcwd()
# filter_files(root_dir, ['.conf'], ['.svn'])

# setup(
#     package=PACKAGE,
#     name=NAME,
#     version=VERSION,
#     description=DESCRIPTION,
#     packages=find_packages(),
#     include_package_data=True,
#     classifiers=[
#         "Development Status :: 3 - Alpha",
#         "Environment :: Web Environment",
#         "Intended Audience :: Developers",
#         "License :: OSI Approved :: BSD License",
#         "Operating System :: OS Independent",
#         "Programming Language :: Python",
#         "Framework :: Django",
#     ],
#     zip_safe=False,
# )

# # setup(
# #     name=NAME,
# #     version=VERSION,
# #     description=DESCRIPTION,
# #     long_description=file("README.rst",'r').read(),
# #     author=AUTHOR,
# #     author_email=AUTHOR_EMAIL,
# #     license="commercial",
# #     url=URL,
# #     data_files = [
# #                     ('py', file_paths),
# #                     ],
# #     classifiers=[
# #         "Development Status :: 3 - Alpha",
# #         "Environment :: PC test",
# #         "Intended Audience :: Developers",
# #         "License :: OSI Approved :: BSD License",
# #         "Operating System :: OS Independent",
# #         "Programming Language :: Python 2.7",
# #         "Framework :: none",
# #     ],
# # )


# # os.system("mv dist/mercury-community-%s.tar.gz dist/mercury-community.tar.gz" %VERSION)