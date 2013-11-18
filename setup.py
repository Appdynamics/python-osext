from distutils.core import setup

setup(
    name='OSExtension',
    version='0.1.0',
    author='Andrew Udvare',
    author_email='audvare@gmail.com',
    packages=['osext'],
    url='http://pypi.python.org/pypi/OSExtension/',
    license='LICENSE.txt',
    description='Extension for os module, for POSIX systems only',
    long_description=open('README.rst').read(),
)
