from tkinter import *  
import pandas as pd
import plotly.express as px
import numpy as np
from scipy.optimize import minimize 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from PIL import Image, ImageTk


base = Tk()
base.state('zoomed')  

base.title('RoboAdvisor')

# logo = Image.open("logo.png")
# logo = logo.resize((210, 75), Image.LANCZOS)
# logo_image = ImageTk.PhotoImage(logo)
# logo_label = Label(base, image=logo_image)
# logo_label.place(x=20,y=0)



x0,y0=20,60
dx,dy=25,25
fs=8

# 1
Label(base, text="1. When it comes to investing, which best describes your goal? ",font=("bold",fs)).place(x=x0,y=y0)    
x1c = [
    ("a) Preservation of capital ", 5),
    ("b) Steady growth ", 10),
    ("c) High returns, even if it means taking on significant risk", 15),
]
x1=0
def sel():
    global x1
    x1=varx1.get()
varx1 = IntVar()
for txt, val in x1c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx1, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)

# 2
y0+=dy+5
Label(base, text="2. How would you feel if you lost some money on an investment?  ",font=("bold",fs)).place(x=x0,y=y0)    
x2c = [
    ("a) Devastated", 5),
    ("b) Disappointed  ", 10),
    ("c) Unfazed, it's part of the game", 15),
]
x2=0
def sel():
    global x2
    x2=varx2.get()
varx2 = IntVar()
for txt, val in x2c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx2, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)

# 3
y0+=dy+5
Label(base, text="3. What is your age?",font=("bold",fs)).place(x=x0,y=y0)    
x3c = [
    ("a) Under 30", 5),
    ("b) 30-50", 10),
    ("c) Over 50", 15),
]
x3=0
def sel():
    global x3
    x3=varx3.get()
varx3 = IntVar()
for txt, val in x3c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx3, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)

# 4
y0+=dy+5
Label(base, text="4. How long are you willing to leave your money invested?",font=("bold",fs)).place(x=x0,y=y0)    
x4c = [
    ("a) Less than a year", 5),
    ("b) 1-5 years  ", 10),
    ("c) More than 5 years", 15),
]
x4=0
def sel():
    global x4
    x4=varx4.get()
varx4 = IntVar()
for txt, val in x4c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx4, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)

# 5
y0+=dy+5
Label(base, text="5. How much investment experience do you have?",font=("bold",fs)).place(x=x0,y=y0)    
x5c = [
    ("a) None", 5),
    ("b) Limited", 10),
    ("c) Extensive", 15),
]
x5=0
def sel():
    global x5
    x5=varx5.get()
varx5 = IntVar()
for txt, val in x5c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx5, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)

# 6
y0+=dy+5
Label(base, text="6. Which statement best describes your financial situation?",font=("bold",fs)).place(x=x0,y=y0)    
x6c = [
    ("a) I am living paycheck to paycheck ", 5),
    ("b) I have some savings, but not much ", 10),
    ("c) I have a significant amount of savings", 15),
]
x6=0
def sel():
    global x6
    x6=varx6.get()
varx6 = IntVar()
for txt, val in x6c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx6, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# 7
y0+=dy+5
Label(base, text="7. How much of your portfolio are you willing to invest in risky assets, such as stocks or bonds? ",font=("bold",fs)).place(x=x0,y=y0)    
x7c = [
    ("a) None", 5),
    ("b) Less than 25%", 10),
    ("c) More than 25%", 15),
]
x7=0
def sel():
    global x7
    x7=varx7.get()
varx7 = IntVar()
for txt, val in x7c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx7, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)

# 8
y0+=dy+5
Label(base, text="8. How often do you check your investment portfolio? ",font=("bold",fs)).place(x=x0,y=y0)    
x8c = [
    ("a) Daily", 5),
    ("b) Weekly", 10),
    ("c) Monthly", 15),
]
x8=0
def sel():
    global x8
    x8=varx8.get()
varx8 = IntVar()
for txt, val in x8c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx8, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)

# second column
x0+=500
y0=60

# 9
Label(base, text="9. How comfortable are you with market fluctuations?",font=("bold",fs)).place(x=x0,y=y0)    
x9c = [
    ("a) Not at all comfortable ", 5),
    ("b) Somewhat comfortable", 10),
    ("c) Very comfortable", 15),
]
x9=0
def sel():
    global x9
    x9=varx9.get()
varx9 = IntVar()
for txt, val in x9c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx9, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# 10
y0+=dy+5
Label(base, text="10. How important is it for you to achieve high returns on your investments?",font=("bold",fs)).place(x=x0,y=y0)    
x10c = [
    ("a) Not important at all ", 5),
    ("b) Somewhat important ", 10),
    ("c) Very important", 15),
]
x10=0
def sel():
    global x10
    x10=varx10.get()
