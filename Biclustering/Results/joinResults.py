
# There are 2 types of files, bicPAM and the others

# For bicPAM:
#     Starts with FOUND BICS:#<bics>
#     Followed by <bics> lines of bicluster info:
#    
#     I=[<type of bicluster>] (<number of columns>,<number of genes>) Y=[<column names>] X=[<gene names (mostly empty)>] pvalue=<pvalue>
#
#     Then we have the actual list of biclusters, set in tables with the first row containing the same information as above and the remaining
#     rows each starting with the gene name

