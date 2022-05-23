import json

from fastapi import status


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


def test_read_all_jobs(client):
    data = {
        'title': 'SDE super',
        'company': 'Google',
        'company_url': 'www.google.com',
        'location': 'Kyrgyzstan',
        'description': 'python',
        'date_posted': '2022-01-01'
    }

    client.post('/jobs/create-job/', json.dumps(data))
    client.post('/jobs/create-job/', json.dumps(data))
    response = client.get('jobs/all')
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        'title': 'New Job super',
        'company': 'doogle',
        'company_url': 'www.doogle.com',
        'location': 'Kyrgyzstan',
        'description': 'fastapi',
        'date_posted': '2022-01-01'
    }
    client.post('/jobs/create-job/', json.dumps(data))
    data['title'] = 'test-job'
    response = client.put('/jobs/update/1', json.dumps(data))
    assert response.json()['msg'] == 'Successfully updated'


def test_delete_a_job(client):
    data = {
        'title': 'New Job super',
        'company': 'doogle',
        'company_url': 'www.doogle.com',
        'location': 'Kyrgyzstan',
        'description': 'fastapi',
        'date_posted': '2022-01-01'
    }
    client.post('/jobs/create-job/', json.dumps(data))
    msg = client.delete('/jobs/delete/1')
    response = client.get('/jobs/get/1')
    assert response.status_code == status.HTTP_404_NOT_FOUND
