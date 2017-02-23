from setuptools import setup
import clusterflag



setup(name='cluster-flag',
      version=clusterflag.__version__,
      url='https://github.com/dashee87/cluster-flag',
      author='David Sheehan',
      author_email='davidfsheehan87@gamil.com',
      description='Generate country flags with numpy and pandas',
      keywords='country flag numpy pandas',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Scientific/Engineering :: Visualization'
      ],
      license='MIT',
      packages=['clusterflag'],
      install_requires=[
        'pandas>=0.17.1',
        'numpy>=1.11.0'],
      zip_safe=False)