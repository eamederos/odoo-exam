
from odoo.exceptions import UserError
from odoo import _, fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    show_btn_delete_lines = fields.Boolean(compute='_compute_product_uom_qty_for_btn_delete')

    def action_confirm(self):
        for line in self.order_line:
            if line.product_uom_qty == 0:
                raise UserError(_("It is not possible to confirm an order with no zero quantity of products in any line"))
        return super(SaleOrder, self).action_confirm()

    def action_delete_zero_product_uom_qty_lines(self):
        for line in self.order_line:
            if line.product_uom_qty == 0:
                line.unlink()
        self.show_btn_delete_lines = False

    @api.depends('order_line.product_uom_qty')
    def _compute_product_uom_qty_for_btn_delete(self):
        zero = False
        for line in self.order_line:
            if line.product_uom_qty == 0:
                zero = True
                break
        self.show_btn_delete_lines = True if zero else False






