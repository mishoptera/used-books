# Author: Misha Leong
# Date: June 2019
# Project: Insight Data Fellowship Project to classify used book posts as likely to sell
# Specificly: Data wrangling and cleaning


# *************************************************************
# FIRST THINGS FIRST
# *************************************************************

# load libraries
library(tidyverse)


books <- read.csv('used-book-data.csv')
nrow(books)
unique_books <- unique(books)
nrow(unique_books)



#check they are different from each other


#create list that combines everything
books <- sold_data %>%
  union(soldlow_data) %>%
  union(soldhigh_data) %>%
  union(soldmatch_data) %>%
  union(soldliked_data) %>%
  union(forsale_data) %>%
  union(forsalelow_data) %>%
  union(forsalehigh_data) %>%
  union(forsalematch_data) %>%
  union(forsaleliked_data) 
nrow(books)

# NEED TO GET RID OF $, COMMAS, and MAKE NUMERIC
books$price = gsub("\\$", "", books$price)
sum(is.na(books$price))
books$price = as.numeric(gsub("\\,", "", books$price)) 
sum(is.na(books$price))
books$price = as.numeric(books$price)
books[c(203:210),]

# CONVERT POSTED TO DATES
books$posted <- as.Date(books$posted, "%m/%d/%Y")


# *************************************************************
# NOW TIME TO EXPLORE WITH AND PLOT!
# **********************************************************
qplot(x = posted, y = price, color = sold, data = books, geom = "point")

books %>% group_by(sold) %>% tally()
