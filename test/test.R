# W205 Project

# Test Data Viz

library(dplyr)
library(data.table)


# for Bernie Sanders
# - read files containing individual contribution, independent expenditure data

# read file header
dt.indivCon = data.table(read.csv(file = 'raw-data/bernie-sanders/indiv_contrib_2016-2y_bernie-sanders.csv',
                           nrows = 7, header = F, col.names = c('key','value'), stringsAsFactors = F))
setkey(dt.indivCon, key)

# save election year, candidate ID, candidate name
year = dt.indivCon['description', value]
cid = dt.indivCon['cmte_id', value]
cname = dt.indivCon['cmte_nm', value]

# read individual contribution data
dt.indivCon = data.table(read.csv(file = 'raw-data/bernie-sanders/indiv_contrib_2016-2y_bernie-sanders.csv',
                         skip = 7, header = T, stringsAsFactors = F))
n = nrow(dt.indivCon)

dt.indivCon[, ':=' (Candidate.Id = as.factor(rep(cid, n)),
                    Candidate.Name = as.factor(rep(cname, n)),
                    Year = as.factor(rep(year, n)))]

summary(dt.indivCon)

# write.csv(file = )

# - transform data
#       - clean special chars
#       - populate can_id column
#       - create views grouping contributions by source, interest, industry, geography
# - write data to Excel workbook so we can blend in Tableau


