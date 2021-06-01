from setuptools import setup
from setuptools import find_packages
from sphinx.setup_command import BuildDoc
from os import path

name = 'pyavtech'
version = '0.1.0'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='name',
      version=version,
      
      cmdclass={'build_sphinx': BuildDoc},
      command_options={
          'build_sphinx': {
              'project': ('setup.py', name),
              'version': ('setup.py', version),
              'source_dir': ('setup.py', 'docs/source')
          }
      },
      description='AVTECH Device driver',
      
      long_description=long_description,
      long_description_content_type='text/markdown',
      
      classifiers=[
        'License :: OSI Approved ::  Massachusetts Institute of Technology (MIT)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Device driver',
        'Intended Audience :: Developers',
      ],

      entry_points={
          'console_scripts': ['avtech_info = bin.avr_info:main'],
      },

      keywords='avtech',
      
      url='https://git.ul-ts.com/ims-se/hardware-team/pybench/pyavtech',
      author='Laurent Bonnet',
      author_email='laurent.bonnet@ul.com',
      python_requires='>=3.6',
      license='MIT',
      packages=find_packages(),
      install_requires=['PyVISA>=1.11.3'],
      zip_safe=False)
