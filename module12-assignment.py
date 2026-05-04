# Module 12 Assignment: Business Analytics Fundamentals and Applications
# GreenGrocer Data Analysis

#we must import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#we print a welcome message to our company 
print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO CREATE SAMPLE DATA (DO NOT MODIFY) -----
np.random.seed(42)

stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}
store_df = pd.DataFrame(store_data)

departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

sales_data = []
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

store_performance = {
    "Tampa": 1.0,
    "Orlando": 0.85,
    "Miami": 1.2,
    "Jacksonville": 0.75,
    "Gainesville": 0.65
}

dept_performance = {
    "Produce": 1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery": 0.95,
    "Prepared Foods": 1.1
}

for date in dates:
    month = date.month
    seasonal_factor = 1.0
    if month in [6, 7, 8]:
        seasonal_factor = 1.15
    elif month == 12:
        seasonal_factor = 1.25
    elif month in [1, 2]:
        seasonal_factor = 0.9

    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0

    for store in stores:
        store_factor = store_performance[store]
        for dept in departments:
            dept_factor = dept_performance[dept]
            for category in categories[dept]:
                base_sales = np.random.normal(loc=500, scale=100)
                sales_amount = base_sales * store_factor * dept_factor * seasonal_factor * dow_factor
                sales_amount = sales_amount * np.random.normal(loc=1.0, scale=0.1)

                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery": 0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]
                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)
                profit = sales_amount * profit_margin

                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })

sales_df = pd.DataFrame(sales_data)

customer_data = []
total_customers = 5000
age_mean, age_std = 42, 15
income_mean, income_std = 85, 30
segments = ["Health Enthusiast", "Gourmet Cook", "Family Shopper", "Budget Organic", "Occasional Visitor"]
segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]
store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami": 0.30,
    "Jacksonville": 0.15,
    "Gainesville": 0.10
}

for i in range(total_customers):
    age = int(np.random.normal(loc=age_mean, scale=age_std))
    age = max(min(age, 85), 18)
    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])
    income = int(np.random.normal(loc=income_mean, scale=income_std))
    income = max(income, 20)
    segment = np.random.choice(segments, p=segment_probabilities)
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))

    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8, 15)
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120, scale=25)
    elif segment == "Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150, scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)

    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket = max(avg_basket, 15)
    monthly_spend = visit_frequency * avg_basket

    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"

    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000,
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth": visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(visit_frequency * avg_basket, 2),
        "LoyaltyTier": loyalty_tier
    })

customer_df = pd.DataFrame(customer_data)

operational_data = []
for store in stores:
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]
    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"] == store]["Profit"].sum()
    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(5, np.random.normal(loc=4.0, scale=0.3) *
                                (store_performance[store] ** 0.5))
    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft, 2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })

operational_df = pd.DataFrame(operational_data)

print("\nDataframes created successfully. Ready for analysis!")
print(f"Sales data shape: {sales_df.shape}")
print(f"Customer data shape: {customer_df.shape}")
print(f"Store data shape: {store_df.shape}")
print(f"Operational data shape: {operational_df.shape}")

print("\nSales Data Sample:")
print(sales_df.head(3))
print("\nCustomer Data Sample:")
print(customer_df.head(3))
print("\nStore Data Sample:")
print(store_df)
print("\nOperational Data Sample:")
print(operational_df)
# ----- END OF DATA CREATION -----
#we do not manipulate this data because it will serve as the main data frame for the creation of our figures

# TODO 1

