import os
import pytest

@pytest.mark.skipif(os.getenv("CI") == 'true', reason="Not running in CI")
def test_swagger(client):
    assert client.get('/swagger.json').status_code == 200

@pytest.mark.skipif(os.getenv("CI") == 'true', reason="Not running in CI")
def test_api_documentation(client):
    assert client.get('/docs').status_code == 301