varx10 = IntVar()
for txt, val in x10c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx10, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# 11
y0+=dy+5
Label(base, text="11. How would you react if your investment lost 10% of its value in a single day?",font=("bold",fs)).place(x=x0,y=y0)    
x11c = [
    ("a) Hold on to it and wait for it to recover", 5),
    ("b) Sell a portion of it ", 10),
    ("c) Sell all of it immediately ", 15),
]
x11=0
def sel():
    global x11
    x11=varx11.get()
varx11 = IntVar()
for txt, val in x11c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx11, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# 12
y0+=dy+5
Label(base, text="12. When making an investment decision, how much emphasis do you place on the opinions of others?",font=("bold",fs)).place(x=x0,y=y0)    
x12c = [
    ("a) A lot, I always seek advice from others before making a decision ", 5),
    ("b) Some, I consider others' opinions but make my own decision ", 10),
    ("c) None, I make my investment decisions solely based on my own research and analysis", 15),
]
x12=0
def sel():
    global x12
    x12=varx12.get()
varx12 = IntVar()
for txt, val in x12c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx12, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# 13
y0+=dy+5
Label(base, text="13. What is your current marital status?",font=("bold",fs)).place(x=x0,y=y0)    
x13c = [
    ("a) Married", 5),
    ("b) Divorced", 10),
    ("c) Single", 15),
]
x13=0
def sel():
    global x13
    x13=varx13.get()
varx13 = IntVar()
for txt, val in x13c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx13, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)



# 14
y0+=dy+5
Label(base, text="14. How many children do you have?",font=("bold",fs)).place(x=x0,y=y0)    
x14c = [
    ("a) 3 or more", 5),
    ("b) 1-2", 10),
    ("c) None", 15),
]
x14=0
def sel():
    global x14
    x14=varx14.get()
varx14 = IntVar()
for txt, val in x14c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx14, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# 15
y0+=dy+5
Label(base, text="15. How much debt do you have, such as credit cards, student loans, or mortgages?",font=("bold",fs)).place(x=x0,y=y0)    
x15c = [
    ("a) A lot", 5),
    ("b) Some", 10),
    ("c) None", 15),
]
x15=0
def sel():
    global x15
    x15=varx15.get()
varx15 = IntVar()
for txt, val in x15c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx15, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# 16
y0+=dy+5
Label(base, text="16. Which of the following best describes your current employment status? ",font=("bold",fs)).place(x=x0,y=y0)    
x16c = [
    ("a) Employed full-time ", 5),
    ("b) Employed part-time ", 10),
    ("c) Unemployed", 15),
]
x16=0
def sel():
    global x16
    x16=varx16.get()
varx16 = IntVar()
for txt, val in x16c:
    y0+=dy
    Radiobutton(base, text=txt, variable=varx16, value=val, command=sel,font=("bold",fs)).place(x=x0,y=y0)


# simulate button
button = Button(master=base,text='Create Portfolio',width=100,height=2,bg='gray')
button.pack()
button.place(x=100,y=935)

# privacy disclaimer
# Label(base, text="Privacy Policy: RoboAdvisor does not collect or store any user data, ensuring complete privacy and anonymity for our users.",font=("bold",7)).place(x=20,y=900) 

