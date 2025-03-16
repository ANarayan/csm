from setuptools import setup, find_packages

setup(
    name="csm",  # Replace with your actual package name
    version="0.1.0",
    description="Fork of Sesame CSM package",
    url="https://github.com/ANarayan/csm.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "torch==2.4.0",
        "torchaudio==2.4.0",
        "tokenizers==0.21.0",
        "transformers==4.49.0",
        "huggingface_hub==0.28.1",
        "moshi==0.2.2",
        "torchtune==0.4.0",
        "torchao==0.9.0",
    ],
    dependency_links=[
        "git+https://github.com/SesameAILabs/silentcipher@master#egg=silentcipher"
    ],
)
