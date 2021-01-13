# default to setuptools so that 'setup.py develop' is available,
# but fall back to standard modules that do the same

from setuptools import setup, find_packages

setup(
    name="temp",
    version="0.1.1",
    description="A Library For MaixPy Example",
    author="Juwan",
    author_email="juwan@sipeed.com",
    license="BSD",
    url="https://github.com/sipeed/MaixPy3-Pack",
    packages=find_packages(),
    install_requires=["Pillow"],
    tests_requires=["pytest", "scripttest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
    ],
)
