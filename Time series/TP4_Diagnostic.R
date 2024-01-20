layout(c(1,1,1,2:7), nrow= 3, ncol=3, byrow=TRUE) 
#Une matrice 



checkupRes <- function(Res) {
  layout(matrix(c(1, 1, 1, 2, 3, 4, 5, 6, 7), nrow = 3, ncol = 3, byrow = TRUE))
  plot(Res, main = "Évolution de la série", type = "l")
  acf = acf(Res, main = "ACF des résidus", lag.max = 50, plot=FALSE)
  plot(acf, ylim=c(-1,1),  main = "ACF des résidus")
  pacf = pacf(Res, main = "PACF des résidus", lag.max = 50, plot= FALSE)
  plot(pacf, ylim=c(-1,1), main = "PACF des résidus")
  plot(Res[-length(Res)], Res[-1],col="green" ,main = "Nuage de points Res[i] vs Res[i-1]")
  hist(Res, main = "Histogramme des résidus")
  qqnorm(Res, main = "QQ plot des résidus")
  qqline(Res)
  z <- (Res - mean(Res)) / sd(Res)
  plot(z, main = "Nuage de points série renormalisée", ylim = c(-1.96, 1.96))
  abline(h = c(-1.96, 1.96), col = "red")
  grid()
}

checkupRes(rnorm(1000))

