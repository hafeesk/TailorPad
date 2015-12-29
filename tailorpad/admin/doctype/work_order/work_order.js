cur_frm.cscript.import_measurement_from_work_order = function(doc, cdt, cdn){
  get_server_fields('get_measurement_from_wo', '', '', doc, cdt, cdn, 1, function(r){
    refresh_field('measurement_fields')
  })
}

cur_frm.cscript.import_style_from_work_order = function(doc, cdt, cdn){
  get_server_fields('get_style_from_wo', '', '', doc, cdt, cdn, 1, function(r){
    refresh_field('style_fields')
  })
}

cur_frm.fields_dict['import_measurement_from_work_order'].get_query = function(doc, cdt, cdn) {
	return{
    query: "tailorpad.admin.doctype.work_order.work_order.work_orderlink",
    filters:{ 'work_order': doc.name}
	}
}

cur_frm.fields_dict['import_style_from_work_order'].get_query = function(doc, cdt, cdn) {
	return{
    query: "tailorpad.admin.doctype.work_order.work_order.work_orderlink",
    filters:{ 'work_order': doc.name}
	}
}
