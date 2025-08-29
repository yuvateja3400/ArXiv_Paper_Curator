# Airflow Configuration

This directory contains Apache Airflow configuration and DAGs for the arXiv Paper Curator project.

## Week 1 Setup

For Week 1, we have a basic setup with:

- **hello_world_dag.py**: Simple test DAG to verify Airflow is working
- **init-db.sql**: Database initialization script

## Directory Structure

```
airflow/
├── README.md           # This file
├── init-db.sql         # Database initialization
└── dags/
    └── hello_world_dag.py  # Test DAG for Week 1
```

## Usage

The Airflow service is configured to run via Docker Compose and can be accessed at:
- Web UI: http://localhost:8080
- Default credentials: admin/[auto-generated password]

## Future Weeks

In later weeks, this directory will contain:
- arXiv paper fetching DAGs
- PDF processing workflows
- Data pipeline orchestration