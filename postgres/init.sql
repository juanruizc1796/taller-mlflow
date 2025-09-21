CREATE USER mlflow_user WITH PASSWORD 'mlflow_pass';
CREATE DATABASE mlflowdb OWNER mlflow_user;
GRANT ALL PRIVILEGES ON DATABASE mlflowdb TO mlflow_user;
