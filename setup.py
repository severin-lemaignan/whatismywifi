from setuptools import setup

setup(
    name="whatismywifi",
    version="0.1.0",
    description="Summarize Wi-Fi adapter capabilities and the active link, parsing `iw` output.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Claude (Opus 4.7)",
    license="Public Domain",
    url="https://github.com/severin/whatismywifi",
    scripts=["whatismywifi"],
    python_requires=">=3.7",
    classifiers=[
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Networking",
        "Environment :: Console",
    ],
)
