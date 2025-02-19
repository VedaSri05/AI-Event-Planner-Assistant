def forecast_revenue(initial_revenue, growth_rate, months):
    print("\n📈 Revenue Forecast for the Next 6 Months:")
    print("------------------------------------------------")
    print(f"{'Month':<10}{'Projected Revenue (₹)':<20}")
    print("------------------------------------------------")

    revenue = initial_revenue
    for month in range(1, months + 1):
        revenue += revenue * (growth_rate / 100)  # Apply growth rate
        print(f"{month:<10}₹{round(revenue, 2):<20}")
    
    print("------------------------------------------------")
    print(f"🚀 Estimated Revenue in 6 Months: ₹{round(revenue, 2)}")

# User input
initial_revenue = float(input("Enter current monthly revenue (₹): "))
growth_rate = float(input("Enter expected monthly growth rate (%): "))

# Run forecast
forecast_revenue(initial_revenue, growth_rate, months=6)
