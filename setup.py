from setuptools import setup, find_packages

setup(
    name='blandai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='LanKabelGezogen',
    author_email='cybertom1234@gmail.com',
    description='A Python wrapper for the Bland.ai API',
    license='MIT', 
    keywords='blandai API wrapper',
    url='https://github.com/lankabelgezogen/blandailibrary'
)
