from distutils.core import setup
from setuptools import find_packages

setup(
    name='tango-voting',
    version='0.4.1',
    author='Jonathan Buchanan/Tim Baxter',
    author_email='mail.baxter@gmail.com',
    url='https://github.com/tBaxter/django-voting',
    license='LICENSE',
    description="""Generic voting application for Django,
      based on django-voting by Jonathan Buchanan""",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'],
)
