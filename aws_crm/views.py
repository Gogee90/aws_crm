from django.shortcuts import render, redirect
import boto3
from .forms import CreatEnvForm, CreateAppForm, LoginForm
from django.contrib.auth import authenticate, login


session = boto3.Session(profile_name='eb-cli')
client = session.client('elasticbeanstalk', 'eu-central-1')
# Create your views here.
def create_environment(request):
    form = CreatEnvForm(request.POST)
    if form.is_valid():
        app_name = request.POST['app_name']
        cname_prefix = form.cleaned_data['cname_prefix']
        env_name = form.cleaned_data['env_name']
        solution_stack = request.POST['solution_stack']
        response = client.create_environment(
          ApplicationName=app_name,
          CNAMEPrefix=cname_prefix,
          EnvironmentName=env_name,
          SolutionStackName=solution_stack,
          OptionSettings=[
            {
              'Namespace': 'aws:autoscaling:launchconfiguration',
              'OptionName': 'IamInstanceProfile',
              'Value': 'aws-elasticbeanstalk-ec2-role'
            }

          ],
        )
        return redirect(to='get_all_envs')
    else:
        form = CreatEnvForm()
    stacks = client.list_available_solution_stacks()
    apllications = client.describe_applications()
    return render(request, 'create_environment.html', {
        'form': form,
        'stacks': stacks,
        'applications': apllications
        }
    )


def update_env(request):
    response = client.update_environment(
        EnvironmentName='wordpress-test-env',
        VersionLabel='v1.2',
    )

    print(response)


def create_application(request):
    form = CreateAppForm(request.POST)
    if form.is_valid():
        app_name = form.cleaned_data['app_name']
        description = form.cleaned_data['description']
        response = client.create_application(
            ApplicationName=app_name,
            Description=description,
        )
        print(response)
        return redirect(to='create_environment')
    else:
        form = CreateAppForm()
    return render(request, 'create_application.html', {'form': form})


def update_application(request):
    response = client.create_application_version(
        ApplicationName='wp-test-app',
        AutoCreateApplication=True,
        Description='my-app-v1',
        Process=True,
        SourceBundle={
            'S3Bucket': 'elasticbeanstalk-eu-central-1-225882122082',
            'S3Key': 'Simple-django-based-CRM/wordpress.zip',
        },
        VersionLabel='v1.3',
    )
    client.update_environment(
        EnvironmentName='wordpress-test-env',
        VersionLabel='v1.3',
    )

    print(response)


def get_all_envs(request):
    response = client.describe_environments()
    session = boto3.Session(profile_name='eb-cli')
    bucket = session.client('s3', 'eu-central-1')
    buckets_content = bucket.list_objects(
        Bucket='elasticbeanstalk-eu-central-1-225882122082',
    )

    print(buckets_content)
    context = {
      'responses': response
    }
    return render(request, 'envs1.html', context)



def retrieve_single_env(request, id):
    response = client.describe_environments(
        EnvironmentIds=[
            id,
        ]
    )
    return render(request, 'single_env.html', {'responses': response})


def restart_server(request, id):
    response = client.restart_app_server(
        EnvironmentId = id
    )
    return redirect(to='retrieve_single_env', id=id)


def terminate_env(request, id):
    response = client.terminate_environment(
        EnvironmentId=id,
    )
    return redirect(to='retrieve_single_env', id=id)


def login_user(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            return redirect(to='get_all_envs')
        if user is not None and not user.is_staff:
            return redirect(to='get_all_envs')
        else:
            return redirect(to='login')
    return render(request, "login.html", {
        'form': form
    })