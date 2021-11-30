#!/usr/local/bin/python3

import os
import sys

a = input('please enter the protein family:\n\t')
b = input('please enter the taxonomic group:\n\t')

import subprocess
subprocess.call('chmod 700 project.py',shell = True)

##This section is generated to search for the desired protein and organisms from NCBI database

#A default query sentence of esearch is made, and replace the default word with user input
#default_line = "esearch -db protein -query '99[TITL]'| efilter -query ''66'[ORGN] AND 0:1000[SLEN]'| efetch -format fasta > sequence_required.fasta"
#command_line_1 = default_line.replace('99',a)
#command_line = command_line_1.replace('66',b)

#os.system is used to run esearch command line in py transcipt
#os.system(command_line)

##This section is generated to conduct multiple alignment among desired sequences with clustalo installed in MSc server

#subprocess.call("clustalo -i sequence_required.fasta -o multi_alig.fasta",shell = True)

##This section is generaterd to plot the the level of protein sequence conservation across the species within that taxonomic group

#
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

command_plot = "plotcon -sequence multi_alig.fasta -winsize " + str(win_size) + " -graph " + graph_type 
subprocess.call(command_plot,shell = True)



