# -*- coding: utf-8 -*-
"""vat_calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SC8pPTg7h4-Et5qnWfOYPwiq_Q4UC3v4
"""

amounts_without_vat = [(10, "high"),(25, "low"),(60, "zero")]

def add_vat(amount, rate):
  high_rate = 1.21
  low_rate = 1.06
  
  if rate == 'high':
    amount_with_vat = amount*high_rate
  elif rate == "low":
    amount_with_vat = amount*low_rate
  else:
    amount_with_vat = amount
    
  return amount_with_vat

for amount_without_vat in amounts_without_vat:
  print("Value without VAT was EUR ", amount_without_vat[0])
  print("Added the", amount_without_vat[1]," VAT rate")
  print("Total is now EUR ", add_vat(amount_without_vat[0], amount_without_vat[1]))
  print()



