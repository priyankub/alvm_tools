from distutils import log
from setuptools.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):

    def __init__(self, *args):
        _build_ext.__init__(self, *args)

    def has_alvm_extensions(self):
        return (
            self.distribution.alvm_extensions
            and len(self.distribution.alvm_extensions) > 0
        )

    def check_extensions_list(self, extensions):
        if extensions:
            _build_ext.check_extensions_list(self, extensions)

    def run(self):
        """Run build_alvm sub command """
        if self.has_alvm_extensions():
            log.info("running build_alvm")
            build_alvm = self.get_finalized_command("build_alvm")
            build_alvm.inplace = self.inplace
            build_alvm.run()

        _build_ext.run(self)
