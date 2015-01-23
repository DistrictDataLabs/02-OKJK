#Read in BLS txt files
file <- "http://download.bls.gov/pub/time.series/la/la.data.2.AllStatesU"
file2<-"http://download.bls.gov/pub/time.series/la/la.state_region_division"
all_states<-read.delim(file, sep="\t",header=TRUE)
s_r_division<-read.delim(file2,header=TRUE)

#Clean datasets
attach(all_states)
recent<-all_states[which(year==2014 & period=='M11' & substr(series_id,20,20)==3),]
recent$srd_code<-substr(recent$series_id,6,7)
recent$srd_code1<-as.numeric(as.character(recent$srd_code))  
recent_us<-recent[which(recent$srd_code1<60),]

s_r_division$srd_code<-rownames(s_r_division)
s_r_division$srd_code1<-as.numeric(as.character(s_r_division$srd_code)) 
State_def<-s_r_division[which(s_r_division$srd_code1<60),]

#Build output dataset for Tableau
final <- merge(recent_us,State_def,by="srd_code1")
clean_bls<-final[c(-1,-2,-3,-4,-6,-7,-8)]
write.table(clean_bls, "C://Users//Katie//Documents//R//Clean_BLS.txt", sep="\t")
