def calculate_shipping_cost(distance_km, weight_kg, rate_per_km=5, rate_per_kg=10):
    cost = (distance_km * rate_per_km) + (weight_kg * rate_per_kg)
    return cost

def estimate_delivery_time(distance_km, speed_kmh=60):
    return distance_km / speed_kmh

if __name__ == "__main__":
    distance = float(input("Enter distance in km: "))
    weight = float(input("Enter package weight in kg: "))

    cost = calculate_shipping_cost(distance, weight)
    days = estimate_delivery_time(distance) / 8  # 8 hours/day

    print(f"Shipping Cost: ₹{cost}")
    print(f"Estimated Delivery Time: {days:.1f} days")
