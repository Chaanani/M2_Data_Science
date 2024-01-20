
# Charger le fichier "functions.R"
source("TP4_Diagnostic.R")



USD <- read.csv("C:\\Users\\msi\\Desktop\\M2_Data_Science\\Time series\\BTC-USD.csv", sep = ",")
plot(USD$Close,  type= 'l', main= "action Btc" , ylab= "Close" , xlab= "Jours" )


lclose= log(USD$Close)
plot(lclose,  type= 'l', main= "action Btc" , ylab= "lclose" , xlab= "Jours" )
grid()

#tendance constante: ARIMA(...., include.mean=True) ARIMA forcast
#tendance lineaire: ARIMA(...., include.mean=True) 

# Les tests pour tester la stationnarité d'un serie

# la supperisson de tendance par la régresion 

time = 1:length(lclose)
lm_model = lm(lclose ~ time)
trend = predict(lm_model)
llclose = lclose - trend
plot(lclose,  type= 'l', main= "action Btc" , ylab= "lclose" , xlab= "Jours" )
grid()
checkupRes(llclose)
# d'aores PACF implique AR(1)
# la suppresisson de tendance par la ARIMA

library(tseries)
library(forecast)

adf.test(llclose)
kpss.test(llclose)
arima_model = Arima(llclose, order=c(1, 0 , 0), include.drift = FALSE, include.mean= FALSE)
summary(arima_model)
ResARMA=arima_model$residuals

checkupRes(ResARMA)

Mod=fitted(Reglio)+fitted(ARMA)

plot(lclose, type="l", main="Action BTC", ylab ="Log vjfj", Xlab="hhf")

lines(Mod, col="red", lty=2)










