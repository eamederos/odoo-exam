
from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    found_by = fields.Selection([('third','Third Parties'),('social','Social Networks'),('internet','Internet search')],
                                default='internet', string='Found us by', required=True, help="Indicate how our company was found")







