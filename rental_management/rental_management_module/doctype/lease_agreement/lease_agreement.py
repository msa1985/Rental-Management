# Copyright (c) 2024, Muhannad Saleh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests


class LeaseAgreement(Document):
	def before_save(self):
		pass
	
	def validate(self):
		if self.lease_start_date > self.lease_end_date:
			frappe.throw("Sorry Lease End Date Cant Be Before Lease Start Date")
	
	def before_submit(self):
		pass
	
	def after_insert(self):
		invoice = frappe.get_doc({"doctype":"Sales Invoice",
							"customer":self.customer,
							"due_date":self.lease_start_date,
							"custom_lease_agreement":self.name,
							"items":[{"item_code":self.vehicle,
										"item_name":self.vehicle,
										"qty":1,
										"rate": self.rental_rate,}]})

		invoice.insert(ignore_permissions=True)
		invoice.submit()
		self.db_set('sales_invoice', invoice.name)

		rental_vehicle = frappe.get_doc("Vehicles", self.vehicle)
		rental_vehicle.status = "Rented"
		rental_vehicle.save(ignore_permissions=True)

		
	
	def on_update(self):
		pass
	
	def on_cancel(self):
		rental_vehicle = frappe.get_doc("Vehicles", self.vehicle)
		rental_vehicle.status = "Available"
		rental_vehicle.save(ignore_permissions=True)
	
	def on_trash(self):
		pass

@frappe.whitelist()
def get_bitcoin_data():
    try:
        api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(api_url).json()
        return response
    except Exception as e:
        pass
