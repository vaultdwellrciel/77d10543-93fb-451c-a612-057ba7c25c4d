import codecs
import os

from distutils.core import setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


setup(
    name='kik',
    version='1.0.7',
    packages=['kik', 'kik.messages'],
    package_dir={
        'kik': 'kik',
        'kik.messages': 'kik/messages'
    },

    author='kik',
    author_email='bots@kik.com',

    url='https://dev.kik.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],

    long_description=read("README.rst"),

    install_requires=[
        'requests>=2.3.0',
        'six==1.10.0'
    ]
)
