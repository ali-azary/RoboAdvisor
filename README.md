# RoboAdvisor
Optimal portfolio of ETFs based for five risk appetites using mean variance optimization

![image](https://github.com/ali-azary/RoboAdvisor/assets/69943289/8161ec57-0c9f-4384-b7d7-308228f0860d)

Initial Selection:
“ETF-data.xlsx” sheet ETF data is the data for all ETFs downloaded from stockanalysis.com.
In the preprocess.py script top 100 ETFs with highest volumes and top 100 ETFs with highest assets are taken and the common ETFs from both lists are chosen as best ETFs with high liquidity and narrow spread. As a result, we have 37 ETFs, for which monthly price history for is downloaded from yahoo finance for the past 5 years from 2018-01-01 to 2022-12-31 and stored in the sheet named “price history”. Then the monthly returns are calculated taking into account expense ratios and stored in the sheet named “returns”.
Questionnaire:
In the main code “main.py”, first the questionnaire with 16 questions and 3 choices for each with scores 5, 10 and 15 from more risk-averse to less is inserted in the interface in two columns. The scores are chosen as multiples of 5 so that the range is divisible into 5 equal intervals.

Optimization:
After answering the questions and clicking the create portfolio button the portfolio optimization code runs. First, the total score is calculated by summing up the scores for all the questions. The total range is divided into 5 equal intervals as risk classes for which 5 values for risk-aversion coefficient   is assigned for the quadratic utility function. So, depending on the interval the total score is in, the corresponding risk-aversion coefficient is taken.   can have a wide range between 0.1 and 10 or higher, but the most widely accepted values are between 1 and 3. Therefore, we used values between 1 and 6, which seems to be a reasonable choice. 
	 
![image](https://github.com/ali-azary/RoboAdvisor/assets/69943289/9df3d273-f28f-47d7-aa04-f1278ad6ec8d)


Then mean returns and covariances are calculated from the 5-year monthly data imported from the sheet named “returns”. Then the utility function is maximized to find optimal weights of the portfolios. Restricting the weights to the interval between 0 and 1 no shorting is allowed. 
	 

![image](https://github.com/ali-azary/RoboAdvisor/assets/69943289/85a94574-d7c5-4267-acd5-a0a2eb3339dd)


Multiplying the resulting optimal portfolio weights by returns of each ETF the portfolio returns are calculated and used to calculate the performance of the portfolio for the past 5 years starting from 100. Also, the triple exponential smoothing of Holt-Winters is used to forecast the performance for the following 12 months based on the performance of past 5 years. Exponential smoothing uses the historical data to forecast putting more weight on the most recent points. The simplest model only forecasts the level of the time series. Holt’s linear trend method also incorporates the trend along with the level. Holt-Winters or triple exponential smoothing also includes seasonality in forecasting.
Results:
In the end, a gauge shows the level of risk class and two plots are output: the performance plot over time and the pie chart of asset allocation indicating percentages and name of ETFs and their type of asset class. For example we can see comparing the riskiest and the least risky portfolios, we can see that for the riskiest the returns are higher as well as the variations. Also, it is worth noting the difference between diversification and asset classes in each portfolio.
 
