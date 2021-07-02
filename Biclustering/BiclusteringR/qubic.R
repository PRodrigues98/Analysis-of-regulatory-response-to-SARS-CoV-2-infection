library("QUBIC")
library("QUBICdata")
library(biclust)

#data <- data.matrix(read.table('GSE147507_RawReadCounts_Human.tsv', sep = '\t', row.names = 1, header = TRUE), rownames.force = TRUE)

data <- data.matrix(read.table('data-p01.csv', row.names = 1, header = TRUE), rownames.force = TRUE)

res <- biclust(data, method = BCQU(), r = 1, q = 0.06, c = 0.95, o = 100,
                        f = 0.25, k = max(ncol(data)%/%20, 2))
writeBiclusterResults("results-stuff.txt", res,"Cheng and Church, delta = 0.05, alpha = 1, number = 100", dimnames(data)[1][[1]], dimnames(data)[2][[1]])