def analyze_sales_performance():
    #we sum up total sales and profit across all stores, departments, and dates
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    #the average profit margin tells us how much of each dollar of sales becomes profit
    avg_profit_margin = sales_df["ProfitMargin"].mean()
    #we group by store and department to see which locations and sections returns the most revenue
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)

    print("\n--- Sales Performance Summary ---")
    print(f"Total Annual Sales:    ${total_sales:,.2f}")
    print(f"Total Annual Profit:   ${total_profit:,.2f}")
    print(f"Avg Profit Margin:     {avg_profit_margin:.2%}")
    print("\nSales by Store:")
    print(sales_by_store.apply(lambda x: f"${x:,.2f}"))
    print("\nSales by Department:")
    print(sales_by_dept.apply(lambda x: f"${x:,.2f}"))

    # describe() gives count, mean, std, min, quartiles, and max
    print("\nSales Descriptive Statistics:")
    print(sales_df["Sales"].describe())

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "avg_profit_margin": avg_profit_margin,
        "sales_by_store": sales_by_store,
        "sales_by_dept": sales_by_dept
    }


def visualize_sales_distribution():
   
    #we create a bar chart showing which store generates the most total annual sales
    store_fig, ax1 = plt.subplots(figsize=(8, 5))
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    ax1.bar(sales_by_store.index, sales_by_store.values, color="steelblue")
    ax1.set_title("Annual Sales by Store")
    ax1.set_xlabel("Store")
    ax1.set_ylabel("Total Sales ($)")
    # set_xticks must be called before set_xticklabels to avoid matplotlib warnings
    ax1.set_xticks(range(len(sales_by_store.index)))
    ax1.set_xticklabels(sales_by_store.index, rotation=15)
    store_fig.tight_layout()

    #again, we create another bar chart that will show instead of the stores, the departments that make the most total annual sales
    dept_fig, ax2 = plt.subplots(figsize=(8, 5))
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)
    ax2.bar(sales_by_dept.index, sales_by_dept.values, color="darkorange")
    ax2.set_title("Annual Sales by Department")
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Total Sales ($)")
    ax2.set_xticks(range(len(sales_by_dept.index)))
    ax2.set_xticklabels(sales_by_dept.index, rotation=15)
    dept_fig.tight_layout()

    #now, we do a line chart showing how total sales changed month by month
    time_fig, ax3 = plt.subplots(figsize=(10, 5))
    sales_df["Month"] = sales_df["Date"].dt.to_period("M")
    monthly_sales = sales_df.groupby("Month")["Sales"].sum()
    month_labels = monthly_sales.index.astype(str)
    ax3.plot(month_labels, monthly_sales.values, marker="o", color="green")
    ax3.set_title("Monthly Sales Trend (2023)")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Total Sales ($)")
    ax3.set_xticks(range(len(month_labels)))
    ax3.set_xticklabels(month_labels, rotation=45)
    time_fig.tight_layout()

    return (store_fig, dept_fig, time_fig)


def analyze_customer_segments():
    #first, we count how many customers fall into each segment
    segment_counts = customer_df["Segment"].value_counts()
    #now, our avg monthly spend per segment tells us which group is most valuable 
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False) #descending order
    segment_loyalty = customer_df.groupby(["Segment", "LoyaltyTier"]).size().unstack(fill_value=0)
    #groupby will merge both groups and then comparre them, in this case, their behavior patterns

    print("\n--- Customer Segment Analysis ---")
    print("\nSegment Counts:")
    print(segment_counts)
    print("\nAverage Monthly Spend by Segment:")
    print(segment_avg_spend.apply(lambda x: f"${x:.2f}"))
    print("\nLoyalty Tier Distribution by Segment:")
    print(segment_loyalty)

    #we create a bar chart visualizing which customer segments spend the most on average per month
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(segment_avg_spend.index, segment_avg_spend.values, color="mediumpurple")
    ax.set_title("Average Monthly Spend by Customer Segment")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Avg Monthly Spend ($)")
    ax.set_xticks(range(len(segment_avg_spend.index)))
    ax.set_xticklabels(segment_avg_spend.index, rotation=20)
    fig.tight_layout()

    return {
        "segment_counts": segment_counts,
        "segment_avg_spend": segment_avg_spend,
        "segment_loyalty": segment_loyalty
    }


# TODO 2

