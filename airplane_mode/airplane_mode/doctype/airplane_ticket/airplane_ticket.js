// Copyright (c) 2025, md and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {

        d = new frappe.ui.Dialog({
            title: 'Enter details',
            fields: [
                {
                    label: 'Seat ',
                    fieldname: 'seat',
                    fieldtype: 'Data',
                    
                },
            ],
            size: 'small', // small, large, extra-large 
            primary_action_label: 'Assing',
            primary_action(values) {
                frm.set_value("seat",values.seat)
                frm.save()
                d.hide();
            }
        });
        


        frm.add_custom_button("Assign Seat",()=>{

            d.show()

            
        },"Action")

        
	},
});
