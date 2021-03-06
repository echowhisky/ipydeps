# vim: expandtab tabstop=4 shiftwidth=4

from setuptools import setup

setup(
    name='ipydeps',
    version='0.4.2',
    author='Bill Allen',
    author_email='photo.allen@gmail.com',
    description='A pip interface wrapper for installing packages from within Jupyter notebooks.',
    license='MIT',
    keywords='pip install setup jupyter notebook dependencies'.split(),
    url='https://github.com/nbgallery/ipydeps',
    download_url='https://github.com/nbgallery/ipydeps/archive/0.4.2.tar.gz',
    packages=['ipydeps'],
    install_requires=['pip', 'setuptools'],
    dependency_links=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
