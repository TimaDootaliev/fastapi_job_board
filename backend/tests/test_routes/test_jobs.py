import json


def test_create_job(client):
    data = {
        'title': 'SDE super',
        'company': 'Makers',
        'company_url': 'www.makers.com',
        'location': 'Kyrgyzstan',
        'description': 'python',
        'date_posted': '2022-01-01'
    }
    response = client.post("/jobs/create-job/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()['company'] == 'Makers'
    assert response.json()['description'] == 'python'


def test_read_job(client):
    data = {
        'title': 'SDE super',
        'company': 'Makers',
        'company_url': 'www.makers.com',
        'location': 'Kyrgyzstan',
        'description': 'python',
        'date_posted': '2022-01-01'
    }
    response = client.post("/jobs/create-job/", json.dumps(data))

    response = client.get("/jobs/get/1")
    assert response.status_code == 200
    assert response.json()['title'] == 'SDE super'