from django.shortcuts import render

import requests
import json
import environ

env = environ.Env()
environ.Env.read_env()


# Create your views here.

def projects(request):
    url = "https://api.ona.io/api/v1/projects"
    username = env("ONA_USERNAME")
    password = env("ONA_PASSWORD")

    response = requests.get(url, auth=(username, password))
    print(response.status_code)

    my_json_response = response.json()

    list_of_projects = my_json_response
    no_of_projects = len(list_of_projects)

    public_projects = []
    private_projects = []
    favourite_projects = []

    print("MY LIST: ", list_of_projects)
    for item in range(len(list_of_projects)):
        project = list_of_projects[item]

        favourite = project['starred']
        if favourite:
            favourite_projects.append(project)

        status = project['public']
        if status:
            public_projects.append(project)
        else:
            private_projects.append(project)

    # filter response items
    for item in range(no_of_projects):
        project = my_json_response[item]

        if project:
            project_users = project['users']

            for i in range(len(project_users)):
                users = project_users[-1]
                owner = f"{users['first_name']} {users['last_name']}"

        no_of_public_projects = len(public_projects)
        no_of_private_projects = len(private_projects)
        no_of_favourite_projects = len(favourite_projects)

    context = {
        'list_of_projects': list_of_projects,
        'project_owner': owner,
        'no_of_projects': no_of_projects,
        'no_of_public_projects': no_of_public_projects,
        'no_of_private_projects': no_of_private_projects,
        'no_of_favourite_projects': no_of_favourite_projects,
    }
    return render(request, 'dashboard/projects.html', context)


def project_detail(request, pk):
    context = {}
    return render(request, 'dashboard/project.html', context)

