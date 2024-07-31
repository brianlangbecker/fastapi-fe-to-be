from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

def setup_tracer(app):
    resource = Resource(attributes={
        "service.name": "backend-service",
        "deployment.environment": "production"
    })
    trace.set_tracer_provider(TracerProvider(resource=resource))
    tracer_provider = trace.get_tracer_provider()

    # Configure the OTLP exporter
    otlp_exporter = OTLPSpanExporter(
        endpoint="https://api.honeycomb.io:443",
        headers={"x-honeycomb-team": "YOUR_HONEYCOMB_API_KEY"},
    )
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)
