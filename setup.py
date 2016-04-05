from distutils.core import setup

setup(
    name='kik',
    version='1.0.1',
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

    install_requires=[
        'requests>=2.3.0',
        'six==1.10.0'
    ]
)
