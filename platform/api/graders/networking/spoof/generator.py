from os import path

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    rendered_template_path = path.join(generator_path, "udpclient")


    homepage_link = autogen_tools.generate_resource_link(pid, "udpclient", title="client")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "udpclient"),
            ],
        },
        "static_files": {
        },
        "problem_updates": {
            "description": "NSA has their network firewalled for only their own employees. We got intel that one of their secret servers is at 172.27.36.28:5005. Also our monkeys got hold of the following %s. Can you get any useful intel?" % homepage_link
        }
    }
