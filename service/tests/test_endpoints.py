import json


def test_post_subject(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'subject': 'dog'
    }
    url = '/api/v1/subject'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 200
    assert response.content_type == mimetype
    assert response.json['msg'] == 'Success'
    assert type(response.json['summary']) == str

def test_post_subject_failed(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'subject': ''
    }
    url = '/api/v1/subject'

    response = client.post(url, data=json.dumps(data), headers=headers)

    assert response.status_code == 500
    assert response.content_type == mimetype
    assert response.json['msg'] == 'Failed'