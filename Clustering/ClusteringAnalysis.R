source("dataLibrary.R")


# Load data
gene_data <- read.csv("data/GSE147507_RawReadCounts_Human.tsv", row.names = 1, sep = "\t") # 


log_data <- log(gene_data + 1)
log_data <- as.data.frame(t(log_data))



