from setuptools import setup, find_packages

setup(
    name='JeriPy',
    packages=find_packages(),
    version='0.1.0',
    author='Felipe Gomez',
    author_email='felipenicolasgomezmolina@gmail.com',
    description='JeriPy es una libreria que permite la traducción de espanol a Jerigonzo y de jerigonzo a espanol.',
    long_description=open('README.md', encoding='utf-8').read(),
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