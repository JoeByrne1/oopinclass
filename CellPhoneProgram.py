import CellPhoneClass as C

iphone16 = C.CellPhoneClass('apple', 'iphone', 1600)
galaxy10 = C.CellPhoneClass('samsung', 'galaxy', 1500)

print(f"The manufacturer of the phone is {iphone16.get_manufact()}")
print(f"The model of the phone is {iphone16.get_model()}")
print(f"The retail price of the phone is {iphone16.get_retail_price()}")

print(f"The manufacturer of the phone is {galaxy10.get_manufact()}")
print(f"The model of the phone is {galaxy10.get_model()}")
print(f"The retail price of the phone is {galaxy10.get_retail_price()}")