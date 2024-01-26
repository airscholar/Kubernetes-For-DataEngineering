# Kubernetes for Data Engineering

This repository contains the necessary configuration files and DAGs (Directed Acyclic Graphs) for setting up a robust data engineering environment using Kubernetes and Apache Airflow. It includes the setup for the Kubernetes Dashboard, which provides a user-friendly web interface for managing Kubernetes clusters, and Apache Airflow, a platform to programmatically author, schedule, and monitor workflows.

## Repository Structure

The repository is organized as follows:

```
.
├── dags
│   ├── fetch_and_preview.py
│   └── hello.py
└── k8s
    ├── dashboard-adminuser.yaml
    ├── dashboard-clusterrole.yaml
    ├── dashboard-secret.yaml
    ├── recommended-dashboard.yaml
    └── values.yaml
```

### DAGs

- `fetch_and_preview.py`: A DAG for fetching data and providing a preview.
- `hello.py`: A simple example DAG to demonstrate basic Airflow concepts.

### Kubernetes (k8s) Configuration

- `dashboard-adminuser.yaml`: YAML file for setting up an admin user for the Kubernetes Dashboard.
- `dashboard-clusterrole.yaml`: YAML file defining the cluster role for the Kubernetes Dashboard.
- `dashboard-secret.yaml`: YAML file for managing secrets used by the Kubernetes Dashboard.
- `recommended-dashboard.yaml`: YAML file for deploying the recommended Kubernetes Dashboard setup.
- `values.yaml`: YAML file containing values for customizing the Kubernetes setup.

## Getting Started

### Prerequisites

- A Kubernetes cluster
- `kubectl` installed and configured
- Helm (optional, but recommended for managing Kubernetes applications)

### Setup

1. **Deploy the Kubernetes Dashboard:**

   To deploy the Kubernetes Dashboard, apply the YAML files in the `k8s` directory:

   ```bash
   kubectl apply -f k8s/
   ```

   This will set up the Kubernetes Dashboard with the necessary roles and permissions.

2. **Accessing the Kubernetes Dashboard:**

   To access the Dashboard, you may need to start a proxy server:

   ```bash
   kubectl proxy
   ```

   Then, access the Dashboard at: `http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/`.

   Use the token generated for the admin user to log in (see `dashboard-secret.yaml`).

3. **Deploy Apache Airflow:**

   You can deploy Apache Airflow using Helm or by applying custom YAML files. For Helm:

   ```bash
   helm repo add apache-airflow https://airflow.apache.org
   helm install airflow apache-airflow/airflow -f k8s/values.yaml
   ```

   This will deploy Airflow with the settings defined in `values.yaml`.

4. **Adding DAGs to Airflow:**

   Copy your DAG files (e.g., `fetch_and_preview.py`, `hello.py`) into the DAGs folder of your Airflow deployment. The method of copying depends on your Airflow setup (e.g., using Persistent Volume, Git-sync).

### Usage

- **Kubernetes Dashboard:** Use the Dashboard to monitor and manage the Kubernetes cluster.
- **Apache Airflow:** Access the Airflow web UI to manage, schedule, and monitor workflows.

## Video
For a complete walkthrough and practical demonstration, check out the video here: 
[![Kubernetes for Modern Data Engineering](https://img.youtube.com/vi/ISftrpAImHA/0.jpg)](https://youtu.be/ISftrpAImHA)

