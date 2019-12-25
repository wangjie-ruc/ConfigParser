from setuptools import find_packages, setup

install_requires=[
    'addict',
    'yaml'
    ]

setup(
    name='ConfigParser',
    version='0.0.1',
    packages=find_packages(exclude=('test',)),
    author='jie.wang',
    author_email='jie.wang@ruc.edu.cn',
    description='Configuration Toolkit',
    url='https://git.vistel.cn/jie.wang/configparser',
    license='BSD',
    install_requires=install_requires
)
