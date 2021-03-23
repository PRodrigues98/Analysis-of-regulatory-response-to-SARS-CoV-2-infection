
library(hash)


preprocess_log <- function(d) {
    log_data <- log(d + 1)
    return(as.data.frame(t(log_data)))
}


dataLibrary_preprocessing_options <- hash()
dataLibrary_preprocessing_options[["log"]] <- preprocess_log

preprocess <- function(f, d) {
    return(dataLibrary_preprocessing_options[f](d))
}