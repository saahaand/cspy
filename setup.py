from setuptools import setup, find_packages
from setuptools import find_packages, setup
from setuptools.dist import Distribution
from setuptools.command.install import install


class BinaryDistribution(Distribution):

    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True


class InstallPlatlib(install):

    def finalize_options(self):
        install.finalize_options(self)
        self.install_lib = self.install_platlib


setup(
    name='cspy',
    version='1.0.0',
    author='Sahand',
    author_email='s.asgharieh.ahari@rug.nl',
    url='https://github.com/saahaand/cspy',
    description='Modified version of cspy by Mat',
    packages=find_packages(),
    package_data={
        'cspy': ['.libs/*', 'algorithms/*'],
    },
    include_package_data=True,
    install_requires=['networkx', 'numpy'],
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: C++',
    ],
)
