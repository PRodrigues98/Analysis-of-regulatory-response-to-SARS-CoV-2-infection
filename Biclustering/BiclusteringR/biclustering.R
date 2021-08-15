library(biclust)


# load data
data_names <- list("p01", "p02", "p02-03", "p05", "top200", "top500", "top1000", "top2000", "top5000")
data <- vector("list", length(data_names))

i <- 1
for(name in data_names){
    data[[i]] <- data.matrix(read.table(paste("data-", name, ".csv", sep = ""), row.names = 1, header = TRUE), rownames.force = TRUE)
    i <- i + 1
}



# Plaid
for(i in 1:length(data_names)){
    res <- biclust(data[[i]], method = BCPlaid())
    writeBiclusterResults(paste("results-new-", data_names[[i]], "-plaid.txt", sep = ""), res,"BCPlaid, defaults", dimnames(data[[i]])[1][[1]], dimnames(data[[i]])[2][[1]])
}



# xMotifs
for(i in 1:length(data_names)){
    y <- discretize(data[[i]])
    res <- biclust(y, method = BCXmotifs())
    writeBiclusterResults(paste("results-new-", data_names[[i]], "-xMotifs.txt", sep = ""), res,"xMotifs, defaults", dimnames(y)[1][[1]], dimnames(y)[2][[1]])
}



# Cheng and Church
for(i in 1:length(data_names)){
    y <- data[[i]]
    res <- biclust(y, method = BCCC(), delta = 0.05, alpha = 1, number = 100)
    writeBiclusterResults(paste("results-new-", data_names[[i]], "-chengAndChurch.txt", sep = ""), res,"Cheng and Church, delta = 0.05, alpha = 1, number = 100", dimnames(y)[1][[1]], dimnames(y)[2][[1]])
}

