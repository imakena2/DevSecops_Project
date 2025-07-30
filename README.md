# DevSecOps Project Report

## Project Title: Secure CI/CD Pipeline with Monitoring and Testing

---

## 1. Introduction

**Name**: *Idah Makena Ncooro*
**Institution**: *Strathmore University*
**Project**: *Final DevSecOps Project*

This project represents the final DevSecOps practical assessment, aimed at applying industry best practices in continuous integration, deployment, testing, and monitoring. It showcases a secure, automated CI/CD pipeline for deploying a containerized web application. The implementation integrates tools like Docker, Jenkins, SonarQube, Selenium, and Kubernetes, along with monitoring solutions such as Netdata and AWS CloudWatch. The purpose of this project was not only to deploy and test an application securely but also to gain hands-on experience in managing end-to-end DevSecOps workflows in both local and cloud environments.

---

## 2. Project Objectives

* Automate builds and deployments using Jenkins
* Scan code quality using SonarQube
* Package and serve the application using Docker and Nginx
* Deploy the application via Helm on Kubernetes
* Monitor the deployment using Netdata and CloudWatch
* Perform UI testing using Selenium and Pytest
* Track development progress using Jira
* Ensure secure deployment using SSL certificates and security headers

---

## 3. Environment and Tools Setup

### Development Tools:

* **VS Code**: Primary code editor
* **PowerShell & Git Bash**: CLI tools
* **GitHub**: Version control
* **Jira**: Agile board and issue tracking

### Backend/Infrastructure:

* **Docker Desktop**: Local Kubernetes and Docker support
* **AWS EKS & ECR**: For cloud deployment and container registry
* **Jenkins**: CI/CD orchestration
* **SonarQube**: Static analysis (SAST)
* **Helm**: Kubernetes packaging tool
* **Netdata & AWS CloudWatch**: Monitoring solutions
* **Selenium + Pytest**: UI automation testing

---

## 4. Project Flow

1. **Frontend Development**

   * Created a React project using Vite
   * Styled components using TailwindCSS and shadcn/ui
   * Verified UI using `npm run dev`

2. **Containerization**

   * Created a `Dockerfile` with multi-stage build
   * Final stage uses Nginx to serve the app
   * Configured `.dockerignore`

3. **CI/CD Integration with Jenkins**

   * Jenkins containerized using Docker
   * Installed required plugins (Docker, GitHub, NodeJS)
   * Configured Jenkins pipeline using `Jenkinsfile`
   * Triggered build/test steps on push

4. **Code Quality with SonarQube**

   * Set up SonarQube via Docker
   * Wrote `sonar-project.properties`
   * Scanned project from Jenkins and manually

5. **Helm Chart Creation**

   * Defined Helm charts for deployment and service
   * Set `imagePullPolicy: Never` for local testing
   * Configured values in `values.yaml`

6. **Kubernetes Deployment**

   * Deployed via Helm on Docker Desktop
   * Validated service via NodePort

7. **Monitoring Setup**

   * Initially attempted Prometheus and Grafana
   * Due to local issues, switched to Netdata (via DaemonSet)
   * AWS CloudWatch integrated during EKS deployment

8. **Cloud Deployment via AWS**

   * Created EKS cluster using `eksctl`
   * Pushed image to AWS ECR
   * Configured kubeconfig context with `aws eks`
   * Deployed app via `kubectl apply` and Helm

9. **Security Implementation**

   * Configured SSL certificates (self-signed) in Nginx
   * Added security headers (X-Content-Type, X-Frame-Options)

10. **Selenium UI Testing**

* Developed `test_app.py` using Selenium and Pytest
* Tested title, heading, navbar, and buttons
* Captured screenshots on failure
* Generated coverage reports

11. **Project Management with Jira**

* Tracked tasks, sprints, and progress
* Used Jira boards for visualizing development workflow

---

## 5. Project Structure (VS Code)

```text
DevSecOps_Project/
├── public/
├── src/
├── .gitignore
├── Dockerfile
├── Jenkins/
│   ├── Jenkinsfile
│   └── test_app_pytest.py
├── nginx-service.yaml
├── nginx-deployment.yaml
├── sonar-project.properties
├── test_app.py
├── values.yaml
├── chart/
│   └── templates/
│       ├── deployment.yaml
│       └── service.yaml
├── report.html
└── README.md
```

---

## 6. Challenges and Solutions

| Challenge                      | Solution                                              |
| ------------------------------ | ----------------------------------------------------- |
| Prometheus setup failure       | Switched to Netdata and CloudWatch                    |
| Helm install error (file size) | Used `.helmignore` to exclude large files             |
| AWS CLI auth issue             | Installed AWS CLI and configured IAM roles            |
| Docker image not pulled        | Ensured correct tags and set `imagePullPolicy: Never` |
| Kubernetes TLS timeout         | Restarted Docker Desktop and kubelet                  |

---

## 7. Results

* Successful CI/CD integration using Jenkins
* Static analysis integrated with SonarQube
* Dockerized build verified with Nginx
* Deployed via Helm to Kubernetes
* Monitored via Netdata (local) and CloudWatch (AWS)
* Selenium test suite passed for UI workflows
* SSL enabled and security headers configured
* Tasks tracked using Jira board and issue logs

---

## 8. How to Run Locally

```bash
git clone https://github.com/imakena2/devsecopsproject.git
cd devsecopsproject
npm install
npm run dev
```

To build and run Docker:

```bash
docker build -t devsecops-nginx .
docker run -p 8080:80 devsecops-nginx
```

To deploy via Helm:

```bash
helm install devsecops ./chart --set image.repository=devsecops-nginx,image.tag=latest
```

To run tests:

```bash
pytest test_app.py
```

---

## 9. Conclusion

This project provided a comprehensive experience in implementing DevSecOps principles. Each phase from development to deployment, security, testing, and monitoring was addressed, offering a strong foundation for modern software delivery pipelines. The use of both local and cloud environments illustrated the flexibility and power of containerized DevOps workflows.

---

## 10. Author

**Idah Makena Ncooro**
GitHub: [imakena2](https://github.com/imakena2)

---

## 11. License

MIT License

---

## Appendices (with GitHub Links)

### [Appendix A: Environment & Tools Setup](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/1file%20structure.JPG)

### [Appendix B: App Development & Containerization](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/nginx%20prometheus%20container.JPG)

### [Appendix C: CI/CD with Jenkins](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/Jenkins%20Build.JPG)

### [Appendix D: Code Quality & Testing](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/Selenium%20Report.pdf)

### [Appendix E: Kubernetes Deployment](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/Helm.JPG)

### [Appendix F: Monitoring](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/cloudwatch%20metrics.JPG)

### [Appendix G: Security](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/Trivy.docx)

### [Appendix H: Project Management](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/Jira.JPG)

### [Appendix I: Others (EKS, Grafana, Deployment)](https://github.com/imakena2/DevSecops_Project/blob/main/Snapshots/AWS%20cluster.JPG)
