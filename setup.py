from setuptools import setup
setup(
    name = 'pythonLogger',
    version = '0.1.0',
    packages = ['pythonLogger'],
    entry_points = {
        'console_scripts': [
            'pythonLogger = pythonLogger.__main__:main'
        ]
    })