from setuptools import find_packages, setup

setup(name='rate_limited_queue',
      version='0.0.2',
      description='A queue that allows for processing of items within one or more rate-limits.',
      url='https://github.com/jackmaney/rate-limited-queue',
      author='Jack Maney',
      author_email='jackmaney@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