def analyze_sales_correlations():
    
    #we merge store characteristics with the results, so we can measure how each characteristic relates to their performance
    merged = operational_df.merge(store_df, on="Store")
    numeric_cols = ["AnnualSales", "AnnualProfit", "SalesPerSqFt", "ProfitPerSqFt",
                    "SalesPerStaff", "InventoryTurnover", "CustomerSatisfaction",
                    "SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend"]
    #the .corr method shows how strongly each pair of variables moves together
    store_correlations = merged[numeric_cols].corr()

    #now, we isolate the correlations specifically with AnnualSales, and we sort them by absolute strength
    sales_corr = store_correlations["AnnualSales"].drop("AnnualSales").sort_values(
        key=abs, ascending=False) #descending order
    top_correlations = list(zip(sales_corr.index, sales_corr.values))

    print("\n--- Correlation Analysis ---")
    print("\nTop Factors Correlated with Annual Sales:")
    for factor, corr in top_correlations:
        print(f"  {factor}: {corr:.4f}")
        
    #we assign different colors to the correlations
    correlation_fig, ax = plt.subplots(figsize=(9, 5))
    colors = ["blue" if c >= 0 else "red" for c in sales_corr.values]
    ax.bar(sales_corr.index, sales_corr.values, color=colors)
    ax.set_title("Correlation of Store Metrics with Annual Sales")
    ax.set_xlabel("Factor")
    ax.set_ylabel("Correlation Coefficient")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xticks(range(len(sales_corr.index)))
    ax.set_xticklabels(sales_corr.index, rotation=30, ha="right")
    correlation_fig.tight_layout()

    return {
        "store_correlations": store_correlations,
        "top_correlations": top_correlations,
        "correlation_fig": correlation_fig
    }


def compare_store_performance():
    
    #first, we neeed to pull only efficiency-related columns for comparison
    efficiency_metrics = operational_df[["Store", "SalesPerSqFt", "SalesPerStaff",
                                         "ProfitPerSqFt", "CustomerSatisfaction"]].set_index("Store")
    #we rank stores by total annual profit to get the best and worst in performance
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)

    print("\n--- Store Performance Comparison ---")
    print("\nEfficiency Metrics by Store:")
    print(efficiency_metrics)
    print("\nPerformance Ranking by Annual Profit:")
    print(performance_ranking.apply(lambda x: f"${x:,.2f}"))
    
    comparison_fig, ax = plt.subplots(figsize=(10, 5))
    x = np.arange(len(efficiency_metrics.index))
    width = 0.2
    metrics_to_plot = ["SalesPerSqFt", "SalesPerStaff", "ProfitPerSqFt"]
    colors = ["steelblue", "darkorange", "green"]
    for i, (metric, color) in enumerate(zip(metrics_to_plot, colors)):
        #now, assign each metric to 0-100 for a comparison
        vals = efficiency_metrics[metric]
        normalized = (vals - vals.min()) / (vals.max() - vals.min()) * 100
        ax.bar(x + i * width, normalized, width, label=metric, color=color)
    ax.set_title("Normalized Store Efficiency Metrics (0-100 scale)")
    ax.set_xlabel("Store")
    ax.set_ylabel("Normalized Score")
    ax.set_xticks(x + width)
    ax.set_xticklabels(efficiency_metrics.index)
    ax.legend()
    comparison_fig.tight_layout()

    return {
        "efficiency_metrics": efficiency_metrics,
        "performance_ranking": performance_ranking,
        "comparison_fig": comparison_fig
    }


