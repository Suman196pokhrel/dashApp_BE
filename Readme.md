# ![dashApp_BE Logo](https://img.shields.io/badge/dashApp_BE-Backend-blue?style=for-the-badge) - Backend for dashApp Fullstack Web Application

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/downloads/release/python-380/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.101%2B-blue?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-20.10%2B-blue?logo=docker)](https://www.docker.com/)
[![DigitalOcean](https://img.shields.io/badge/DigitalOcean-Droplet-blueviolet?logo=digitalocean)](https://www.digitalocean.com/)

Welcome to the `dashApp_BE` repository – the backend component of the comprehensive dashApp Fullstack Web Application.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)

## Overview

`dashApp_BE` is the backend part of the larger project, `dashApp`, which constitutes a fullstack web application designed to streamline and enhance user interactions. This backend is built using Python's FastAPI framework, utilizing PostgreSQL and pgAdmin 4 for robust database management. SQLAlchemy acts as the bridge between Python and PostgreSQL, providing efficient communication. The project also employs Alembic for seamless database migrations.

## Features

#### Authentication

- User registration and login functionalities.
- JWT token-based authentication for secure interactions.
- Forgot password endpoint with OTP sent to the user's email.
- Data validation using Python class schemas with [Pydantic](https://pydantic-docs.helpmanual.io/) library.

## Technologies Used

- [Python](https://www.python.org/) - Programming language
- [FastAPI](https://fastapi.tiangolo.com/) - Web framework for building APIs with Python 3.8+
- [PostgreSQL](https://www.postgresql.org/) - Powerful, open source object-relational database system
- [pgAdmin 4](https://www.pgadmin.org/) - Open source administration and management platform for PostgreSQL
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and Object-Relational Mapping (ORM) library
- [Alembic](https://alembic.sqlalchemy.org/) - Database migration tool for SQLAlchemy
- [Docker](https://www.docker.com/) - Containerization platform for packaging, distributing, and running applications
- [DigitalOcean](https://www.digitalocean.com/) - Cloud infrastructure provider for hosting

## Deployment

This project is containerized using Docker and Docker Compose for easy deployment. It is hosted on a DigitalOcean Droplet running the Linux Ubuntu distribution.
