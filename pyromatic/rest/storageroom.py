import logging
import json
from pyramid.view import view_config
from pyramid.response import Response

from pyromatic.use_cases import request_objects as req
from pyromatic.shared import response_object as res
from pyromatic.repository import memrepo as mr
from pyromatic.use_cases import storageroom_use_cases as uc
from pyromatic.serializers import storageroom_serializer as ser

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

storageroom1 = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': '-0.09998975',
    'latitude': '51.75436293',
}

storageroom2 = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': '0.18228006',
    'latitude': '51.74640997',
}

storageroom3 = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': '0.27891577',
    'latitude': '51.45994069',
}

logger = logging.getLogger(__name__)

@view_config(route_name='storagerooms', request_method='GET', renderer='json')
def storageroom(request):
    logger.info('[CALLED] storagerooms')
    qrystr_params = {
        'filters': {},
    }

    logger.info('[CALLED] storagerooms/')
    for arg, values in request.params.items():
        if arg.startswith('filter_'):
            logger.info('[FILTERING] {} : {}'.format(arg, values))
            qrystr_params['filters'][arg.replace('filter_', '')] = values

    request_object = req.StorageRoomListRequestObject.from_dict(qrystr_params)

    repo = mr.MemRepo([storageroom1, storageroom2, storageroom3])
    use_case = uc.StorageRoomListUseCase(repo)

    response = use_case.execute(request_object)

    logger.info('[RESPONSE:VALUE]: {}'.format(response.value))
    logger.info('[RESPONSE:TYPE]: {}'.format(response.type))

    try:
        logger.info('[RESPONSE:OBJ]')
        resp = Response(json=response.value,
                        content_type='application/json',
                        status=STATUS_CODES[response.type])
    except Exception as exc:
        logger.info('[EXCEPTION]: {} : {}'.format(exc.__class__.__name__, exc))
        resp = None

    return resp
