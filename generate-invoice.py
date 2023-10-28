#!/usr/bin/env python

# Creator: nik gaffney <nik@fo.am>
# Created: 2023-10-23
# Copyright ©️ 2023 FoAM oü
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import os
import shutil

pandoc = "pandoc"
template = "invoice-template.tex"
pdf_engine = "xelatex"

def check_dependencies():
    def check_cmd(cmd):
        if shutil.which(cmd) is None:
            print(f"error: {cmd} is not installed.\n")
            sys.exit()
    check_cmd(pdf_engine)
    check_cmd(pandoc)
    # etc


def process_invoice(file):
    output_file = os.path.splitext(file)[0]
    # assemble command
    pandoc_command = (f"{pandoc} {file} -o {output_file}.pdf \
                      --template={template} --pdf-engine={pdf_engine} --quiet")
    # run it...
    status = os.system(pandoc_command)
    if status==0:
        print(f"successfully generated {output_file}")
    else:
        print(f"error generating {output_file}")


def main():
    check_dependencies()
    if len(sys.argv) == 2:
      input_file = sys.argv[1]
      process_invoice(input_file)
    else:
      print(f"usage: {sys.argv[0]} <filename.yaml>")
      sys.exit()


if __name__ == "__main__":
    main()
