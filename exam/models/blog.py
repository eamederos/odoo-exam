
from odoo import _, api, exceptions, fields, models


class Blogblog(models.Model):
    _inherit = 'blog.blog'

    company_id = fields.Many2one('res.company', string='Company',  default=lambda self: self.env.user.company_id)


class BlogPost(models.Model):
    _inherit = 'blog.post'

    company_id = fields.Many2one('res.company', related='blog_id.company_id')
