// Copyright (c) 2024, Muhannad Saleh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicles', {
    refresh: function (frm) {
        if (frm.doc.status === 'Available') {
            frm.add_custom_button(__('Create Lease Agreement'), function () {
                frappe.model.with_doctype('Lease Agreement', function () {
                    let lease_doc = frappe.model.get_new_doc('Lease Agreement');
                    
                    lease_doc.vehicle = frm.doc.name;
                    lease_doc.vehicle_model = frm.doc.model;

                    frappe.set_route('Form', 'Lease Agreement', lease_doc.name);
                });
            }, //__('Actions')
        ); 
        }
    }
});

