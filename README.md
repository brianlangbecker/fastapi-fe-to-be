# FastAPI front to backed Example Project

This project demonstrates the use of OpenTelemetry with a FastAPI backend and a JavaScript frontend, sending traces to Honeycomb.

## Setup

### Backend

1. In backend/tracing.py directory update your API Key

   ```python
   headers={"x-honeycomb-team": "YOUR_HONEYCOMB_API_KEY"},
   ```

### FrontEnd

1. In frontend/index.js directory update your API Key

   ```javascript
   apiKey: 'API_KEY_HONEYCOMB', // Replace with your Honeycomb Ingest API Key.
   ```

### Start

1. Make sure to run

   ```bash
   chmod 755 start.sh
   ```

2. To excute, run the below. Note, the first time you do it may take a while to configure the necessary packages

   ```bash
   ./start.sh
   ```
