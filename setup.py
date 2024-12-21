from setuptools import setup, find_packages

setup(
    name='ecocode',
    version='1.1.0',
    description='A tool for profiling, analyzing, and optimizing the energy impact of software.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='EcoCode Team',
    author_email='support@ecocode.org',
    url='https://github.com/EcoCode/ecocode',
    packages=find_packages(include=['ecocode', 'ecocode.*']),
    install_requires=[
        'flask>=2.2.0',
        'socketio>=5.6.0',
        'pytest>=7.2.0',
        'coverage>=6.5.0',
    ],
    extras_require={
        'dev': ['black>=23.0.0', 'flake8>=5.0.0'],
        'docs': ['sphinx>=5.0.0', 'sphinx_rtd_theme>=1.0.0']
    },
    entry_points={
        'console_scripts': [
            'ecocode=ecocode:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Quality Assurance',
    ],
    python_requires='>=3.8',
    keywords='ecocode energy-efficiency profiling optimization',
    include_package_data=True,
    package_data={
        'ecocode': ['templates/*.html', 'static/*.*'],
    },
    zip_safe=False,
)
