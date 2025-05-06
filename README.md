# lib_version

`lib_version` is a Python library designed to manage and retrieve software versions. This is useful for including verbose system information in debugging, logs and ensuring compatibility in dependent systems.

### Description

This package implements a simple mechanism to retrieve and display the version of the library itself. This is useful for verification purposes and dependency management.

### Installation

Install the package from GitHub using `pip`:

```bash
pip install git+https://github.com/remla25-team7/lib-version.git@v<version>
```

Replace `<version>`\_` with your version number (e.g., 1.0.0).

### Usage

After installation, you can check if the package is working properly by running this command in the terminal. 

```bash
python -c "from lib_version import print_version; print_version()"
```

Running this command prints the installed version to the console. Verify that it matches the `<version>` you chose earlier.


## License
Distributed under the MIT License.
