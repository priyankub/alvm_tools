from distutils.cmd import Command
from distutils import log

from setuptools.dist import Distribution

from alvm_tools.alvmc import compile_alvm


Distribution.alvm_extensions = ()


class build_alvm(Command):
    """ Command for building alvm """

    description = "build alvm extensions"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        file_list = self.distribution.alvm_extensions
        for _ in file_list:
            log.info("build_alvm on %s" % _)
            target = "%s.hex" % _
            compile_alvm(_, target)
