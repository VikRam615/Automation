**Table of Contents**

-   [[Requirements]{.underline}](#requirements)

-   [[Setup]{.underline}](#setup)

-   [[Deployment]{.underline}](#deployment)

-   [[Testing]{.underline}](#testing)

-   [[Github Repo]{.underline}](#Github)


**Requirements**

-   Docker

-   Minikube

-   Python 3 and above

-   Nosetest for running tests

**Setup**

1.  **Clone the Repository:**

> git clone https://github.com/Vengatesh-m/qa-test.git


2.  **Create a Virtual Environment (optional):**

> python -m venv myenv
>
> source myenv/bin/activate 
> \`myenv\\Scripts\\activate\`

3.  **Install Dependencies:**


**Deployment**

1.  **Start Minikube:**

> minikube start \--driver=docker

2.  **Deploy Backend:**

> kubectl apply -f backend-deployment.yaml

3.  **Deploy Frontend:**

> kubectl apply -f frontend-deployment.yaml

4.  **Access Frontend Service:** To access the frontend service, run:

> minikube service frontend-service \--url

**Testing**

To run the automated tests, execute the following command:

python test_script.py

**Test Scenarios**

-   Basic connectivity tests between frontend and backend

-   Invalid backend URL handling

-   Empty response handling

-   Data validation and edge cases

**Github Repo -** **https://github.com/VikRam615/Automation.git**