def analyze_seasonal_patterns():
   
    #first, we extract month number and day name from the date column
    sales_df["Month"] = sales_df["Date"].dt.month
    sales_df["DayOfWeek"] = sales_df["Date"].dt.day_name()

    monthly_sales = sales_df.groupby("Month")["Sales"].sum()
    #we havce to put the days in calendar form, in other words, from Monday to Sunday
    dow_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dow_sales = sales_df.groupby("DayOfWeek")["Sales"].sum().reindex(dow_order)

    print("\n--- Seasonal Pattern Analysis ---")
    print("\nMonthly Sales Totals:")
    print(monthly_sales.apply(lambda x: f"${x:,.2f}"))
    print("\nSales by Day of Week:")
    print(dow_sales.apply(lambda x: f"${x:,.2f}"))

    #now, we create two bar charts,  one for monthly patterns, and the other fpr one for day-of-week patterns
    seasonal_fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    ax1.bar(month_names, monthly_sales.values, color="blue")
    ax1.set_title("Total Sales by Month")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Total Sales ($)")
    ax1.set_xticks(range(len(month_names)))
    ax1.set_xticklabels(month_names, rotation=45)

    ax2.bar(dow_sales.index, dow_sales.values, color="red")
    ax2.set_title("Total Sales by Day of Week")
    ax2.set_xlabel("Day of Week")
    ax2.set_ylabel("Total Sales ($)")
    ax2.set_xticks(range(len(dow_sales.index)))
    ax2.set_xticklabels(dow_sales.index, rotation=30)

    seasonal_fig.tight_layout()

    return {
        "monthly_sales": monthly_sales,
        "dow_sales": dow_sales,
        "seasonal_fig": seasonal_fig
    }


# TODO 3

def predict_store_sales():
   
    #we merge store characteristics with operational results to have everything in one place
    merged = operational_df.merge(store_df, on="Store")

    #we use SquareFootage as the primary predictor because it has the strongest correlation with sales
    x = merged["SquareFootage"].values
    y = merged["AnnualSales"].values #.values will only pull out the numbers
    #linregress returns slope, intercept, r-value, p-value, and standard error
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    #r-squared tells us what % of sales variation is explained by store size alone
    r_squared = r_value ** 2
    predictions = pd.Series(slope * x + intercept, index=merged["Store"])

    #we have to run individual regressions for each feature to compare them
    features = ["SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend"]
    coefficients = {}
    for feat in features:
        s, inter, rv, pv, se = stats.linregress(merged[feat].values, y)
        coefficients[feat] = round(s, 4)

    print("\n--- Store Sales Prediction Model ---")
    print("\nPrimary Predictor: SquareFootage")
    print(f"  Slope (coefficient): {slope:.4f}")
    print(f"  Intercept:           {intercept:.4f}")
    print(f"  R-squared:           {r_squared:.4f}")
    print(f"  p-value:             {p_value:.4f}")
    print("\nCoefficients (individual regressions vs AnnualSales):")
    for k, v in coefficients.items():
        print(f"  {k}: {v:.4f}")
    print("\nPredicted vs Actual Sales:")
    for store, pred, actual in zip(merged["Store"], predictions.values, y):
        print(f"  {store}: Predicted ${pred:,.0f} | Actual ${actual:,.0f}")

    #now, we create a scatter plot with regression line
    model_fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(x, y, color="blue", zorder=5, label="Actual")
    x_line = np.linspace(x.min(), x.max(), 100)
    ax.plot(x_line, slope * x_line + intercept, color="red", label=f"Fit (R²={r_squared:.3f})")
    for xi, yi, store in zip(x, y, merged["Store"]):
        ax.annotate(store, (xi, yi), textcoords="offset points", xytext=(5, 3), fontsize=9)
    ax.set_title("Store Square Footage vs Annual Sales")
    ax.set_xlabel("Square Footage")
    ax.set_ylabel("Annual Sales ($)")
    ax.legend()
    model_fig.tight_layout()

    return {
        "coefficients": coefficients,
        "r_squared": r_squared,
        "predictions": predictions,
        "model_fig": model_fig
    }


