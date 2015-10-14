#!/usr/bin/env python
from setuptools import setup
from setuptools.command.develop import develop as _develop
from setuptools.command.sdist import sdist as _sdist
from setuptools.command.install import install as _install


def install_regexes():
    print('Copying regexes.yaml to package directory...')
    import os
    import shutil
    cwd = os.path.abspath(os.path.dirname(__file__))
    yaml_src = os.path.join(cwd, 'uap-core', 'regexes.yaml')
    if not os.path.exists(yaml_src):
        raise RuntimeError(
                  'Unable to find regexes.yaml, should be at %r' % yaml_src)
    yaml_dest = os.path.join(cwd, 'ua_parser', 'regexes.yaml')
    shutil.copy2(yaml_src, yaml_dest)

    print('Converting regexes.yaml to regexes.json...')
    import json
    import yaml
    json_dest = yaml_dest.replace('.yaml', '.json')
    regexes = yaml.safe_load(open(yaml_dest))
    with open(json_dest, "w") as f:
        json.dump(regexes, f)


class develop(_develop):
    def run(self):
        install_regexes()
        _develop.run(self)


class sdist(_sdist):
    def run(self):
        install_regexes()
        _sdist.run(self)


class install(_install):
    def run(self):
        install_regexes()
        _install.run(self)

setup(
    name='ua-parser',
    version='0.5.0',
    description="Python port of Browserscope's user agent parser",
    author='PBS',
    author_email='no-reply@pbs.org',
    packages=['ua_parser'],
    package_dir={'': '.'},
    license='LICENSE.txt',
    zip_safe=False,
    url='https://github.com/ua-parser/uap-python',
    include_package_data=True,
    package_data={'ua_parser': ['regexes.yaml', 'regexes.json']},
    setup_requires=['pyyaml'],
    install_requires=['pyyaml'],
    cmdclass={
        'develop': develop,
        'sdist': sdist,
        'install': install,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
