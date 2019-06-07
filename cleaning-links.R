# Author: Misha Leong
# Date: June 2019
# Project: Insight Data Fellowship Project to classify used book posts as likely to sell
# Specificly: Data wrangling and cleaning


# *************************************************************
# FIRST THINGS FIRST
# *************************************************************

# load libraries
library(tidyverse)

# load files
sold <- read.csv("sold-books.csv")
forsale <- read.csv("forsale-books.csv")
soldHigh <- read.csv("sold-books-high.csv")
forsaleHigh <- read.csv("forsale-books-high.csv")
soldLow <- read.csv("sold-books-low.csv")
forsaleLow <- read.csv("forsale-books-low.csv")

#check they are different from each other
sold
forsale
soldHigh
forsaleHigh
soldLow
forsaleLow

#create list of unique url links for sold vs for sale and append the beginning of the url name.
soldCombine <- sold %>%
  union(soldHigh) %>%
  union(soldLow) %>%
  as.data.frame()
soldCombine

sold_urls <- paste("https://www.mercari.com", soldCombine$link_stub)
write.table(sold_urls, file = "sold_urls.txt", row.names = FALSE)


forsaleCombine <- forsale %>%
  union(forsaleHigh) %>%
  union(forsaleLow)
forsaleCombine

forsale_urls <- paste("https://www.mercari.com", forsaleCombine$link_stub)
write.table(forsale_urls, file = "forsale_urls.txt", row.names = FALSE)