def forecast_department_sales():
    
    #we group the sales by month and department 
    sales_df["Month"] = sales_df["Date"].dt.month
    dept_monthly = sales_df.groupby(["Month", "Department"])["Sales"].sum().unstack()
    dept_trends = dept_monthly
    
    #the growth rate will compare the average of the first 3 months to the last three
    growth_rates = {}
    for dept in departments:
        first_3 = dept_monthly[dept].iloc[:3].mean()
        last_3 = dept_monthly[dept].iloc[-3:].mean()
        growth_rates[dept] = (last_3 - first_3) / first_3
    growth_rates = pd.Series(growth_rates).sort_values(ascending=False)

    print("\n--- Department Sales Forecast ---")
    print("\nGrowth Rates (first 3 months vs last 3 months):")
    print(growth_rates.apply(lambda x: f"{x:.2%}"))

    #we create a line chart with one line for each department
    forecast_fig, ax = plt.subplots(figsize=(10, 6))
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for dept in departments:
        ax.plot(month_names, dept_monthly[dept].values, marker="o", label=dept)
    ax.set_title("Monthly Sales Trend by Department")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Sales ($)")
    ax.legend()
    ax.set_xticks(range(len(month_names)))
    ax.set_xticklabels(month_names, rotation=45)
    forecast_fig.tight_layout()

    return {
        "dept_trends": dept_trends,
        "growth_rates": growth_rates,
        "forecast_fig": forecast_fig
    }


#TODO 4

def identify_profit_opportunities():
   
    #we collect the aggregate sales, profit, and margin for every store-department combination
    store_dept = sales_df.groupby(["Store", "Department"]).agg(
        TotalSales=("Sales", "sum"),
        TotalProfit=("Profit", "sum"),
        AvgMargin=("ProfitMargin", "mean")
    ).reset_index()
    #we normalize profit to a 0-1 score relative to the single best-performing combination
    store_dept["ProfitScore"] = store_dept["TotalProfit"] / store_dept["TotalProfit"].max()

    #the top 10 combinations show where to double down on investment
    top_combinations = store_dept.sort_values("TotalProfit", ascending=False).head(10)
    #the bottom 10 combinations reveal where performance lags and intervention is needed
    underperforming = store_dept.sort_values("TotalProfit", ascending=True).head(10)

    #the stores with lower average profit scores have more room to grow, and we name them opportunity score 
    opportunity_score = (1 - store_dept.groupby("Store")["ProfitScore"].mean()).sort_values(ascending=False)

    print("\n--- Profit Opportunity Analysis ---")
    print("\nTop 10 Store-Department Combinations by Profit:")
    print(top_combinations[["Store", "Department", "TotalSales", "TotalProfit", "AvgMargin"]].to_string(index=False))
    print("\nBottom 10 (Underperforming) Store-Department Combinations:")
    print(underperforming[["Store", "Department", "TotalSales", "TotalProfit", "AvgMargin"]].to_string(index=False))
    print("\nOpportunity Score by Store (higher = more room to grow):")
    print(opportunity_score.apply(lambda x: f"{x:.4f}"))

    return {
        "top_combinations": top_combinations,
        "underperforming": underperforming,
        "opportunity_score": opportunity_score
    }


def develop_recommendations():
    
    #we need 5 recomendations for our company
    recommendations = [
        "1. INVEST IN MIAMI AND TAMPA: These two stores generate the highest sales and profit. Increase marketing spend and expand product range, especially in high-margin departments (Prepared Foods and Bakery), to capitalize on their strong customer base.",

        "2. PRIORITIZE HIGH-MARGIN DEPARTMENTS CHAIN-WIDE: Prepared Foods and Bakery deliver significantly higher margins than Grocery. Allocate more floor space and staff resources to these departments across all locations.",

        "3. BOOST UNDERPERFORMING STORES WITH TARGETED MARKETING: Gainesville and Jacksonville  underperform relative to their size. Introduce localized promotions and loyalty incentives to increase visit frequency, particularly targeting the 'Budget Organic' and 'Health Enthusiast' segments that make frequent visits.",

        "4. MAXIMIZE WEEKEND AND SEASONAL REVENUE: Sales spike on weekends and during summer/December. Schedule additional staff during peak periods, run weekend-only promotions, and prepare inventory.",

        "5. GROW THE FAMILY SHOPPER AND GOURMET COOK SEGMENTS: These segments have the highest average basket sizes ($150 and $120 respectively). Introduce meal-kit offerings, and cooking events to attract and retain these high-value customers.",

    ]

    print("\n--- Recommendations ---")
    for rec in recommendations:
        print(f"\n{rec}")

    return recommendations


