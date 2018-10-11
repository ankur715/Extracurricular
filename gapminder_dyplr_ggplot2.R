install.packages("gapminder")
# only have to install them once
library(gapminder)
# need to call to use
data("gapminder")
# dataset of country, continent, year, lifeExp, pop, gdpPercap

summary(gapminder)
# Min, 1st Qu, Median, Mean, 3rd Qu, Max
x <- mean(gapminder$pop)
# select variable in gapminder dataset
x
# call object x which is assigned the mean 

attach(gapminder)
# to avoid typing gapminder$ to refer to variable
median(pop)
hist(lifeExp)
# histogram of lifeExp (fyi: 70-75 most frequent)
hist(pop)
# right-skewed/positive-skewed graph
# median on left side, mean on right side
hist(log(pop))
# mean and median around middle
boxplot(lifeExp ~ continent)
plot(lifeExp ~ gdpPercap)
# non-linear graph gdpPercap axis
plot(lifeExp ~ log(gdpPercap))


install.packages("dyplr")
library(dyplr)
# use pipe-operator %>% as "and then" to improve readability   

gapminder >%>
  select(country,lifeExp) >%>
  filter(country == "Canada" |
           country == "United States") >%> 
  group_by(country) >%>
  summarize(Average_life = mean(lifeExp))

# test the difference in lifeEXp
# null hypothesis: no difference
df1 <- gapminder >%>
  select(country,lifeExp) >%>
  filter(country == "Canada" |
           country == "United States") >%>
  
t.test(data = df1, lifeExp ~ country)
# compare average lifeExp between the two countries
# if statistically different, the p-value will close to 0
# reject null hypothesis of no difference
# 95 percent confidence interval shows 95% certainty of true difference


install.packages("ggplot2")
# data vizualizations
library(ggplot2)

gapminder >%>
  filter(gdpPercap < 50000) >%>
  ggplot2(aes(x=log(gdpPercap), y=lifeExp, col=year))+
  geom_point(alpha=0.3)+
  geom_smooth(method = lm)+
  facet_wrap(~continent)
# aes function is aesthetic for how the variables will be represented
# change color according to continents first 
# make points more transparent with alpha smaller
# log of gdpPercap to make linear
# geom_smooth tracks the continents with a line  
# divide continents into seperate facets 
# since continents are seperated into facets, change color by year


lm(lifeExp ~ gdpPercap)
# gives us y-intercept and slope
summary(lm(lifeExp ~ gdpPercap))
# residuals, coefficients, significance
summary(lm(lifeExp ~ gdpPercap+pop))
# multivariate analysis
