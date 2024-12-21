from setuptools import setup, find_packages

setup(
    name='ecocode',
    version='1.0.0',
    description='A tool for profiling, analyzing, and optimizing the energy impact of software.',
    author='EcoCode Team',
    author_email='support@ecocode.org',
    packages=find_packages(),
    install_requires=[
        'flask',
        'socketio'
    ],
    entry_points={
        'console_scripts': [
            'ecocode=ecocode:main',
        ],
    },
)
