from os import path
from hashlib import sha1

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    rendered_template_path = path.join(generator_path, "keyp.pcapng")


    homepage_link = autogen_tools.generate_resource_link(pid, "keyp.pcapng", title="usb")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "keyp.pcapng"),
            ],
        },
        "static_files": {
        },
        "problem_updates": {
            "description": "We intercepted this usb traffic from a high secure machine. Can you get anything interesting? The usb file is here: %s" % homepage_link
        }
    }
