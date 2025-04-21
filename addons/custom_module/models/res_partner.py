from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def create(self, vals):
        _logger.info('Creating new partner with values: %s', vals)
        partner = super(ResPartner, self).create(vals)
        _logger.info('Partner created successfully with ID: %s', partner.id)
        return partner

    def write(self, vals):
        _logger.info('Updating partner %s with values: %s', self.ids, vals)
        result = super(ResPartner, self).write(vals)
        _logger.info('Partner update completed: %s', result)
        return result 