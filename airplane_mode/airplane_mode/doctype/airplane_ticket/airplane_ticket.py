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
			
			dd=frappe.get_value("Airplane","Airbus001","capacity")
			total_ticket=frappe.get_all("Airplane Ticket")
			total_airbus_ticket=frappe.get_all("Airplane Ticket",filters={"flight":"Airbus001-05-04-0009"})
			specificAirplanecapacity=frappe.get_all("Airplane Ticket",fields=["flight.airplane"])


			# filtered=[plane for plane in specificAirplanecapacity if plane.lower() == "abebe"]
			
			lists=[]
			
			# def filtered(cls,plane,namee):
			# 	return [plane for plane in specificAirplanecapacity if specificAirplanecapacity.airplane]
			# 	pass
			
          
            
			for x in specificAirplanecapacity:
				newfield=x["airplane"]
				lists.append(newfield)
				
			fillterd=[plane for plane in lists if plane == "Airbus001"]

			if dd-1<len(fillterd):
				frappe.frappe.throw("There is no Availabel seats")
            
				
				
			# newfield=specificAirplanecapacity[0]['airplane']
			


			
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
			
          
			# self.seat=seat
			
			print("Here is the the capacity of airplane Airbus001: ",dd)
			print("Here is the total number of ticket before: ",len(total_ticket))
			print("Here is the total number of ticket of Airbus001-05-04-0009 before: ",len(total_airbus_ticket))
			print("Here is specefice airplane from other doctype ",len(fillterd))
			
			

  
	
	
	
        
	
	
      
	
	
	
	
			

  
			

      
			
      
			

 
	



























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

    


