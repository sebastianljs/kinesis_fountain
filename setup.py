from setuptools import setup, find_packages


def setup_package():
    setup(
        name="kinesis-fountain",
        version="0.0.1",
        description="A library for AWS kinesis analytics app integration and testing",
        author="Sebastian Lin",
        author_email="sebastianljs@gmail.com",
        keywords="AWS Kinesis",
        license="MIT",
        packages=find_packages(),
        python_requires=">=3.6.*",
        install_requires=["boto3"],
        extra_require={
            "test": ["coverage", "nose"]
        }
    )


def main():
    setup_package()


if __name__ == "__main__":
    main()
