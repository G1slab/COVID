library(devtools)
library(tidyverse)
library(corrplot)
library(RColorBrewer)

#at first, should've made coefficient dataframe using python (calculated data frame)
x<-read.csv('input_calculated.csv')
x <- as.data.frame(x) 

x %>% dim()
x %>% unique() %>% dim()

colnames(x)
rownames(x)

#change columnanmes
m_x <- x %>% as.data.frame() %>% rownames_to_column('index') %>% select(-index) %>% column_to_rownames('X')



M <- cor(m_x)
corrplot(M, method="number")


corrplot(M, type="upper", order="hclust",
         col=brewer.pal(n=11, name="RdYlBu"))