def handle_click(event):
    
    # risk score    
    score=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16
    
    '''
    A review paper by Gándelman and Hernández-Murillo (2015) notes a wide range
    from 0.2 to 10 or higher. However, they add that “the most widely accepted 
    measures lie between 1 and 3”. According to their analysis, the coefficient 
    of relative risk aversion varies closely around the value of 1 across the 75 
    countries in their sample.
    ref: Gándelman and Hernández-Murillo (2015) “Risk aversion at the country level” 
    Federal Reserve Bank of St. Louis Review, First Quarter 2015, 97(1), pp. 53-66.
    '''
    # risk classes
    if score<=112:
        A=5 # Defensive (the least risk)
        risk_level = 1
    elif 112<score<=144:
        A=4 # Conservative
        risk_level = 2        
    elif 144<score<=176:
        A=3 # Moderae
        risk_level = 3
    elif 176<score<=208:
        A=2 # Assertive
        risk_level = 4
    elif 208<score:
        A=1 # Aggressive (the most risk)
        risk_level = 5
    

    # optimal portfolio
    # df = pd.read_csv('prices.csv', dtype=float, parse_dates=[0], index_col=0)
    # df = pd.read_excel('ETF-data.xlsx', sheet_name='price history', index_col=[0])
    returns_df = pd.read_excel('ETF-data.xlsx', sheet_name='returns', index_col=[0])
   
    # returns_df = df.pct_change()
    

    mean_returns = returns_df.mean()
    variances = returns_df.var()
    covariances = returns_df.cov()

    def objective(weights, mean_returns, covariances):
        rp = np.dot(weights, mean_returns)
        sigp = np.sqrt(np.dot(weights.T, np.dot(covariances, weights)))
        utility=rp-.5*A*sigp**2
        return -utility

    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]
    bounds = [(0, 1)] * len(mean_returns)

    
    result = minimize(objective, np.ones(len(mean_returns)) / len(mean_returns), args=(mean_returns, covariances), bounds=bounds, constraints=constraints)
    weights = pd.DataFrame(index=mean_returns.index)
    
    
    weights['weights']=result.x
    

    expected_return = np.dot(weights.T, mean_returns)
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(covariances, weights)))
    
    returns_df['portfolio']=0.
    
    for etf in weights[weights['weights'] > 0.0001].index:
        returns_df['portfolio']+=returns_df[etf]*weights[weights['weights'] > 0.0001]['weights'][etf]
       
    returns_df['performance'] = 100 * (1 + returns_df['portfolio']).cumprod()
    returns_df['performance']['1/1/2018'] = 100
    
    #  holt-winters forecast
    fit = ExponentialSmoothing(returns_df['performance'], seasonal_periods=12, trend='add', seasonal='add',freq='MS').fit()
    forecast = fit.forecast(12)
    
    forecast=pd.concat([returns_df['performance'].tail(1),forecast])    
    # plot performance
    figure1 = plt.Figure(figsize=(8, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    line = FigureCanvasTkAgg(figure1, base)
    line.get_tk_widget().place(x=1050,y=555)
    
    ax1.plot(returns_df.index,returns_df.performance,'k' ,label='past 5 years')
    ax1.plot(forecast,'b',label='forecast')
    ax1.legend()
    Label(base, text="Portfolio Performance",font=("bold",14),bg="white").place(x=1365,y=555)

    # pie chart
    figure2 = plt.Figure(figsize=(8, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    
    pie = FigureCanvasTkAgg(figure2, base)
    pie.get_tk_widget().place(x=1050,y=140)
    
    # df = pd.read_csv('screener-etf.csv')
    df = pd.read_excel('ETF-data.xlsx', sheet_name='ETF data')
    df.set_index('Symbol', inplace=True)
    weights = weights.merge(df['Asset Class'], left_index=True, right_index=True)
    weights.index = weights.index + ' (' + weights['Asset Class'] + ')'
    
    explode=[.05 for i in range(len(weights[weights['weights'] > 0.0001]['weights']))]
    ax2.pie(weights[weights['weights'] > 0.0001].weights,autopct='%1.1f%%',pctdistance=1.2, explode=explode)
    ax2.legend(weights[weights['weights'] > 0.0001].index,bbox_to_anchor=(1.05, 1.0))
    Label(base, text="Portfolio Weights",font=("bold",14),bg="white").place(x=1375,y=140)
    
    # risk gauge
    figure3 = plt.Figure(figsize=(8, 1), dpi=100)
    FigureCanvasTkAgg(figure3, base).get_tk_widget().place(x=1050,y=30)
    Label(base, text="Risk Class",font=("bold",14),bg="white").place(x=1400,y=30) 

    values = ["Defensive", "Conservative", "Moderate", "Aggressive", "Very Aggressive"]
    colors = ["blue", "deep sky blue", "light green", "orange", "red"]
    values = ["Defensive", "Conservative", "Moderate", "Assertive", "Aggressive"]
    num_values = len(values)

    width = 600
    height = 30
    canvas = Canvas(base, width=width, height=60,bg="white", bd=0, highlightthickness=0, relief='ridge')
    canvas.place(x=1150,y=65)
    canvas.create_rectangle(0, 10, width, height, fill="white", outline="black")
    section_width = width / num_values
    for i in range(num_values):
        xl = i * section_width
        xr = (i+1) * section_width
        canvas.create_rectangle(xl, 10, xr, height, fill=colors[i], outline="black")
        canvas.create_text((xl + xr) / 2+1, (height+10) / 2, text=values[i], fill="white",font='bold 11')
        canvas.create_text((xl + xr) / 2, (height+10) / 2+1, text=values[i], fill="white",font='bold 11')
        canvas.create_text((xl + xr) / 2, (height+10) / 2-1, text=values[i], fill="white",font='bold 11')
        canvas.create_text((xl + xr) / 2-1, (height+10) / 2, text=values[i], fill="white",font='bold 11')
        canvas.create_text((xl + xr) / 2, (height+10) / 2, text=values[i], fill="black",font='bold 11')
    
     
    line_x = (risk_level-1) * section_width + section_width/2
    line_y1 = height
    line_y2 = 10
    canvas.create_polygon(line_x-10, line_y1+10, line_x+10, line_y1+10, line_x, line_y1, fill="red")
    canvas.create_polygon(line_x-10, line_y2-10, line_x+10, line_y2-10, line_x, line_y2, fill="red")    
    
button.bind('<Button-1>',handle_click)
base.mainloop()  

