# argo-demo-app
simply python app build into docker image for later K8s ArgoCD demo.

# 🚀 ArgoCD GitOps Portfolio Project

This portfolio project demonstrates a production-grade **Pull-based GitOps pipeline** utilizing decoupled application and configuration repositories.

## 🏗️ Architecture Design
1. **CI Layer:** Developer pushes to `argo-demo-app` ➡️ GitHub Actions builds image tagged with Git Commit SHA.
2. **GitOps Trigger:** GitHub Actions updates the image reference inside the `argo-demo-config` repository.
3. **CD Layer:** Argo CD detects configuration drift ➡️ Reconciles cluster state to match the updated configuration repository state automatically.

## 🛠️ Tech Stack
* **Runtime:** Python 3.11
* **Containerization:** Docker
* **CI Automation:** GitHub Actions
* **Continuous Delivery:** Argo CD
* **Orchestration:** Kubernetes (K8s)
