from importlib.metadata import version, PackageNotFoundError

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            return version("lib-version")
        except PackageNotFoundError:
            return "Package not found"