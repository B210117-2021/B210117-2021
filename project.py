#!/usr/local/bin/python3

import os
import sys

a = input('please enter the protein family:\n\t')
b = input('please enter the taxonomic group:\n\t')

import subprocess
subprocess.call('chmod 700 project.py',shell = True)

#######################################################################################################################
##This section is generated to search for the desired protein and organisms from NCBI database

#A default query sentence of esearch is made, and replace the default word with user input
#default_line = "esearch -db protein -query '99[TITL]'| efilter -query ''66'[ORGN] AND 0:1000[SLEN]'| efetch -format fasta > sequence_required.fasta"
#command_line_1 = default_line.replace('99',a)
#command_line = command_line_1.replace('66',b)

#os.system is used to run esearch command line in py transcipt
#os.system(command_line)

#######################################################################################################################
##This section of code is generated a report about what species are shown dataset

subprocess.call("grep -E '>' sequence_required.fasta | cat >> data_review.txt",shell = True)
print("A report of dataset is generated and based on the report, a general result is shown below")
all_species_data = []

import re
for i in open("data_review.txt"):
    
    species = re.findall("\[(.*?)\]",i,re.I|re.M)
    all_species_data = all_species_data + species
     
    
species_dic = list(set(all_species_data))

#List all the species
for i in species_dic:
    print(i,"\n")

#######################################################################################################################
##Ask users if they want to continue the program

decision = input("Please make a decision if you want to continue the program [y/n]:\n\t") 

if decision == 'n':
    print("Good luck!")
    sys.exit()
else:
    print("Let's continue...Next step is plotting the the level of protein sequence conservation across the species")


#######################################################################################################################
##This section aims at transform multi-line of a sequence becomes a single-line.

fr=open('sequence_required.fasta', 'r')  #read files
fw=open('sigle_line_sequence.fasta', 'w')  #write files
seq={}
for line in fr:
    line = line.strip()
    if line.startswith('>'):    #判断字符串是否以‘>开始’
        name=line.split()[0]    #以空格为分隔符。
        seq[name]=''
    else:
        seq[name]+=line.replace('\n', '')
fr.close()

for i in seq.keys():
    fw.write(i)
    fw.write('\n')
    fw.write(seq[i])
    fw.write('\n')
fr.close()

#######################################################################################################################
##This section is generated to conduct multiple alignment among desired sequences with clustalo installed in MSc server

#subprocess.call("clustalo -i sequence_required.fasta -o multi_alig.fasta",shell = True)

##This section is generaterd to plot the the level of protein sequence conservation across the species within that taxonomic group

#Code designed to avoid users typing in inapproperiate values
while True:
    win_size = input("Please input a window size (note:Number of columns to average alignment quality over. The larger this value is, the smoother the plot will be. (Any integer value))\n\t")
    try:
        if_int = int(win_size)
        if isinstance(if_int,int): 
            break               
    except ValueError:
        print("*Man, learn to enter a integer*")
        continue

graph_type = "ps, hpgl, hp7470, hp7580, meta, cps, x11, tek, tekt, none, data, xterm, svg"
graph_type_list = graph_type.split(', ')
while True:
    graph_type = input("Please type in  an output graph type you want (Options: ps, hpgl, hp7470, hp7580, meta, cps, x11, tek, tekt, none, data, xterm, svg)\n\t")
    
    if (graph_type in graph_type_list):
        break
    else:
        print("*Please type in the right graph type*")
        continue 

plot_command = "plotcon -sequence multi_alig.fasta -winsize " + str(win_size) + " -graph " + graph_type 
subprocess.call(plot_command,shell = True)

#######################################################################################################################
##This section scan protein a protein sequence with motifs from the PROSITE database

lines_counts  = subprocess.call("wc -l data_review.txt",shell = True) 

#for i in lines_counts:
    
writefile_command = "patmatmotifs -sequence single_line_sequence.fasta -outfile prosite.patmatmotifs "
subprocess.call(writefile_command,shell = True)












