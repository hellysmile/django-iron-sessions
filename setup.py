from setuptools import setup


classifiers = '''\
Framework :: Django
Environment :: Web Environment
Intended Audience :: Developers
Topic :: Internet :: WWW/HTTP
License :: OSI Approved :: Apache Software License
Development Status :: 5 - Production/Stable
Natural Language :: English
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
'''

description = 'Iron Cache Session Backend For Django'

packages = ['iron_sessions', ]


# no with statement for python 2.5
def long_description():
    f = open('README.rst')
    rst = f.read()
    f.close()
    return rst


setup(
    name='django-iron-sessions',
    version='0.0.1',
    packages=packages,
    description=description,
    long_description=long_description(),
    author='hellysmile',
    author_email='hellysmile@gmail.com',
    url='https://github.com/hellysmile/django-iron-sessions',
    zip_safe=False,
    install_requires=[
        'django >= 1.4',
        'iron-cache == 0.2.0'
    ],
    license='http://www.apache.org/licenses/LICENSE-2.0',
    classifiers=filter(None, classifiers.split('\n')),
    keywords=[
        "django", "sessions", "iron cache", "heroku"
    ]
)
