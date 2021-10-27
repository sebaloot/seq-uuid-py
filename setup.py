from distutils.core import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='seq-uuid',
    version='1.0.0',
    packages=['seq_uuid'],
    description='A library to generate sequential uuid based on RFC4122',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sebaloot/seq-uuid-py',
    author='Sebaloot',
    license="MIT",
    keywords=['uuid', 'uuidv6', 'sequential uuid'],
    classifiers=[]
)
