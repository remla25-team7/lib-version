from .version_util import VersionUtil

__all__ = ["VersionUtil", "get_version"]

def get_version() -> str:
    return VersionUtil().get_version()
