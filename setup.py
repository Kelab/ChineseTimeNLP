from setuptools import setup
import setuptools

setup(
    name="ChineseTimeNLP",
    version="1.1.5",
    keywords=("time", "nlp"),
    author="BuddingLab",
    author_email="lengthmin@gmail.com",
    description="...",
    long_description="...",
    license="MIT Licence",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["regex>=2017", "arrow>=0.15.2"],
    zip_safe=False,
    classifiers=["Programming Language :: Python :: 3.7"],
)
