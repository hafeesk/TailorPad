cur_frm.fields_dict['items'].grid.get_field("fabric_item_code").get_query = function(doc, cdt, cdn) {
	return {
		query: "tailorpad.custom_folder.custom_selling.get_fabric"
	}
}

cur_frm.cscript.size = function(doc, cdt, cdn){ cur_frm.cscript.get_fabric_qty(doc, cdt, cdn); }

cur_frm.cscript.get_fabric_qty = function(doc, cdt, cdn){
  var d = locals[cdt][cdn]
  if(d.size && d.width)
    frappe.call({
        method: 'tailorpad.custom_folder.custom_selling.get_fabric_qty',
        args: {'parent': d.item_code, 'size': d.size, 'width': d.width},
        freeze: true,
        callback: function(r){
            if(r.message){
              frappe.model.set_value('Sales Invoice Item', d.name, 'fabric_qty', r.message.fabric_qty)
            }
        }
    })
}
