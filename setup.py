from setuptools import setup, find_packages
__version__ = '1.2.0'
setup(
    name="sgcharts-stringx",
    version=__version__,
    python_requires='>=3.5.0',
    install_requires=[],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    description='description',
    license='MIT'
)
