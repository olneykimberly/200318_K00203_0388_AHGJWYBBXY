###############################################################################
# Author: Kimberly Olney
# Date: 2020-11-10
###############################################################################

# imports
import fileinput
import sys
import re
from optparse import  OptionParser

USAGE = """
python2 makeConfig.py --samples <samples.txt> --out <outConfig>

samples == List of samples to make commands for, one per line
out == Output file stem name

get PU ids from fastq files
$ head -n1 -q *.fastq 
"""
parser = OptionParser(USAGE)
parser.add_option('--samples',dest='samples', help = 'List of bam files to make commands for, one per line')
parser.add_option('--out',dest='out', help = 'Output file stem name (e.g. ancientY)')

(options, args) = parser.parse_args()

parser = OptionParser(USAGE)
if options.samples is None:
	parser.error('sample list name not given')
if options.out is None:
	parser.error('Output file stem name not given')

bamList = options.samples

CmdOutfile = options.out + '.json' #Write out the shell script
CmdOutFile = open(CmdOutfile, 'w')

CommandsToWrite = []
inFile = open(bamList ,'r') # reading bam list, bamList is what you specified in '--samples' flag

for line in inFile:
    line = line.rstrip()
    line = line.split('\t')
    sn = line[0]
    CommandsToWrite.append(sn)
inFile.close()

for sn in CommandsToWrite: # each line in your bam file list (so each file name)
	cmd_echo = '\t'+'"'+ sn + '":{'+'\n'
	CmdOutFile.write(cmd_echo)
	cmd_path = '\t'+'\t'+'"bam_path"'+': "/research/labs/neurology/fryer/m239830/200318_K00203_0388_AHGJWYBBXY/200318_K00203_0388_AHGJWYBBXY/BAM/",'+'\n'
	CmdOutFile.write(cmd_path)
	cmd_BAM = '\t'+'\t'+'"BAM": "'+ sn +'.bam",'+'\n'
	CmdOutFile.write(cmd_BAM)


	cmd_ID = '\t'+'\t'+'"ID": "'+ sn +'",'+'\n'
	CmdOutFile.write(cmd_ID)
	cmd_SM = '\t'+'\t'+'"SM": "'+ sn +'",'+'\n'
	CmdOutFile.write(cmd_SM)
	cmd_LB = '\t'+'\t'+'"LB": "'+ sn +'",'+'\n'
	CmdOutFile.write(cmd_LB)
	cmd_PU = '\t'+'\t'+'"PU": "'+ sn +'",'+'\n'
	CmdOutFile.write(cmd_PU)
	cmd_PL = '\t'+'\t'+'"PL": "Illumina"'+'\n'+'\t'+'},'+'\n'+'\n'
	CmdOutFile.write(cmd_PL)
	
#date_end = '\n#-------------------------- \n# 4. end timer \n#-------------------------- \ndate'
#CmdOutFile.write('%s' % (date_end))
CmdOutFile.close()

