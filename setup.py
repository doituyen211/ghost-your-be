from setuptools import setup, find_packages

setup(
    name="ghost-your-be",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "faker>=18.0",
        "pydantic>=2.0",
        "pyyaml>=6.0",
        "sqlalchemy>=2.0",
        "pymongo>=4.0",
        "fastapi>=0.100",
        "uvicorn>=0.20",
        "deepdiff>=6.0",
        "rich>=13.0",
        "requests>=2.28",
    ],
    entry_points={
        "console_scripts": [
            "ghost-your-be =  ghost_your_be.cli:cli",
        ],
    },
    author="Doi Trong Tuyen",
    author_email="tuyensvip@gmail.com",
    description="Công cụ CLI tạo dữ liệu giả, mock API và so sánh API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/doituyen211/ghost-your-be",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)