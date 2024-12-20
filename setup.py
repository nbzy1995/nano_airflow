from setuptools import setup, find_packages

setup(
    name="nano_airflow",
    version="1.0.0",
    description="A lightweight workflow management library",
    author="Yang Zhou",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
