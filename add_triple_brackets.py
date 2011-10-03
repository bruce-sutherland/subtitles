import sys
from lxml import etree

def parse(in_file):
	f = open(in_file, 'r')
	xml = etree.parse(f, etree.XMLParser())
	f.close()
	return xml

def output_xml(xml):
	print etree.tostring(xml, encoding='UTF-8', xml_declaration=True)

def insert_brackets(in_file):
	#in_xml = parse(in_file)
	#output_xml(in_xml)
	f = open(in_file, 'r')
	in_lines = f.readlines()
	f.close()
	for ln in in_lines:
		print ln.replace('<', '[[[<').replace('>', '>]]]'),

def main():
	""" adds triple square brackets to angle brackets in specified input file """
	""" output goes to stdout """
	if len(sys.argv) > 1:
		insert_brackets(sys.argv[1])
	else:
		print "No input file specified."

if "__main__" == __name__:
	main()

