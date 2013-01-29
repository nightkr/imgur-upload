 #!/usr/bin/env python2

from setuptools import setup

setup(name='imgur_upload',
      version='1.0',
      description='CLI for uploading images to imgur',
      license='Public Domain',
      py_modules=['imgur_upload'],
      entry_points={
        'console_scripts': ['imgur-upload = imgur_upload:main']
      },
      install_requires=['requests>=1.1'],
)