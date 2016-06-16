from setuptools import setup, find_packages

with open('README.md') as f:
        readme = f.read()

with open('LICENSE') as f:
        license = f.read()

setup(
        name='document-shingles',
        version='0.0.1',
        description='k-shingles for text',
        long_description=readme,
        author='Steven Samson',
        author_email='steven.a.samson@gmail.com',
        url='https://github.com/steven-s/document-shingles',
        license=license,
        packages=find_packages(exclude=('tests'))
)

