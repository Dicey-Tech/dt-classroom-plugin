from glob import glob
import os
import pkg_resources

from .__about__ import __version__

templates = pkg_resources.resource_filename(
    "classroom_plugin", "templates"
)

config = {
    "add": {
        "MYSQL_PASSWORD": "{{ 8|random_string }}",
        "SECRET_KEY": "{{ 24|random_string }}",
        "OAUTH2_SECRET": "{{ 24|random_string }}",
    },
    "defaults": {
        "VERSION": __version__,
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}diceytech/dt-classroom:{{ CLASSROOM_VERSION }}",
        "HOST": "classroom.{{ LMS_HOST }}",
        "MYSQL_DATABASE": "classroom",
        "MYSQL_USERNAME": "classroom",
    },
}

hooks = {
    "build-image": {"classroom": "{{ CLASSROOM_DOCKER_IMAGE }}"},
    "init": ["classroom"],
}


def patches():
    all_patches = {}
    patches_dir = pkg_resources.resource_filename(
        "classroom_plugin", "patches"
    )
    for path in glob(os.path.join(patches_dir, "*")):
        with open(path) as patch_file:
            name = os.path.basename(path)
            content = patch_file.read()
            all_patches[name] = content
    return all_patches