#TODO 5
#now, we need to define a function that will generate our summary

def generate_executive_summary():
    #we pull the key headline numbers that will anchor the summary
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()
    avg_margin = sales_df["ProfitMargin"].mean()
    #we use idxmax() to find the top store and department
    #this updates automatically if the data changes
    best_store = sales_df.groupby("Store")["Sales"].sum().idxmax()
    best_dept = sales_df.groupby("Department")["ProfitMargin"].mean().idxmax()

    print("\n" + "=" * 60)
    print("EXECUTIVE SUMMARY: GREENGROCER ANNUAL PERFORMANCE REPORT")
    print("=" * 60)

    print(f"""
OVERVIEW:
GreenGrocer generated ${total_sales:,.0f} in total sales and ${total_profit:,.0f} in profit across its five Florida locations in 2023, delivering an average profit margin of {avg_margin:.1%}.
The Miami location led performance, while Gainesville and Jacksonville represent opportunities for improvement. This analysis tells us certain patterns on behavior that we can use to our advantage and make better decisions. 

KEY FINDINGS:
• Sales peak in months June to August and then in December, with weekends generating approximately 30% more revenue
  than weekdays. 
• Family Shoppers and Gourmet Cooks are the highest-value customer segments by basket size.
• Jacksonville and Gainesville are underperforming relative to the chain average, with opportunity to improve.

RECOMMENDATIONS:
• Increase investment in Miami and Tampa, focusing on Prepared Foods and Bakery to maximize margin.
• Develop packages and offerings to attract Family Shoppers
  and Gourmet Cooks, who deliver the highest basket values.
• Use loyalty program data to build personalized retention campaigns for Platinum members.

EXPECTED IMPACT:
Implementing these recommendations is expected to improve overall chain profitability by shifting sales mix toward higher-margin departments and closing the performance gap between top and underperforming stores.
An improvement in profit margin at the two underperforming stores, combined with an uplift in high-margin department sales chain-wide, could add an estimated $500,000+ in annual profit. Longer-term, investments in store expansion and loyalty program enhancements will attract more revenue.
""")


#finally, we define our last function and getting the return, and then calling it
def main():
    print("\n" + "=" * 60)
    print("GREENGROCER BUSINESS ANALYTICS RESULTS")
    print("=" * 60)

    print("\n--- DESCRIPTIVE ANALYTICS: CURRENT PERFORMANCE ---")
    sales_metrics = analyze_sales_performance()
    dist_figs = visualize_sales_distribution()
    customer_analysis = analyze_customer_segments()

    print("\n--- DIAGNOSTIC ANALYTICS: UNDERSTANDING RELATIONSHIPS ---")
    correlations = analyze_sales_correlations()
    store_comparison = compare_store_performance()
    seasonality = analyze_seasonal_patterns()

    print("\n--- PREDICTIVE ANALYTICS: FORECASTING ---")
    sales_model = predict_store_sales()
    dept_forecast = forecast_department_sales()

    print("\n--- BUSINESS INSIGHTS AND RECOMMENDATIONS ---")
    opportunities = identify_profit_opportunities()
    recommendations = develop_recommendations()

    print("\n--- EXECUTIVE SUMMARY ---")
    generate_executive_summary()

    plt.show()

    return {
        "sales_metrics": sales_metrics,
        "customer_analysis": customer_analysis,
        "correlations": correlations,
        "store_comparison": store_comparison,
        "seasonality": seasonality,
        "sales_model": sales_model,
        "dept_forecast": dept_forecast,
        "opportunities": opportunities,
        "recommendations": recommendations
    }


if __name__ == "__main__":
    results = main()
