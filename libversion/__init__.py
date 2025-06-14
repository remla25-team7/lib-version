from .version_util import VersionUtil

__all__ = ["VersionUtil", "get_version"]

def get_version() -> str:
    #get the version using the VersionUtil classs
    return VersionUtil().get_version()