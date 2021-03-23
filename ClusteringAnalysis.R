source("dataLibrary.R")


# Load data
gene_data <- read.csv("data/GSE147507_RawReadCounts_Human.tsv", row.names = 1, sep = "\t") # 


log_data <- log(gene_data + 1)
log_data <- as.data.frame(t(log_data))


dgList <- edgeR::DGEList(counts = gene_data, genes = rownames(gene_data))

countsPerMillion <- edgeR::cpm(dgList)
summary(countsPerMillion)


countCheck <- countsPerMillion > 1
head(countCheck)
keep <- which(rowSums(countCheck) >= 2)
dgList <- dgList[keep,]
summary(edgeR::cpm(dgList)) #compare this to the original summary


dgList <- edgeR::calcNormFactors(dgList, method="TMM")


limma::plotMDS(dgList)
