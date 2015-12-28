frappe.ui.form.on('Measurement Fields', 'image', function(frm, cdt, cdn){
  var d = locals[cdt][cdn]
  refresh_field('image_view', d.name, 'measurement_fields')
})
