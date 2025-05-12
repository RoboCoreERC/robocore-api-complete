from setuptools import setup, find_packages

setup(
    name="robocore-api",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        # prefer websockets, but fallback will use websocket-client if needed
        "websockets>=10.0",
    ],
    extras_require={
        "jetson": ["websocket-client"],     # for Jetson fallback
        "dev": ["pytest", "pytest-asyncio", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "robocore-cli=robocore_api.cli:main"
        ],
    },
    license="MIT",
    author="RoboCore",
    description="Python API for RoboCore robots (WebSocket)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/robocore-api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Communications :: Telephony",
    ],
)
