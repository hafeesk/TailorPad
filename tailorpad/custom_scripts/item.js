frappe.ui.form.on('Item', 'item_naming_series', function(frm, cdt, cdn){
  var doc = frm.doc;
  frm.set_value('naming_series', doc.item_naming_series)
})

frappe.ui.form.on('Item', 'refresh', function(frm, cdt, cdn){
  var doc = frm.doc;
  hide_field('naming_series');

  if(!doc.__islocal){
    hide_field('item_naming_series');
  }

  if(doc.is_stock_item != '1'){
    frm.add_custom_button(__("Make Clubbed Product"), frm.cscript.make_clubbed_product);
  }
})

cur_frm.cscript.make_clubbed_product = function(){
  frappe.model.open_mapped_doc({
    method: "tailorpad.admin.custom_methods.make_clubbed_product",
    frm: cur_frm
  });
}


cur_frm.cscript.measurement_template = function(doc, cdt, cdn){
  frappe.call({
    method: "tailorpad.custom_folder.custom_stock.fetch_measurement",
    args: {'measurement_template': doc.measurement_template},
    freeze: true,
    callback: function(r){
        if(r.message){
          cur_frm.clear_table("measurement_fields");
          $.each(r.message, function(k,v){
            mfs = cur_frm.add_child("measurement_fields");
            mfs.measurement_field = v.measurement_field
            mfs.note = v.note
            mfs.image = v.image
            mfs.image_view = v.image_view
          })
          refresh_field('measurement_fields')
        }
    }
  });
}


cur_frm.cscript.style_template = function(doc, cdt, cdn){
  frappe.call({
    method: "tailorpad.custom_folder.custom_stock.fetch_style",
    args: {'style_template': doc.measurement_template},
    freeze: true,
    callback: function(r){
        if(r.message){
          cur_frm.clear_table("style_fields");
          $.each(r.message, function(k,v){
            mfs = cur_frm.add_child("style_fields");
            mfs.style_field = v.style_field
            mfs.style_name = v.style_name
            mfs.note = v.note
            mfs.image = v.image
            mfs.image_view = v.image_view
          })
          refresh_field('style_fields')
        }
    }
  });
}
