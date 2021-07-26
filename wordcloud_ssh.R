txt <- read.csv('wordcloud_ssh.csv',header=F,stringsAsFactors = F,fileEncoding = 'cp949')
nouns <- extractNoun(txt)
wordcount <- table(unlist(nouns))
df_word <-as.data.frame(wordcount,stringsAsFactors = F)
df_word <-filter(df_word,nchar(Var1)>1)
top20 <- df_word %>% 
  arrange(desc(Freq)) %>% 
  head(300)


pal<- brewer.pal(8,'Dark2')
set.seed(1234)
wordcloud(word = df_word$Var1,
          freq = df_word$Freq,
          min.Freq = 3,
          random.order = F,
          rot.per =.1,
          scale = c(3,0.1),
          colors =  pal
  
)
