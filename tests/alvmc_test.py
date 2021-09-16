"""
These tests check that the `alvmc` utility methods
continue to work with the `include` keyword, and produce
the expected output. It's not intended to be a complete
test of the compiler, just the `alvmc` api.
"""

from tempfile import TemporaryDirectory

from alvm_tools import alvmc


INCLUDE_CODE = "((defconstant FOO 6001))"
MAIN_CODE = """(mod (VALUE) (include "include.alvm") (+ VALUE FOO))"""
EXPECTED_HEX_OUTPUT = "ff10ff02ffff0182177180"

# `EXPECTED_HEX_OUTPUT` disassembles to "(+ 2 (q . 6001))"


def test_compile_alvm_text():
    with TemporaryDirectory() as include_dir:
        include_path = f"{include_dir}/include.alvm"
        with open(include_path, "w") as f:
            f.write(INCLUDE_CODE)
        output = alvmc.compile_alvm_text(MAIN_CODE, search_paths=[include_dir])
        assert repr(output) == f"SExp({EXPECTED_HEX_OUTPUT})"


def test_compile_alvm():
    with TemporaryDirectory() as include_dir:
        with TemporaryDirectory() as source_dir:
            with open(f"{include_dir}/include.alvm", "w") as f:
                f.write(INCLUDE_CODE)
            main_path = f"{source_dir}/main.alvm"
            main_output = f"{source_dir}/main.hex"
            with open(main_path, "w") as f:
                f.write(MAIN_CODE)
            output = alvmc.compile_alvm(
                main_path, main_output, search_paths=[include_dir]
            )
            t = open(output).read()
            assert t == f"{EXPECTED_HEX_OUTPUT}\n"
