from setuptools import setup, find_packages

setup(
    name='document_portal',
    author="Khang Ho Phu",
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'numpy',
        'python-dotenv',
    ])