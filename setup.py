import setuptools

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="alfa",
    author="H Graham",
    author_email="hamish(at)graham.gb.net",
    description="Code to determine a symplectic matrix.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
