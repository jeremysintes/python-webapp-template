from setuptools.command.test import test as TestCommand
import sys

"""
Integration of tox
python setup.py test
TODO : 
- author, author mail, description... in setup automatically added as version
- check the need for a setup file
"""



here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.rst')


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)



setup(
    name='sandman',
    version=find_version('NAME_OF_THE_PROJECT', '__init__.py'),
    url='http://github.com/jeremysintes/NAME_OF_THE_PROJECT/',
    license='Apache Software License',
    author='Jeff Knupp',
    
    tests_require=['pytest'], #or ['tox'], in this case change cmdclass as well
    install_requires=['Flask>=0.10.1',
                      'Flask-SQLAlchemy>=1.0',
                      'SQLAlchemy>=0.8.2',
                      'Flask-Admin>=1.0.6',
                      'Flask-HTTPAuth>=2.2.1',
                      'docopt>=0.6.1',
                      'click',
                      #'sphinx-rtd-theme',
                      ],
    cmdclass={'test': PyTest},  #or {'test': Tox}, in this case change tests_require as well
    
    author_email='jeremy.sintes@gmail.com',
    description='Automated REST APIs for existing database-driven systems',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'sandmanctl = sandman.sandmanctl:run',
            ],
        },
    packages=['sandman', 'sandman.model'],
    include_package_data=True,
    platforms='any',
    test_suite='sandman.test.test_sandman',
    zip_safe=False,
    package_data={'sandman': ['templates/**', 'static/*/*']},
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    extras_require={
        'testing': ['pytest'],
      }
)






# example with version defined once https://github.com/jeffknupp/sandman/blob/develop/setup.py

# Exemple of the setup.py file created by H. Schlawack for his attrs module : 

"""
import codecs
import os
import re

from setuptools import setup, find_packages


###################################################################

NAME = "attrs"
PACKAGES = find_packages(where="src")
META_PATH = os.path.join("src", "attr", "__init__.py")
KEYWORDS = ["class", "attribute", "boilerplate"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
INSTALL_REQUIRES = []

###################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):

    # Build an absolute path from *parts* and and return the contents of the
    # resulting file.  Assume UTF-8 encoding.
    
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    
    # Extract __*meta*__ from META_FILE.
    
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=find_meta("uri"),
        version=find_meta("version"),
        author=find_meta("author"),
        author_email=find_meta("email"),
        maintainer=find_meta("author"),
        maintainer_email=find_meta("email"),
        keywords=KEYWORDS,
        long_description=read("README.rst"),
        packages=PACKAGES,
        package_dir={"": "src"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
    )

"""