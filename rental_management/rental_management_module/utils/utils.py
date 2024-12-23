import frappe
from frappe.utils import today

def check_lease_agreements():
    expired_agreements = frappe.get_all("Lease Agreement", filters={
        "lease_end_date": ["<=", today()],
        "status": "Active"
    })
    for agreement in expired_agreements:
        lease = frappe.get_doc("Lease Agreement", agreement.name)
        lease.status = "Completed"
        lease.save()
        
        rental_vehicle = frappe.get_doc("Vehicles", lease.vehicle)
        rental_vehicle.status = "Available"
        rental_vehicle.save(ignore_permissions=True)