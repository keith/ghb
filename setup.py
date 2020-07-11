import setuptools

import ghb

setuptools.setup(
    name="ghb",
    version=ghb.__version__,
    description="A collection of useful GitHub commands",
    license="MIT",
    url="https://github.com/keith/ghb",
    author="Keith Smiley",
    author_email="keithbsmiley@gmail.com",
    install_requires=["requests==2.20.0"],
    packages=["ghb", "ghb.helpers"],
    entry_points={"console_scripts": ["ghb=ghb.__main__:main"]},
    python_requires=">=3.8",
)
