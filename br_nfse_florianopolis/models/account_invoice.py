# © 2017 Danimar Ribeiro, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models


class AccountInvoice(models.Model):
    _inherit = 'account.move'

    def _return_pdf_invoice(self, doc):
        if doc.model == '012':  # Floripa
            return 'br_nfse_florianopolis.report_br_nfse_danfpse'
        # TODO Implementar ou não?
        return super(AccountInvoice, self)._return_pdf_invoice(doc)
