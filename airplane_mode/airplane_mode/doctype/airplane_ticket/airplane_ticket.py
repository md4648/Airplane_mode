# Copyright (c) 2025, md and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ranome_letter=random.choice(uppercase_letters)
random_digit = str(random.randint(0, 100))
seat=ranome_letter+random_digit

print(ranome_letter)


class AirplaneTicket(Document):
		

		def validate(self):
			total_amount=0
			add_item=[]
			if not self.flight_price:
				frappe.throw("Please Enter the Price")
			if self.status!="Boarded":
				frappe.throw("The status Must be Boarded")
				
			print("The type self.add_ons is ", type(self.add_ons))

			for add_onss in self.add_ons:# type of self.add_ons is  is list
				total_amount=add_onss.amount
				if add_onss.item in add_item:
					frappe.throw(f"Item '{add_onss.item}' is already added in Add-ons. Please remove duplicates.")

				add_item.append(add_onss.item)
			self.total_price=total_amount+self.flight_price
			self.seat=seat
			

  
	
	
	
        
	
	
      
	
	
	
	
			

  
			

      
			
      
			

 
	



























    # def validate(self):
    #     # Validate flight price is set
    #     if not self.flight_price:
    #         frappe.throw("Please Enter the Flight Price")
        
    #     # Initialize total amount
    #     total_amount = 0
    #     items_added = set()  # To track duplicate items
        
        
    #     for add_on in self.add_ons:
    #         if add_on.item in items_added:
    #             frappe.throw(f"Item '{add_on.item}' is already added in Add-ons. Please remove duplicates.")
    #         items_added.add(add_on.item)
            
    #         # Validate amount for each add-on
    #         if not add_on.amount or add_on.amount <= 0:
    #             frappe.throw(f"Please enter a valid amount for item '{add_on.item}'")
            
    #         total_amount += add_on.amount
        
    #     # Calculate total price
    #     self.total_price = total_amount + self.flight_price

    


