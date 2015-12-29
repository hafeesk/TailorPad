frappe.ui.form.on('Sales Order', 'refresh', function(frm, cdt, cdn){
  var doc = frm.doc;
  if(!doc.delivery_date){
      frm.set_value('delivery_date', frappe.datetime.nowdate());
  }
})


frappe.ui.form.on('Sales Order Item', 'item_code', function(frm, cdt, cdn){
  var d = locals[cdt][cdn];
  frappe.call({
    method : "tailorpad.custom_folder.custom_selling.get_supplier",
    args : {'item_code': d.item_code},
    freeze: true,
    callback: function(r){
      if(r.message){
        frappe.model.set_value('Sales Order Item', d.name, 'manufacturer_name', r.message.default_supplier);
        frappe.model.set_value('Sales Order Item', d.name, 'warehouse', r.message.default_warehouse);
      }
    }
  });
});


frappe.ui.form.on('Sales Order Item', 'fabric_item_code', function(frm, cdt, cdn){
  var d = locals[cdt][cdn];
  frappe.call({
    method : "tailorpad.custom_folder.custom_selling.get_supplier",
    args : {'item_code': d.fabric_item_code},
    freeze: true,
    callback: function(r){
      if(r.message){
        frappe.model.set_value('Sales Order Item', d.name, 'fabric_supplier', r.message.default_supplier);
        frappe.model.set_value('Sales Order Item', d.name, 'fabric_warehouse', r.message.default_warehouse);
      }
    }
  });
});


cur_frm.fields_dict['items'].grid.get_field("fabric_item_code").get_query = function(doc, cdt, cdn) {
	return {
		query: "tailorpad.custom_folder.custom_selling.get_fabric"
	}
}


cur_frm.cscript.size = function(doc, cdt, cdn){ cur_frm.cscript.get_fabric_qty(doc, cdt, cdn); }

cur_frm.cscript.get_fabric_qty = function(doc, cdt, cdn){
  var d = locals[cdt][cdn];
  if(d.size && d.width)
    frappe.call({
        method: 'tailorpad.custom_folder.custom_selling.get_fabric_qty',
        args: {'parent': d.item_code, 'size': d.size, 'width': d.width},
        freeze: true,
        callback: function(r){
            if(r.message){
              frappe.model.set_value('Sales Order Item', d.name, 'fabric_qty', r.message.fabric_qty)
            }
        }
    });
}
