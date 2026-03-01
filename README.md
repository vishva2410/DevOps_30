# 30 Days of DevOps Learning Journey

Welcome to the **30 Days of DevOps** repository! This project is a curated collection of simple, hands-on DevOps projects designed to help you learn the fundamentals of containerization, CI/CD, web servers, and more.

## 🚀 Projects Overview

### 1. Flask Docker Application (`projects/flask-docker-app`)
A simple Python Flask application containerized using Docker.
- **Key Concepts:** Python, Flask, Docker, Port Mapping.
- **How to Run:**
  ```bash
  cd projects/flask-docker-app
  docker build -t flask-app .
  docker run -p 5000:5000 flask-app
  ```

### 2. Nginx Static Web Server (`projects/nginx-web-server`)
Serving a static HTML page using the official Nginx Docker image.
- **Key Concepts:** Nginx, Docker, Static Content, Web Hosting.
- **How to Run:**
  ```bash
  cd projects/nginx-web-server
  docker build -t nginx-web .
  docker run -p 8080:80 nginx-web
  ```

### 3. Age Prediction ML Environment (`projects/age-prediction`)
A containerized environment for training an Age Prediction CNN model.
- **Key Concepts:** Machine Learning, Docker, Python Dependencies, OpenCV.
- **How to Run:**
  ```bash
  cd projects/age-prediction
  docker build -t age-prediction .
  docker run age-prediction
  ```

### 4. GitHub Actions CI Pipeline (`.github/workflows/ci.yml`)
An automated Continuous Integration (CI) pipeline that lints Python code and builds Docker images on every push.
- **Key Concepts:** CI/CD, GitHub Actions, Automated Testing, Docker Build.

---

## 🛠 Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Python 3.x](https://www.python.org/downloads/) for local development.
- A GitHub account to explore Actions.

## 📈 Roadmap
- **Day 1-5:** Docker Fundamentals & Containerizing Web Apps.
- **Day 6-10:** Introduction to CI/CD with GitHub Actions.
- **Day 11-15:** Infrastructure as Code (Coming Soon).
- **Day 16-20:** Monitoring and Logging (Coming Soon).
- **Day 21-30:** Advanced Orchestration with Kubernetes (Coming Soon).

---
*Happy Learning!*
