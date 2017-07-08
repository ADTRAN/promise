from setuptools import setup


def build_version():
    try:
        with open('promise/BUILD_VERSION') as f:
            return f.read().strip()
    except IOError:
        return '0.dev0'

setup(
    name='promise',
    version='1.0.2b'+build_version(),
    description='Promises/A+ implementation for Python',
    long_description=open('README.rst').read(),
    url='https://github.com/syrusakbary/promise',
    download_url='https://github.com/syrusakbary/promise/releases',
    author='Syrus Akbary',
    author_email='me@syrusakbary.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
    ],

    keywords='concurrent future deferred promise',
    packages=["promise"],
    package_data={"promise": ["BUILD_VERSION"]},
    install_requires=[
        'typing', 'six'
    ],
    tests_require=['pytest>=2.7.3', 'futures'],
)
