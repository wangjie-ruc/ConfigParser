from setuptools import find_packages, setup

install_requires=['astunparse']

setup(
    name='apcs',
    version='0.0.6',
    packages=find_packages(exclude=('test',)),
    author='jie.wang',
    author_email='jie.wang@ruc.edu.cn',
    description='Configuration Toolkit',
    url='https://github.com/wangjie-ruc/apcs',
    license='MIT',
    install_requires=install_requires
)
