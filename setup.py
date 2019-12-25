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
    url='https://github.com/wangjie-ruc/ConfigParser',
    license='MIT',
    install_requires=install_requires
)
