# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Use the global conversion factor to convert Fahrenheit to Celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Use the global conversion factor to convert Celsius to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature value: ").strip()
        # Validate temperature input as numeric
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted:.2f}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted:.2f}°C")
    else:
        raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
