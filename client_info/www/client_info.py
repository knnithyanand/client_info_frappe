from __future__ import unicode_literals
import frappe

sitemap = 1

def get_context(context):
	context.ip_address = "192.168.0.1"
	context.headers = frappe.request.headers
	return context
