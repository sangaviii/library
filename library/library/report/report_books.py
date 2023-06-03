from odoo import models, fields, api


class ReportBooks(models.AbstractModel):
    _name = 'report.library.report_books'
    _description = 'Report books'

    @api.model
    def _get_report_values(self, docids, data=None):
        books_ids = data['books_ids']
        # docs = self.env['books.books'].browse(books_ids)
        docs = self.env['books.books'].search(
            ['|',('id', 'in', books_ids),
             ('checkin_date', '>=', data['checkin_date']), ('checkout_date', '<=', data['checkout_date'])])
        print('>>>>>>>>>>>>>>>', docs)
        return {
            'doc_ids': docids,
            'doc_model': 'books.books',
            'docs': docs,

        }




    # @api.model
    # def _get_report_values(self, docids, data=None):
    #     books_ids = data['books_ids']
    #     docs = self.env['books.books'].browse(books_ids)
    #     return {
    #         'doc_ids': docids,
    #         'doc_model': 'books.Books',
    #         'docs': docs,
    #     }


