from os import path
from hashlib import sha1

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    template_path = path.join(generator_path, "file_generator.py")
    out_template_path = path.join(generator_path, "file_generated.py")
    rendered_template_path = path.join(generator_path, "encrypted.txt")

    key = "aad7imfd6bl0ab68sb67vk"
    flag = "cs628a{" + sha1((str(n) + key).encode('utf-8')).hexdigest()[:22]+"}"

    autogen_tools.replace_source_tokens(
        template_path,
        {"flag": flag},
        out_template_path
    )
    autogen_tools.run_makefile(generator_path)

    homepage_link = autogen_tools.generate_resource_link(pid, "encrypted.txt", title="encrypted file")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "encrypted.txt"),
            ],
        },
        "static_files": {
        },
        "problem_updates": {
            "description": "Can you construct the flag from these encrypted lines of text messages with the information you already know ? I promise its not going to be difficult a problem for you as everything you need to know is in the description :P Get the file here: %s" % homepage_link
        }
    }
