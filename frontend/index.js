import { HoneycombWebSDK } from '@honeycombio/opentelemetry-web';
import { getWebAutoInstrumentations } from '@opentelemetry/auto-instrumentations-web';

const configDefaults = {
  ignoreNetworkEvents: true,
};

const sdk = new HoneycombWebSDK({
  debug: true, // Set to false for production environment.
  apiKey: '[YOUR API KEY HERE]', // Replace with your Honeycomb Ingest API Key.
  serviceName: '[YOUR APPLICATION NAME HERE]', // Replace with your application name.
  instrumentations: [getWebAutoInstrumentations({
    '@opentelemetry/instrumentation-xml-http-request': configDefaults,
    '@opentelemetry/instrumentation-fetch': configDefaults,
    '@opentelemetry/instrumentation-document-load': configDefaults,
  })],
});

sdk.start();

document.getElementById('fetch-data').addEventListener('click', async () => {
  const response = await fetch('http://localhost:8000/data');
  const data = await response.json();
  console.log(data);
});
