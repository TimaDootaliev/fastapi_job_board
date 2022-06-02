# To set this project up:

```

git clone git@github.com:TimaDootaliev/jobs_fastapi_t.git

cd jobs_fastapi_t

python3 -m venv <virtual_environment_name>

. venv/bin/activate - linux
. venv/Scripts/activate - Windows

pip install -r requirements.txt

cd backends/

uvicorn main:app <some_options(--reload)>

```