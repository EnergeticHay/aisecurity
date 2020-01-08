# Installation of `aisecurity`

## Prerequisites

1. Python >= 3.5

2. `wget` must be installed, preferably using `brew` (install `brew` with `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`). `wget` can be installed using `brew install wget` and is pre-installed on Linux systems.

3. For GPU usage, `CUDA>=9.0` and the appropriate version of `CuDNN` must be installed.

4. `mysql-connector-python`, `pymysql`, and MySQL Community Server must be downloaded (see https://dev.mysql.com/downloads/mysql/) in order to use MySQL logging functions.

5. `tensorflow>=1.12, <2.0` must also be installed. It's not included in the requirements because of platform-specific version requirements. For the `keras` version of this project, `keras>=2` should also be installed.

## Installation

Note that TensorFlow 2.0 is not yet supported, as `mtcnn` is not compatible with it.

Current version: `python3 -m pip install "git+https://github.com/orangese/aisecurity.git@v0.9a"`

Keras version: `python3 -m pip install "git+https://github.com/orangese/aisecurity.git@keras"`

TF-TRT version: `python3 -m pip install "git+https://github.com/orangese/aisecurity.git@tf-trt"`

Pure TensorRT version [__broken__]: `python3 -m pip install "git+https://github.com/orangese/aisecurity.git@tensorrt"`

After installing, you might want to change the key location settings in `~/.aisecurity/config.json`, which is installed with the `aisecurity` package.

## Upgrade

Keras version: `python3 -m pip install --upgrade "git+https://github.com/orangese/aisecurity.git@keras"`

TF-TRT version: `python3 -m pip install --upgrade "git+https://github.com/orangese/aisecurity.git@tf-trt"`

Pure TensorRT version [__broken__]: `python3 -m pip install --upgrade "git+https://github.com/orangese/aisecurity.git@tensorrt"`

## FaceNet weight files

All weight files (.h5 and .pb models) are available in this [Dropbox folder](https://www.dropbox.com/sh/k9ci2nphj7i7dde/AACaQuxUJ6GoPHFxW6FtJlZca?dl=0). Please cite this repository if using them.

