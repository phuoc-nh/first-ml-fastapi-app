An example app that shows how to build a ML app with FastAPI and Docker.

The starter file is model_starter.py with a model from Hugging Face: https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

The final app is in main.py and final model code is in model.py.

## Get started
- Refer to `./requirements.txt` to install required libraries.
- Run `uvicorn 'main:app' --port=8000` to start app
- Go to `localhost:8000/docs` to try APIs out

## Examples usage of /ask api
file: cats.jpeg
text: How many cats are there?

file: tiger.jpeg
text: What's the animal doing?

file: palace.jpeg
text: What is on top of the building?

## Docker
- Run `docker init` to generate python template dockerfile, basically this file is good to build image already
- Run `docker build -t thecoffeeguy/mlfastapiapp:latest .` to create image
- Push to docker hub `docker push hecoffeeguy/mlfastapiapp:latest`

## Deploy to K8S
- Install [Rancher Desktop](https://rancherdesktop.io/), which offers a lightweight k8s cluster powered by [k3s](https://k3s.io/)
- Deploy pod `kubectl run first-fastapi --image=thecoffeeguy/mlfastapiapp:latest --image-pull-policy=Never --port=8000`
- Forward port in pod to local env `kubectl port-forward pods/first-fastapi 8000:8000`



# ML App with FastAPI and Docker

This project demonstrates how to build a machine learning application using FastAPI, Docker, and a pre-trained model from Hugging Face. The app takes an image and a question about the image, then responds with an answer using a Vision-and-Language Transformer (ViLT) model from Hugging Face.

The starter file is `model_starter.py`, and it utilizes the model available at: [ViLT-b32-finetuned-VQA](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa). The final application code is in `main.py`, and the refined model code can be found in `model.py`.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Usage](#usage)
3. [Dockerization](#dockerization)
4. [Kubernetes Deployment](#kubernetes-deployment)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Docker
- Kubernetes (Rancher Desktop for local deployment)

### Install Dependencies
Install Dependencies
```
pip install -r requirements.txt
```

### Running the App

```
uvicorn main:app --port=8000
```

This command will launch the application on localhost:8000. To interact with the API, navigate to http://localhost:8000/docs

### Example Requests

1. **Image**: cats.jpeg
**Text**: "How many cats are there?"

2. **Image**: tiger.jpeg
**Text**: "What's the animal doing?"

3. **Image**: palace.jpeg
**Text**: "What is on top of the building?"


### Dockerization
1.**Initialize Dockerfile**:

To generate a basic Python Dockerfile template
```
docker init
```
It generally includes instructions to:

- Use an official Python base image (python:3.8-slim).
- Copy the project files.
- Install required dependencies.
- Expose the application port.

2.**Build the Docker Image:**

```
docker build -t thecoffeeguy/mlfastapiapp:latest .
```


3.**Push the Image to Docker Hub**
```
docker push thecoffeeguy/mlfastapiapp:latest
```

### Kubernetes Deployment
To run the application on Kubernetes, use Rancher Desktop, which provides an easy way to deploy a lightweight Kubernetes cluster using [k3s](https://k3s.io/).

1.**Install Rancher Desktop:**

Download and install [Rancher Desktop](https://rancherdesktop.io/).

2.**Start the Kubernetes Cluster**

Rancher Desktop will set up `k3s`, a lightweight Kubernetes distribution.

### Deploying the Application

1.**Deploy the pod**
```
kubectl run first-fastapi --image=thecoffeeguy/mlfastapiapp:latest --image-pull-policy=Never --port=8000
```
2.**Forward the Port**
```
kubectl port-forward pods/first-fastapi 8000:8000
```