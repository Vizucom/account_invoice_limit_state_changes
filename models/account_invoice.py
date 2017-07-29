# -*- encoding: utf-8 -*-
from openerp.osv import fields, osv
from openerp.tools.translate import _
from datetime import datetime
from dateutil.relativedelta import relativedelta


class AccountInvoice(osv.osv):

    _inherit = "account.invoice"

    def write(self, cr, uid, ids, vals, context=None):
        '''If the invoice's state is being changed to Open or Cancelled, check the dates 
        whether it should be permitted '''
        if not context:
            context = {}

        res = super(AccountInvoice, self).write(cr, uid, ids, vals, context)

        ir_config_model = self.pool.get('ir.config_parameter')
        last_allowed_edit_day = ir_config_model.get_param(cr, uid, 'account_invoice_limit_state_changes.last_edit_day_in_month')

        if not last_allowed_edit_day:
            # System parameter not set, skip the check
            return res
        
        try:
            last_allowed_edit_day = int(last_allowed_edit_day)
        except ValueError:
            raise osv.except_osv(_('Error'), _('Could not check dates, system parameter "account_invoice_limit_state_changes.last_edit_day_in_month" should be an integer.'))

        if 'state' in vals and vals['state'] in ['cancel', 'open'] and int(last_allowed_edit_day) > 0:
            for invoice in self.browse(cr, uid, ids, context):                

                today = datetime.today()
                current_day_of_month = today.day

                if current_day_of_month > last_allowed_edit_day:
                    # Only invoices from this month's first day can have their states changed
                    first_allowed_edit_date = today.replace(day=1).date()
                else:
                    # Invoices from previous month's first day onwards can have their states changed
                    first_allowed_edit_date = today.replace(day=1).date() - relativedelta(months=1)

                invoice_date = datetime.strptime(invoice.date_invoice, '%Y-%m-%d').date()
                if invoice_date < first_allowed_edit_date:
                    raise osv.except_osv(_('Error'), _('Invoices with invoice date earlier than {} cannot be validated or cancelled anymore.').format(first_allowed_edit_date.strftime('%d.%m.%Y')))

        return res