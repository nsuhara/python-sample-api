"""app/apis/views/handler.py
"""
from flask import Blueprint, jsonify, request

from apis.views.sample import handler as sample_handler
from common.utility import err_response

apis = Blueprint(name='apis', import_name=__name__,
                 url_prefix='/sample')


@apis.route('/healthcheck', methods=['GET'])
def healthcheck():
    """healthcheck
    """
    return jsonify({'status': 'healthy'}), 200


@apis.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api():
    """api
    """
    if request.method == 'GET':
        payload = [
            {
                'service': request.args.get('service'),
                'statement': request.args.get('statement')
            },
            {
                'id': request.args.get('id', None)
            }
        ]

    if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
        payload = request.json

    header = payload.pop(0)

    if header.get('service') == 'SERV_SAMPLE':
        return sample_handler(header=header, payload=payload)

    return jsonify({'message': 'no route matched with those values'}), 200


@apis.errorhandler(404)
@apis.errorhandler(500)
def errorhandler(error):
    """errorhandler
    """
    return err_response(error=error), error.code
