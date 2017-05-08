from os import path
from hashlib import sha1

def generate(random, pid, autogen_tools, n):
    """
    Generate an instance of the problem
    Needs to return a list of files to copy to particular instance.
    """

    #Get a random build path
    generator_path = autogen_tools.get_directory(__file__)

    template_path = path.join(generator_path, "flag.c")
    question_path = path.join(generator_path, "encrypt.py")
    out_template_path = path.join(generator_path, "flag_gen.c")
    rendered_template_path = path.join(generator_path, "encrypted.out")

    key = "jfryabsdhii753hyaf68db6"
    flag = "cs628a{" + sha1((str(n) + key).encode('utf-8')).hexdigest()[:22]+"}"

    autogen_tools.replace_source_tokens(
        template_path,
        {"flag": flag},
        out_template_path
    )
    autogen_tools.run_makefile(generator_path)

    homepage_link = autogen_tools.generate_resource_link(pid, "encrypted.out", title="encrypted head")

    return {
        "resource_files": {
            "public": [
                (rendered_template_path, "encrypted.out"),
            ],
        },
        "static_files": {
            "public": [
                (question_path, "encrypt.py"),
            ],
        },
        "problem_updates": {
            "description": "Try to get the the flag from the binary file which is encrypted using the script provided to you. Remember there are some things which always remains same :D Get the file here: {}. The NSA just found the following file which may help <a href='problem-static/crypto/cmh/encrypt.py'>encrypt.py</a>".format(homepage_link)
        }
    }
