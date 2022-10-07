import os
import sys

from setuptools import setup

# ensure the current directory is on sys.path so versioneer can be imported
# when pip uses PEP 517/518 build rules.
# https://github.com/python-versioneer/python-versioneer/issues/193
sys.path.append(os.path.dirname(__file__))

import versioneer  # noqa: E402


setup(
    name="snakemake",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Johannes Köster",
    author_email="johannes.koester@tu-dortmund.de",
    description="Snakemake is a workflow management system that aims to reduce the complexity "
    "of creating workflows by providing a fast and comfortable execution environment, "
    "together with a clean and modern specification language in python style. "
    "Snakemake workflows are essentially Python scripts extended by declarative "
    "code to define rules. Rules describe how to create output files from input files.",
    long_description_content_type="text/markdown",
    zip_safe=False,
    license="MIT",
    url="https://snakemake.readthedocs.io",
    project_urls={
        "Source": "https://github.com/snakemake/snakemake",
    },
    packages=[
        "snakemake",
        "snakemake.remote",
        "snakemake.report",
        "snakemake.report.template",
        "snakemake.report.template.components",
        "snakemake.report.data",
        "snakemake.common",
        "snakemake.caching",
        "snakemake.deployment",
        "snakemake.linting",
        "snakemake.executors",
        "snakemake.unit_tests",
        "snakemake.unit_tests.templates",
        "snakemake.template_rendering",
    ],
    entry_points={
        "console_scripts": [
            "snakemake = snakemake:main",
            "snakemake-bash-completion = snakemake:bash_completion",
        ]
    },
    package_data={"": ["*.css", "*.sh", "*.html", "*.jinja2", "*.js", "*.svg"]},
    python_requires=">=3.7",
    install_requires=[
        "wrapt",
        "requests",
        "ratelimiter",
        "pyyaml",
        "configargparse",
        "appdirs",
        "datrie",
        "jsonschema",
        "docutils",
        "gitpython",
        "psutil",
        "nbformat",
        "toposort",
        "connection_pool >=0.0.3",
        "pulp >=2.0",
        "smart_open >=3.0",
        "stopit",
        "tabulate <0.9.0",
        "yte >=1.0,<2.0",
        "jinja2 >=3.0,<4.0",
        "reretry",
    ],
    extras_require={
        "reports": ["jinja2", "pygments"],
        "messaging": ["slacker"],
        "google-cloud": [
            "oauth2client",
            "google-crc32c",
            "google-api-python-client",
            "google-cloud-storage",
        ],
        "pep": [
            "peppy",
            "eido",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
