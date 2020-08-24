from setuptools import setup
from setuptools import find_packages

setup(name='pyavtech',
      version='0.0.0',
      
      description='AVTECH Device driver',
      long_description=open('README.md').read(),
      
      classifiers=[
        'License :: OSI Approved ::  Massachusetts Institute of Technology (MIT)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Device driver',
        'Intended Audience :: Developers',
      ],
      
      keywords='avtech',
      
      url='https://git.ul-ts.com/ims-se/hardware-team/pybench/pyavtech',
      author='Laurent Bonnet',
      author_email='laurent.bonnet@ul.com',
      python_requires='>=3.6',
      license='MIT',
      packages=find_packages(),
      install_requires=['PyVISA'],
      zip_safe=True)
