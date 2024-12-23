// Copyright (c) 2024, Muhannad Saleh and contributors
// For license information, please see license.txt

frappe.ui.form.on("Lease Agreement", {
	refresh: function (frm) {
        if (frm.doc.sales_invoice) {
            frm.add_custom_button(__('Pay Invoice'), function () {
                if (!frm.doc.customer) {
                    frappe.msgprint(__('Customer is not defined for this Lease Agreement.'));
                    return;
                }
                frappe.model.with_doctype('Payment Entry', function () {
                    let payment_entry = frappe.model.get_new_doc('Payment Entry');
                    payment_entry.payment_type = 'Receive';
                    payment_entry.party_type = 'Customer';
                    payment_entry.party = frm.doc.customer;
                    payment_entry.mode_of_payment = 'cash';
                    payment_entry.paid_amount = frm.doc.rental_rate;

                    payment_entry.references = [{
                        reference_doctype: 'Sales Invoice',
                        reference_name: frm.doc.sales_invoice,
                        total_amount: frm.doc.rental_rate || 0,
                        allocated_amount: frm.doc.rental_rate || 0
                    }];

                    frappe.set_route('Form', 'Payment Entry', payment_entry.name).then(() => {
                        cur_frm.set_value('payment_type', 'Receive');
                        cur_frm.set_value('party_type', 'Customer');
                        cur_frm.set_value('party', frm.doc.customer);
                        cur_frm.refresh_field('references',payment_entry.references = [{
                            reference_doctype: 'Sales Invoice',
                            reference_name: frm.doc.sales_invoice,
                            total_amount: frm.doc.rental_rate || 0,
                            allocated_amount: frm.doc.rental_rate || 0
                        }]);
                    });
                });
            },// __('Actions')
        );
        }
    },
    validate: function(frm) {
        
    },
    
    onload: function (frm) {
        frm.set_query('vehicle', function(doc) {
            return {
                filters: {
                    status: "Available",
                },
            };
        });
    },
    
    lease_end_date: function (frm) {
    
    },
    after_save: function (frm) {

    },

    on_submit: function (frm) {
        
    },


});
