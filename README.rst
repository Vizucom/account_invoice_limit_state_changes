.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============================================
State Change Limitations for Customer Invoices
==============================================

Adds a system parameter for setting a date after which old invoices cannot be cancelled or validated

* Intended for situations where invoices get changed after e.g. VAT reporting has already been done and sent out, when the correct procedure would be to do an appropriate refund invoice instead of editing an old one.

Installation
============
* Just install the module from Settings -> Modules

Configuration
=============
* Go to system parameters and set the account_invoice_limit_state_changes.last_edit_day_in_month value to a number between 1-31. The default is 5.
* After that day, the invoices of previous months cannot have their states changed to Open or Cancelled anymore.
* If you want to temporarily disable the functionality, you can set the parameter value to 0

Usage
=====
* Handle invoices as normal. An exception will get thrown if a prohibited state change is attempted

Known issues / Roadmap
======================
* Define group-based access rights so that some users are still allowed to do state changes if absolutely necessary.

Credits
=======

Contributors
------------
* Timo Talvitie <timo@vizucom.com>

Maintainer
----------
.. image:: http://vizucom.com/logo.png
   :alt: Vizucom Oy
   :target: http://www.vizucom.com


This module is maintained by Vizucom Oy