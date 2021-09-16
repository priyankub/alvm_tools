# alvm_tools setuptools integration

from distutils import log
from distutils.dep_util import newer

import os
import pathlib

from ir import reader
from alvm_tools import binutils
from stages import stage_2


def compile_alvm_text(text, search_paths):
    ir_src = reader.read_ir(text)
    assembled_sexp = binutils.assemble_from_ir(ir_src)

    input_sexp = assembled_sexp.to((assembled_sexp, []))
    run_program = stage_2.run_program_for_search_paths(search_paths)
    cost, result = run_program(stage_2.run, input_sexp)
    return result


def compile_alvm(input_path, output_path, search_paths=[]):
    if newer(input_path, output_path):
        log.info("alvmcc %s -o %s" % (input_path, output_path))
        with open(input_path) as f:
            text = f.read()
        result = compile_alvm_text(text, search_paths)
        hex = result.as_bin().hex()

        with open(output_path, "w") as f:
            f.write(hex)
            f.write("\n")
    else:
        log.info("skipping %s, compiled recently" % input_path)

    return output_path


def find_files(path=""):
    r = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".alvm"):
                full_path = pathlib.Path(dirpath, filename)
                target = "%s.hex" % path
                compile_alvm(full_path, target)
                r.append(target)
    return r
