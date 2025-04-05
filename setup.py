from setuptools import setup, find_packages

setup(
    name="webchameleon",
    version="1.3.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
        "networkx>=2.5",
        "playwright>=1.30.0",
        "aiohttp>=3.8.0",
        "aiolimiter>=1.0.0",
        "cachetools>=5.0.0",
        "aiohttp-retry>=2.8.0",
        "nltk>=3.6.5",
        "python-louvain>=0.16",
        "faker>=18.0.0",
        "matplotlib>=3.5.0",
        "numpy>=1.21.0",
        "brotli>=1.1.0",
    ],
    author="Your Name",
    description="Advanced web scraping and API reversal tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/webchameleon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
