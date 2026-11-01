# 🚀 ArgoCD GitOps Demo - Application Source (`argo-demo-app`)

This repository contains the application source code and continuous integration (CI) workflows for the GitOps Portfolio Project. 

## 🏗️ System Architecture
This project utilizes a **decoupled polyrepo architecture** to enforce a strict separation of concerns between application code and deployment configurations:
1. **Developer Push:** Code modifications are pushed to this repository (`argo-demo-app`).
2. **CI Pipeline:** GitHub Actions builds a stateless Docker container tagged with the unique Git Commit SHA.
3. **GitOps Handshake:** The pipeline securely checks out the companion infrastructure repository (`argo-demo-config`) and updates the deployment manifest with the newly generated image tag.

## 🛠️ Tech Stack
* **Language:** Python 3.11 (Stateless HTTP Server)
* **Containerization:** Docker
* **CI Automation:** GitHub Actions

## 💻 Local Development & Testing

To run and test the containerized application locally on your machine:

```bash
# Clone the repository
git clone https://github.com
cd argo-demo-app

# Build the Docker image
docker build -t argo-demo-app:local .

# Run the container locally
docker run -d -p 8080:8080 argo-demo-app:local
```
Once running, navigate to `http://localhost:8080` in your web browser to verify the deployment.

## 🤖 CI/CD Workflow (`.github/workflows/deploy.yml`)
The integrated automated pipeline performs the following tasks on every push to the `main` branch:
* Checks out the latest source code.
* Packages the runtime environment using the local `Dockerfile`.
* Uses a `sed` stream editor to dynamically inject the immutable image tag into the declarative GitOps repo manifests.
* Pushes the atomic configuration update to trigger the Argo CD reconciliation loop.
