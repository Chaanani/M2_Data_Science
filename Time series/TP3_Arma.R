
#Question 1)

simulerARMA = function(n, m, Phi, Theta, s2){
  
  # Bruit N(0, s2)
  E = rnorm(n, 0, sqrt(s2))
  
  # Ordres  du processus
  p = length(Phi)
  q = length(Theta)
  r = max(p, q)
  
  # S?rie recentr?e
  Y = rep(0, n)
  
  # Construction pas ? pas de la structure ARMA
  for (i in (r+1):n){
    ar = ifelse(p > 0, sum(Phi*Y[(i-1):(i-p)]), 0)
    ma = ifelse(q > 0, sum(Theta*E[(i-1):(i-q)]), 0)
    Y[i] = ar + ma + E[i]
  }
  
  # La s?rie est centr?e sur m avant renvoi
  Y = Y+m
  
  # Repr?sentation graphique
  plot(1:n, Y, type="l", xlab="Temps", ylab=paste("S?rie ARMA(", substitute(p), ",", substitute(q), ")", sep=""))
  
  return(Y)
}
X = simulerARMA(500, 5, c(0.5), c(), 1)
X2 = simulerARMA(500, 5, c(1), c(), 1)
plot(X, type='l', col='red', main="simulation d'un proicessus  Arma(2,2) vs Arma(2, 1)")
lines(X2, type='l', col='blue')


#Camparision avec arima.sim

ts = arima.sim(list(ar = c(0.5) , ma = c(0.5)), n = 100, sd = sqrt(2) )
plot(X, type='l', col='red', main="simulation d'un proicessus  Arma(2,2) vs Arma(2, 1)")
lines(ts, type='l', col='blue')



#Question 3 les etudes de ACF et PACF

# les graphes ACF

acf_resultat = acf(X)
plot(acf_resultat, main="Graphique de l'ACF  de serie1")





# les graphe PACF
acf_resultat <- pacf(X)
plot(acf_resultat, main="Graphique de l'ACF  de serie1")


#Question 4
# Test de Box

lag = 10
resultat_test <- Box.test(X, lag = lag, type = "Ljung-Box")
print(resultat_test)






#les tests de stationnarité

# Charger la bibliothèque tseries
library(tseries)
dttf <- simulerARMA(100, 5, c(-1), c(0.5), 2)
# Supposons que votre série temporelle est stockée dans un objet appelé serie_temporelle
resultat_adf <- adf.test(dttf)
p_value_adf <- resultat_adf$p.value
print(p_value_adf)
# test kpss
resultat_kpss <- kpss.test(dttf)

# Extraire et afficher la p-value du test KPSS
p_value_kpss <- resultat_kpss$p.value
print(p_value_kpss)

library(stats)
modele_arima <- arima(dttf, order = c(3, 2, 0))
plot(modele_arima, main="Graphique de l'ACF  de serie2")



#######################################
library(TSA)
# Charger le jeu de données "electricity"
data("electricity")
ln_Xt <- log(electricity)

# Décomposer la série
electricity_decomposed <- decompose(ln_Xt)
plot(electricity_decomposed)
