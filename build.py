import datetime
import re

class Builder(object):
    """
    This class is used to merge the codebase into file m26/__init__.py
    """
    def __init__(self, n=0.0):
        self.value = float(n)
        self.plain_imports = dict()
        self.from_imports = dict()
        self.code_lines = list()
        self.outfile = 'm26/__init__.py'
        self.import_regexp1 = re.compile('^import ')
        self.import_regexp2 = re.compile('^from ')
        self.blank_line_counter = 0

    def build(self):
        for code_file in self.code_files():
            self.merge_file(code_file)

        with open(self.outfile, 'wt') as f:
            for line in self.header_lines():
                f.write("%s\n" % line)
            for key in sorted(self.plain_imports):
                f.write("%s\n" % key)
            if len(self.from_imports) > 0:
                f.write("\n")
            for key in sorted(self.from_imports):
                f.write("%s\n" % key)
            for line in self.code_lines:
                f.write("%s\n" % line)
            f.write("\n\n# generated on {0}\n".format(datetime.datetime.now()))
            print('file written {0}'.format(self.outfile))

    def header_lines(self):
        lines = list()
        lines.append("__author__ = 'cjoakim'")
        lines.append("__version__ = '0.0.6'")
        lines.append("")
        lines.append('"""')
        lines.append("m26 library")
        lines.append('"""')
        lines.append("")
        lines.append("VERSION = __version__")
        lines.append("")
        return lines

    def merge_file(self, code_file):
        print('merging file {0}'.format(code_file))
        with open(code_file, 'rt') as f:
            for line in f:
                self.add_line(line.rstrip(), True)

    def add_line(self, line, filter=False):
        if filter:
            if '__author__' in line:
                return
            if 'from .' in line:
                return
            if self.import_regexp1.match(line):
                self.plain_imports[line] = ''
                return
            if self.import_regexp2.match(line):
                self.from_imports[line] = ''
                return

        if len(line) > 0:
            self.blank_line_counter = 0
            self.code_lines.append(line)
        else:
            self.blank_line_counter += 1
            if self.blank_line_counter < 3:
                self.code_lines.append(line)

    def code_files(self):
        files = list()
        files.append('m26/age.py')
        files.append('m26/age_calculator.py')
        files.append('m26/constants.py')
        files.append('m26/distance.py')
        files.append('m26/elapsed_time.py')
        files.append('m26/run_walk_calculator.py')
        files.append('m26/speed.py')
        return files


if __name__ == "__main__":

    builder = Builder()
    builder.build()
