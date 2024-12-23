# Copyright (c) 2024, Muhannad Saleh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Vehicles(Document):
	def before_save(self):
		pass
	
	def validate(self):
		pass
	
	def before_submit(self):
		pass
	
	def after_insert(self):
		try:
			item_group = frappe.db.exists("Item Group","Vehicles")
			if item_group == None:
				create_item_group = frappe.get_doc({"doctype":"Item Group",
										"item_group_name":"Vehicles"})
				create_item_group.insert()
		except Exception as e:
			raise e
		try:
			item = frappe.get_doc({"doctype":"Item",
							"item_code":self.vehicle_name,
							"item_group":"Vehicles",
							"stock_uom":"Nos"})

			item.insert(ignore_permissions=True)
			item.submit()
		except Exception as e:
			frappe.logger().error(f"Error while creating vehicle: {str(e)}")
			frappe.throw(f"Failed to create vehicle: {str(e)}")
	
	def on_update(self):
		pass
	
	def on_cancel(self):
		pass
	
	def on_trash(self):
		pass
