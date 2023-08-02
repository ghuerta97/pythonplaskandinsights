from opencensus.ext.azure import exceptions
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
import logging

def configure_insights(app, instrumentation_key):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = AzureLogHandler(
        connection_string=f'InstrumentationKey={instrumentation_key}')
    logger.addHandler(handler)

    try:
        middleware = FlaskMiddleware(
            app,
            exporter=handler,
            blacklist_paths=['/healthcheck']
        )
    except exceptions.TransportError:
        pass

    return logger