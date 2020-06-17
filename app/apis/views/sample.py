"""app/apis/views/sample.py
"""
from flask import jsonify

from apis.models import db
from apis.models.t_sample import Sample, upsert_stmt


def handler(header, payload):
    """handler
    """
    statement = header.get('statement')

    if statement == 'STAT_READ_ALL':
        return _read_all()

    if statement == 'STAT_READ_ONE':
        return _read_one(payload=payload)

    if statement == 'STAT_UPSERT':
        return _upsert(payload=payload)

    if statement == 'STAT_UPDATE':
        return _update(payload=payload)

    if statement == 'STAT_DELETE':
        return _delete(payload=payload)

    return jsonify({'message': 'no route matched with those values'}), 200


def _read_all():
    """_read_all
    """
    results = Sample.query.all()
    return jsonify([result.to_dict() for result in results]), 200


def _read_one(payload):
    """_read_one
    """
    record = payload.pop(0)

    result = Sample.query.filter_by(id=record.get('id')).first()
    if result is None:
        return jsonify([]), 200
    return jsonify(result.to_dict()), 200


def _upsert(payload):
    """_upsert
    """
    records = payload

    db.session.execute(clause=upsert_stmt(), params=records)
    db.session.commit()

    response = jsonify(records[-1])
    response.headers['Location'] = \
        '/sample/api?service=SERV_SAMPLE&statement=STAT_READ_ONE&id={}'.format(
            records[-1].get('id'))
    return response, 201


def _update(payload):
    """_update
    """
    record = payload.pop(0)

    result = Sample.query.filter_by(id=record.get('id')).first()
    result.set_attrs(record)

    db.session.commit()

    response = jsonify(None)
    response.headers['Length'] = 0
    return response, 204


def _delete(payload):
    """_delete
    """
    record = payload.pop(0)

    result = Sample.query.filter_by(id=record.get('id')).first()

    db.session.delete(result)
    db.session.commit()

    response = jsonify(None)
    response.headers['Length'] = 0
    return response, 204
