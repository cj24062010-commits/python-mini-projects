"""USD to INR Currency Converter Utility
Author: Chirag Jain
Description: Converts multiple USD values into Indian Rupees (INR) 
             using a fixed market exchange rate.
"""

# Define exchange rate as a constant variable 
USD_TO_INR_RATE = 95.15


def convert_usd_to_inr(usd_amount: float) -> float:
  """Converts a given USD amount to INR and rounds to 2 decimal places."""
  return round(usd_amount * USD_TO_INR_RATE, 2)


if __name__ == "__main__":
  # List of USD values to convert
  usd_amounts = [100, 65, 47]
  
  # Loop through each value cleanly instead of writing repeated code
  for amount in usd_amounts:
    converted_value = convert_usd_to_inr(amount)
    print(f"${amount} USD is equal to ₹{converted_value}")
