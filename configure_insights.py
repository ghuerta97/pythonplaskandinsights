from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
import logging

def configure_insights(app, instrumentation_key):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = AzureLogHandler(
        connection_string=f'InstrumentationKey={instrumentation_key}')
    logger.addHandler(handler)

    middleware = FlaskMiddleware(
        app,
        exporter=AzureExporter(
            connection_string=f'InstrumentationKey={instrumentation_key}'
        ),
        sampler=ProbabilitySampler(rate=1.0)
    )

    return logger

