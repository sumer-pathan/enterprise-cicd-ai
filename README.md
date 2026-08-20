# Enterprise CI/CD Pipeline with AI Code Review

A production-style CI/CD pipeline for a FastAPI service, featuring automated testing, security scanning, AI-powered code review, and controlled multi-environment deployments.

**Stack:** Python · FastAPI · GitHub Actions · SonarCloud · CodeRabbit · Trivy · Docker · Helm · Kubernetes

---

## Overview

This project simulates a real enterprise deployment workflow, from code push to production release, with quality gates and approval checkpoints at every stage. It's built as a portfolio piece to demonstrate practical DevOps and platform engineering skills: not just running a pipeline, but designing one with security, code quality, and safe rollout in mind.

---

## Architecture

```
Pull Request / Push
        │
        ▼
GitHub Actions CI
  ├── Unit Tests (Pytest)
  ├── Linting (flake8)
  ├── Security Scan (Trivy)
  ├── Code Quality (SonarCloud)
  └── AI Code Review (CodeRabbit)
        │
        ▼
   Docker Build
        │
        ▼
   CD Pipeline
  ├── Dev         → Auto deploy
  ├── Staging     → Manual approval
  └── Production  → Manual approval
```

---

## Key Features

- **Multi-stage CI pipeline** with tests, linting, and security scanning on every push
- **AI code review** via CodeRabbit on all pull requests
- **Static analysis and coverage tracking** with SonarCloud
- **Vulnerability scanning** with Trivy before any image is built
- **Multi-environment CD** across dev, staging, and production
- **Manual approval gates** for staging and production deployments
- **Hardened Docker build**: multi-stage, runs as a non-root user
- **Helm chart** for Kubernetes deployment
- **Cost-controlled**: designed to run within free-tier limits for portfolio use

---

## Project Structure

```
enterprise-cicd-ai/
├── .github/workflows/
│   ├── ci.yaml           # Tests, lint, Trivy scan
│   ├── cd.yaml           # Multi-environment deploy
│   └── sonarcloud.yaml   # Code quality analysis
├── app/                  # FastAPI application
├── tests/                # Unit tests (Pytest)
├── charts/task-api/      # Helm chart for K8s deployment
├── environments/         # Environment-specific configs
├── docs/                 # Additional documentation
├── Dockerfile            # Multi-stage, non-root build
├── requirements.txt
└── README.md
```

---

## Application

A simple Task Management API built with FastAPI, used as the workload running through this pipeline.

- Create, read, update, and delete tasks
- Health check endpoint for monitoring/readiness probes
- Fully containerized and Kubernetes-ready

---

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

---

## CI/CD Pipeline Details

| Stage | Tool | Trigger |
|---|---|---|
| Unit Tests | Pytest | Every push/PR |
| Linting | flake8 | Every push/PR |
| Security Scan | Trivy | Every push/PR |
| Code Quality | SonarCloud | Every push/PR |
| AI Review | CodeRabbit | Every PR |
| Deploy: Dev | GitHub Actions | Auto, on merge to main |
| Deploy: Staging | GitHub Actions | Manual approval |
| Deploy: Production | GitHub Actions | Manual approval |

---

## Author

**Sumer Pathan**
Cloud & DevOps Engineer | Portfolio Project, 2026
