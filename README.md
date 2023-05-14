# RoboAdvisor
Optimal portfolio of ETFs based on risk classusing mean variance optimization
Initial Selection:
“ETF-data.xlsx” sheet ETF data is the data for all ETFs downloaded from stockanalysis.com.
In the preprocess.py script top 100 ETFs with highest volumes and top 100 ETFs with highest assets are taken and the common ETFs from both lists are chosen as best ETFs with high liquidity and narrow spread. As a result, we have 37 ETFs, for which monthly price history for is downloaded from yahoo finance for the past 5 years from 2018-01-01 to 2022-12-31 and stored in the sheet named “price history”. Then the monthly returns are calculated taking into account expense ratios and stored in the sheet named “returns”.
Questionnaire:
In the main code “main.py”, first the questionnaire with 16 questions and 3 choices for each with scores 5, 10 and 15 from more risk-averse to less is inserted in the interface in two columns. The scores are chosen as multiples of 5 so that the range is divisible into 5 equal intervals.
 ![image](https://github.com/ali-azary/RoboAdvisor/assets/69943289/86d1f31c-0609-407e-b5b6-4f898ede86f1)

Figure 1 Risk Assessment Questionnaire
Optimization:
After answering the questions and clicking the create portfolio button the portfolio optimization code runs. First, the total score is calculated by summing up the scores for all the questions. The total range is divided into 5 equal intervals as risk classes for which 5 values for risk-aversion coefficient   is assigned for the quadratic utility function. So, depending on the interval the total score is in, the corresponding risk-aversion coefficient is taken.   can have a wide range between 0.1 and 10 or higher, but the most widely accepted values are between 1 and 3. Therefore, we used values between 1 and 6, which seems to be a reasonable choice. 
	 
(1)


Then mean returns and covariances are calculated from the 5-year monthly data imported from the sheet named “returns”. Then the utility function is maximized to find optimal weights of the portfolios. Restricting the weights to the interval between 0 and 1 no shorting is allowed. 
	 
(2)

Multiplying the resulting optimal portfolio weights by returns of each ETF the portfolio returns are calculated and used to calculate the performance of the portfolio for the past 5 years starting from 100. Also, the triple exponential smoothing of Holt-Winters is used to forecast the performance for the following 12 months based on the performance of past 5 years. Exponential smoothing uses the historical data to forecast putting more weight on the most recent points. The simplest model only forecasts the level of the time series. Holt’s linear trend method also incorporates the trend along with the level. Holt-Winters or triple exponential smoothing also includes seasonality in forecasting.
Results:
In the end, a gauge shows the level of risk class and two plots are output: the performance plot over time and the pie chart of asset allocation indicating percentages and name of ETFs and their type of asset class. For example we can see comparing the riskiest and the least risky portfolios, we can see that for the riskiest the returns are higher as well as the variations. Also, it is worth noting the difference between diversification and asset classes in each portfolio.
 ![image](https://github.com/ali-azary/RoboAdvisor/assets/69943289/4e418e4a-72fc-4ce2-ad16-190de77c6db3)

Figure 2 The least Risky Portfolio
![image](https://github.com/ali-azary/RoboAdvisor/assets/69943289/65b43ad9-9a0d-437e-96e5-bc13d8f4796f)

 
Figure 3 The Riskiest Portfolio
References
https://stockanalysis.com/etf/screener/
https://www.initialreturn.com/risk-aversion-coefficient-meaning-formula/
https://www.investopedia.com/articles/exchangetradedfunds/08/etf-choose-best.asp
https://www.investopedia.com/terms/v/var.asp
Kim, D. and Francis, J.C., 2013. Modern portfolio theory: Foundations, analysis, and new developments. John Wiley & Sons.
https://towardsdatascience.com/time-series-forecasting-with-holt-winters-b78ffc322f24
Gándelman and Hernández-Murillo (2015) “Risk aversion at the country level” Federal Reserve Bank of St. Louis Review, First Quarter 2015, 97(1), pp. 53-66
