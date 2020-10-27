from service import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_app_name(app):
    assert app.name == 'service'

def test_request_returns_404(client):
    assert client.get("/").status_code == 404
