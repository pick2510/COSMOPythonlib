from setuptools import setup

setup(name='COSMOPythonLib',
      version='0.2',
      description='COSMO Python Utilities',
      url='http://github.com/pick250/COSMOPythonLib',
      author='Dominik Strebel',
      author_email='dominik.strebel@empa.ch',
      license='MIT',
      packages=['COSMOPythonLib','COSMOPythonLib.proj'],
      install_requires=['numpy>0.8','netCDF4>1.0.0','pandas>0.15','scipy>0.12'],
      zip_safe=False)
