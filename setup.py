from setuptools import setup, find_packages
import io

import versioneer


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        try:
            with io.open(filename, encoding=encoding) as f:
                buf.append(f.read())
        except IOError:
            pass
    return sep.join(buf)


setup(
    name='sql_column_names',
    version=versioneer.get_version(),
    author='Nico',
    author_email=[u'nk@gpredictive.de'],
    license='proprietary',
    packages=find_packages(),
    url='http://www.gpredictive.de/',
    description='Liest SQL Code und erkennt die Spaltennamen',
    long_description=read('README.md', 'CHANGELOG'),
    cmdclass=versioneer.get_cmdclass()
)
