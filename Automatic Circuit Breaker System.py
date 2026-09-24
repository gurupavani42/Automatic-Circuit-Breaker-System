# Automatic Circuit Breaker System
# EEE Python Mini Project

# Protection limits
MIN_VOLTAGE = 210
MAX_VOLTAGE = 250
MAX_CURRENT = 100
MAX_TEMPERATURE = 80
MAX_SHORT_CIRCUIT_CURRENT = 200


def circuit_breaker(voltage, current, temperature):

    print("\n======================================")
    print("     AUTOMATIC CIRCUIT BREAKER")
    print("======================================")

    print(f"Voltage     : {voltage:.2f} V")
    print(f"Current     : {current:.2f} A")
    print(f"Temperature : {temperature:.2f} °C")

    faults = []

    # Over-voltage
    if voltage > MAX_VOLTAGE:
        faults.append("Over-Voltage")

    # Under-voltage
    elif voltage < MIN_VOLTAGE:
        faults.append("Under-Voltage")

    # Over-current
    if current > MAX_CURRENT:
        faults.append("Over-Current")

    # Short-circuit
    if current > MAX_SHORT_CIRCUIT_CURRENT:
        faults.append("Short-Circuit")

    # Over-temperature
    if temperature > MAX_TEMPERATURE:
        faults.append("Over-Temperature")

    print("\n----------- BREAKER STATUS -----------")

    # Trip breaker if fault is detected
    if len(faults) > 0:

        print("⚠ FAULT DETECTED")

        for fault in faults:
            print(" -", fault)

        print("\nCircuit Breaker : TRIPPED")
        print("Load Supply     : OFF")
        print("Protection      : ACTIVE")

    else:

        print("✓ SYSTEM NORMAL")
        print("Circuit Breaker : ON")
        print("Load Supply     : ON")
        print("Protection      : STANDBY")


# Main program

print("======================================")
print("    AUTOMATIC CIRCUIT BREAKER SYSTEM")
print("======================================")

voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
temperature = float(input("Enter Temperature (°C): "))

circuit_breaker(
    voltage,
    current,
    temperature
)
