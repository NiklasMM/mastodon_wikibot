import getpass
import os
import string
import subprocess

repo_root = os.path.dirname(os.path.realpath(__file__))
service_file_template = repo_root + "/systemd/wikibot.service.template"
service_file = repo_root + "/systemd/wikibot.service"
timer_file = repo_root + "/systemd/wikibot.timer"


def render_service_file():

    values = {
        "repo_root": repo_root,
        "user": getpass.getuser(),
        "uv_bin": subprocess.run(["which", "uv"], stdout=subprocess.PIPE)
        .stdout.decode("utf-8")
        .strip(),
    }

    with open(service_file_template, "r") as f:
        template = string.Template(f.read())

    with open(service_file, "w") as f:
        f.write(template.substitute(values))


if __name__ == "__main__":

    print("Rendering service file...")
    render_service_file()

    print("Creating links to systemd...")
    os.symlink(service_file, "/etc/systemd/system/wikibot.service")
    os.symlink(timer_file, "/etc/systemd/system/wikibot.timer")

    print("Starting service...")
    subprocess.run(["systemctl", "daemon-reload"])
    subprocess.run(["systemctl", "start", "wikibot.timer"])
