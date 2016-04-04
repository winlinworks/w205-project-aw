# W205 Project - Visualization of Campaign Contributions

library(dplyr)
library(data.table)

parseAmount = function(x) as.numeric(gsub('$', '', gsub(',', '', x, fixed = T), fixed = T))

####################################
###   INDIVIDUAL CONTRIBUTIONS   ###
####################################

# read file header
dt.ic = data.table(read.csv(file = 'raw-data/indiv_contrib_2016-2y_bernie-sanders.csv',
                            nrows = 7, header = F, col.names = c('key','value'), stringsAsFactors = F))
setkey(dt.ic, key) # set key, values

# read election year, candidate ID from header
year = dt.ic['description', value]
cid = dt.ic['cmte_id', value]




class.ic = rep('character', 17)

# read individual contribution data
dt.ic = data.table(read.csv(file = 'raw-data/indiv_contrib_2016-2y_bernie-sanders.csv',
                            skip = 7, header = T, stringsAsFactors = F, colClasses = class.ic))
nr = nrow(dt.ic) # count # of rows to replicate values for new fields

date.fmt = '%m/%d/%Y' # date format

# recast dates and amounts
# add fields for candidate ID, election year
dt.ic[, ':=' (Zip = substr(Zip, 1, 5),
              Receipt.Date = as.Date(Receipt.Date, date.fmt),
              Amount = parseAmount(Amount),
              Candidate.Id = rep(cid, nr),
              Election.Year = as.integer(rep(year, nr))
              )]
summary(dt.ic)

# write result to CSV
write.table(dt.ic, file = 'mod-data/indiv-contrib-2016-bernie-sanders.csv', sep = ',')



####################################
###   INDEPENDENT EXPENDITURES   ###
####################################

class.ie = rep('character', 22)

# read individual expenditure data
dt.ie = data.table(read.csv(file = 'raw-data/indep_expend_2016-2y_bernie-sanders.csv',
                            header = T, stringsAsFactors = F, colClasses = class.ie))

# recast dates and amounts
dt.ie[ , ':=' (exp_amo = parseAmount(exp_amo),
               exp_dat = as.Date(exp_dat, date.fmt),
               agg_amo = parseAmount(agg_amo),
               rec_dat = as.Date(exp_dat, date.fmt))]

write.table(dt.ie, file = 'mod-data/indep-expend-2016-bernie-sanders.csv', sep = ',')


###############################################
###   CONTRIBUTIONS FROM OTHER COMMITTEES   ###
###############################################

# read file header
dt.oc = data.table(read.csv(file = 'raw-data/other_comm_contrib_2016-2y_bernie-sanders.csv',
                            nrows = 7, header = F, col.names = c('key','value'), stringsAsFactors = F))
# print(dt.cc)
setkey(dt.oc, key) # set key, values

# read election year, candidate ID from header
year = substr(dt.oc['description', value], 1, 4)
cid = dt.oc['cand_id', value]

class.oc = rep('character', 15)

# read other committee contribution data
dt.oc = data.table(read.csv(file = 'raw-data/other_comm_contrib_2016-2y_bernie-sanders.csv',
                            skip = 7, header = T, stringsAsFactors = F, colClasses = class.oc))

nr = nrow(dt.oc) # count # of rows to replicate values for new fields

# recast dates and amounts
# add fields for candidate ID, election year
dt.oc[ , ':=' (Zip = substr(Zip, 1, 5),
               Receipt.Date = as.Date(Receipt.Date, date.fmt),
               Amount = parseAmount(Amount),
               Candidate.Id = rep(cid, nr),
               Election.Year = as.integer(rep(year, nr))
               )][ , X := NULL]
summary(dt.oc)

write.table(dt.oc, file = 'mod-data/other-comm-contrib-2016-bernie-sanders.csv', sep = ',')


################################################
###   TRANSFERS FROM AUTHORIZED COMMITTEES   ###
################################################

# read file header
dt.ac = data.table(read.csv(file = 'raw-data/transfers_auth_comm_2016-2y_bernie-sanders.csv',
                            nrows = 7, header = F, col.names = c('key','value'), stringsAsFactors = F))
# print(dt.ac)
setkey(dt.ac, key)

# read election year, candidate ID from header
year = substr(dt.ac['description', value], 1, 4)
cid = dt.ac['cand_id', value]

class.ac = rep('character', 15)

# read authorized committee transfer data
dt.ac = data.table(read.csv(file = 'raw-data/transfers_auth_comm_2016-2y_bernie-sanders.csv',
                            skip = 7, header = T, stringsAsFactors = F, colClasses = class.ac))

nr = nrow(dt.ac) # count # of rows to replicate values for new fields
# recast dates and amounts
# add fields for candidate ID, election year
dt.ac[ , ':=' (Zip = substr(Zip, 1, 5),
               Receipt.Date = as.Date(Receipt.Date, date.fmt),
               Amount = parseAmount(Amount),
               Candidate.Id = rep(cid, nr),
               Election.Year = as.integer(rep(year, nr))
               )][ , X := NULL]
summary(dt.ac)

write.table(dt.ac, file = 'mod-data/auth-comm-trans-2016-bernie-sanders.csv', sep = ',')