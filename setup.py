import pathlib

import setuptools

import ghb

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="ghb",
    version=ghb.__version__,
    description="A collection of useful GitHub commands",
    long_description=long_description,
    license="MIT",
    url="https://github.com/keith/ghb",
    author="Keith Smiley",
    author_email="keithbsmiley@gmail.com",
    install_requires=["requests==2.32.4"],
    packages=["ghb", "ghb.helpers"],
    entry_points={"console_scripts": ["ghb=ghb.__main__:main"]},
    python_requires=">=3.8",
)
