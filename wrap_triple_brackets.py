#!/opt/local/bin/python
import sys
from optparse import OptionParser

def wrap_brackets(in_file):
    f = open(in_file, 'r')
    in_lines = f.readlines()
    f.close()
    for ln in in_lines:
        print ln.replace('<', '[[[<').replace('>', '>]]]'),

def unwrap_brackets(in_file):
    f = open(in_file, 'r')
    in_lines = f.readlines()
    f.close()
    for ln in in_lines:
        print ln.replace('[[[<', '<').replace('>]]]', '>'),

def main():
    ''' adds (or removes) triple square brackets to angle brackets in specified input file
        output goes to stdout 
    '''

    usage = "Usage: ./%prog [-u] -f <filename>"
    parser = OptionParser(usage)
    parser.add_option('-u', '--unwrap', action="store_true", dest="unwrap", default=False,
                      help='set to unwrap triple brackets')
    parser.add_option('-f', '--file', action="store", type="string", dest="filename")
    (options, args) = parser.parse_args()

    if not options.filename:
        parser.error('Filename required')

    if options.unwrap:
        unwrap_brackets(options.filename)
    else:
        wrap_brackets(options.filename)
        

if "__main__" == __name__:
    main()
