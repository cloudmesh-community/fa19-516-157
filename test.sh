cms set cloud=aws
pytest tests/cloud

cms set cloud=azure
pytest tests/cloud

cms set cloud=chameleon
pytest tests/cloud
