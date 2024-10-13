# Metabase Postgres Business Intelligence Dashboard

Studies based in day 67-68 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 61–70: Advanced Observability and Analytics

Day 67–68: Implement a business intelligence dashboard using tools like Tableau or Power BI connected to your application databases.

## Project Overview

This project demonstrates the implementation of a Business Intelligence (BI) dashboard using Metabase connected to a PostgreSQL database. The dashboard allows users to explore and visualize data from the PostgreSQL database in real-time.

The main focus is on using open-source BI tools, offering a free and scalable alternative to proprietary solutions like Tableau or Power BI. This solution is containerized using Docker to ensure easy deployment and consistent environments, allowing you to interact with your data directly from a Metabase dashboard.

In this project, I set up the following:

* A PostgreSQL database that holds the application data.
* A FastAPI backend that serves as an example for loading and interacting with data.
* Metabase, an open-source BI tool, for visualizing data through charts and dashboards.
* All components are containerized and orchestrated using Docker Compose, making it easy to run and manage the application in any environment.

The goal of this project is to showcase how to set up and use a BI dashboard for analytics and data visualization in a cloud-native environment, focusing on observability and insights.

## Prerequisites
Ensure you have the following installed:

* Docker
* Docker Compose

## How to Run

Run docker-compose:
```
docker-compose up --build
```

Populate the PostgreSQL Database After setting up the project, you may want to populate the PostgreSQL database with some initial data. Use the following command to run the Python script that inserts sample data:
```
docker exec -it fastapi_app python populate.py
```

## Access the Services

Metabase: Once the services are running, go to ```http://localhost:3000``` to access the Metabase dashboard.

On the first launch, you will be prompted to set up a Metabase account and connect it to the PostgreSQL database (which will already be running as a service).

FastAPI: Visit ```http://localhost:8000``` to access the FastAPI backend. You can interact with your API endpoints or fetch data from the /data endpoint.

## Build Your First Dashboard

After the data is populated, log in to Metabase, and explore your PostgreSQL database.

Create and save queries using the Metabase query editor.

Add these queries to your dashboard and create visualizations such as bar charts, pie charts, or line graphs.

Explore how to improve ```populate.py``` so you can improve dashboard data.


## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the Day 23–24: Automate multi-environment setups using Terraform and Ansible dynamic inventories from the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"