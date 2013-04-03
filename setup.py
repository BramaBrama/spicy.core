"""spicy core package"""
from importlib import import_module
from setuptools import setup, find_packages

version = import_module('src').__version__
long_description = """spicy core package"""


def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open('README.rst').read()
    except IOError:
        return long_description

setup(
    name='spicy',
    version=version,
    author='Burtsev Alexander',
    author_email='eburus@gmail.com',
    description='spicy',
    license='BSD',
    keywords='django, cms',
    url='', # TODO: define an url

    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    include_package_data=True,
    zip_safe=False,
    long_description=long_description(),
    install_requires=[
        'Django==1.4.3',
        'Fabric==1.6',
        'Sphinx==1.2b1',
        'raven==3.2.1',
        'python-memcached==1.48',

        # ?? siteskin deps.
        'pytils==0.2.3',
        'pytz',
        'html5lib',

        # profile deps.
        'django-captcha==0.1.7',
        'django-social-auth==0.7.13.dev',

        # service deps.
        #

    ],
    dependency_links=[
        'svn+http://django-simple-captcha.googlecode.com/svn/trunk@54#egg=django-captcha-0.1.7',
        'git+https://github.com/krvss/django-social-auth.git#egg=django-social-auth-0.7.13.dev',
    ],
    entry_points={
        'console_scripts': [
            'spicy = spicy.script:handle_command_line',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Development Status :: 1.1',
        'Topic :: Internet',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
