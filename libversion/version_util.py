import os

"""
Version utility module for the libversion package.
Provides a VersionUtil class to read the package version from a file.
"""

class VersionUtil:
    """Utility for retrieving the package version."""

    def __init__(self, version_file: str = None):
        """
        Initialize VersionUtil.

        :param version_file: Optional path to a version.txt file. If not provided,
                             defaults to '../version.txt' relative to this file.
        """
        if version_file:
            self._version_file = version_file
        else:
            # determine the default path: one level up from this file
            self._version_file = os.path.abspath(
                os.path.join(os.path.dirname(__file__), os.pardir, 'version.txt')
            )

    def get_version(self) -> str:
        """
        Read and return the version string from the version file.

        :return: Version string, e.g. '1.2.3'
        :raises RuntimeError: If the version file cannot be found or read.
        """
        try:
            with open(self._version_file, 'r') as f:
                return f.read().strip()
        except (IOError, OSError) as e:
            raise RuntimeError(f"Unable to read version file at {self._version_file}: {e}")

    def __str__(self) -> str:
        """
        String representation of this utility returns the version.
        """
        return self.get_version()

