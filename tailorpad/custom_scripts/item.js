frappe.ui.form.on('Item', 'item_naming_series', function(frm, cdt, cdn){
  var doc = frm.doc;
  frm.set_value('naming_series', doc.item_naming_series)
})

frappe.ui.form.on('Item', 'refresh', function(frm, cdt, cdn){
  var doc = frm.doc;
  hide_field('naming_series')

  if(!doc.__islocal){
    hide_field('item_naming_series')
  }

  if(doc.is_stock_item != '1'){
    frm.add_custom_button(__("Make Clubbed Product"), frm.cscript.make_clubbed_product)
  }
})

cur_frm.cscript.make_clubbed_product = function(){
  frappe.model.open_mapped_doc({
    method: "tailorpad.admin.custom_methods.make_clubbed_product",
    frm: cur_frm
  })
}
