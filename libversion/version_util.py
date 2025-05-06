import os
class VersionUtil:

    @staticmethod
    def get_version():
        path = os.path.join(os.path.dirname(__file__), "..", "version.txt")
        with open(path) as f:
            return f.read().strip()
