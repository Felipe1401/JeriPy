from setuptools import setup, find_packages

setup(
    name='JeriPy',
    packages=["JeriPy"],
    version='0.1.0',
    author='Felipe Gómez',
    author_email='felipenicolasgomezmolina@gmail.com',
    description='JeriPy es una librería que permite la traducción de español a Jerigonzo y de jerigonzo a español.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Felipe1401/JeriPy.git',
    install_requires=[
        "pyphen",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
)