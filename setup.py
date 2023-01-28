from setuptools import setup

setup(
    name='sortviews',
    version='0.1.0',
    py_modules=['script'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'sortviews=script:format',
        ],
    },
)