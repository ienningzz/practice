from flask import render_template, request, jsonify
from . import main


@main.app_errorhandler(400)
def not_found(error):
    return render_template('400.html'), 400

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500