from flask import request , jsonify, Response
# from flask_cors import CORS
import sys


import config

config.init()

# CORS(config.APP)

config.LOGGER.info("STARTUP PYTHON TEST SERVICE")


@config.APP.route('/health')
def health():
    config.LOGGER.info("GET /health - received")
    result = { 'result' : 'ok', 'service' : 'python-test-backend' }
    config.LOGGER.info("GET /health - result: {}".format(result['result']))
    return jsonify(result)



@config.APP.route('/exception')
def exception():
    config.LOGGER.info(f'GET /excpetion - received')
    try:
        1/int('a')
    except:
        config.LOGGER.warning('Excpetion 1 - {} - occured'.format(sys.exc_info()[0]))
    try:
        1/int(0)
    except:
        config.LOGGER.warning('Excpetion 2 - {} - occured'.format(sys.exc_info()[0]))
    config.LOGGER.info(f'GET /excpetion - result 500')
    status_code = Response(status=500)
    return status_code

@config.APP.route('/exception1')
def exception1():
    config.LOGGER.info(f'GET /excpetion1 - received')
    raise Exception('This is a sample exception')
    config.LOGGER.info(f'GET /excpetion1 - result 200')
    status_code = Response(status=200)
    return status_code

@config.APP.route('/status_code')
def status_code():
    status = request.args.get('status')
    config.LOGGER.info(f'GET /status_code - received - status: {status}')
    status_code = Response(status=int(status))
    config.LOGGER.info(f'GET /status_code - result {status}')
    return status_code

if __name__ == "__main__":
    from waitress import serve
    config.LOGGER.info("STARTUP PYTHON TEST BACKEND waitress server on port %s ..." % (config.PYTHON_TEST_BACKEND_PORT_DEFAULT))
    serve(config.APP, host="0.0.0.0", port=config.PYTHON_TEST_BACKEND_PORT_DEFAULT, threads=10)