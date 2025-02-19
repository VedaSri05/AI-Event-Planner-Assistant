def calculate_revenue(premium_users, business_users, pay_per_use_users, vendor_bookings):
    # Pricing for different plans
    premium_price = 499
    business_price = 999
    pay_per_use_price = 99
    vendor_commission = 0.05  # 5% commission

    # Revenue calculations
    subscription_revenue = (premium_price * premium_users) + (business_price * business_users)
    pay_per_use_revenue = pay_per_use_price * pay_per_use_users
    vendor_revenue = vendor_commission * vendor_bookings

    # Total revenue
    total_revenue = subscription_revenue + pay_per_use_revenue + vendor_revenue

    # Display results
    print("\n📊 Monthly Revenue Breakdown:")
    print(f"💰 Subscription Revenue: ₹{subscription_revenue}")
    print(f"💰 Pay-Per-Use Revenue: ₹{pay_per_use_revenue}")
    print(f"💰 Vendor Commission Revenue: ₹{vendor_revenue}")
    print(f"\n🚀 Total Monthly Revenue: ₹{total_revenue}")

# User input
premium_users = int(input("Enter number of Premium Plan users: "))
business_users = int(input("Enter number of Business Plan users: "))
pay_per_use_users = int(input("Enter number of Pay-Per-Use users: "))
vendor_bookings = int(input("Enter total vendor booking value (₹): "))

# Calculate revenue
calculate_revenue(premium_users, business_users, pay_per_use_users, vendor_bookings)
