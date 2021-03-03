"""
Automate deployment to PyPi
"""

import invoke


@invoke.task
def deploy(ctx):
    """
    Automate deployment
    rm -rf build/* dist/*
    bumpversion patch --verbose
    python3 setup.py sdist bdist_wheel
    twine upload dist/*
    git push --tags
    """
    ctx.run("rm -rf build/* dist/*")
    # ctx.run("bumpversion {bump} --verbose")
    ctx.run("python3 setup.py sdist bdist_wheel")
    ctx.run("python3 -m twine check dist/*")
    ctx.run("python3 -m twine upload dist/*")
    ctx.run("git push origin --tags")

@invoke.task
def gitpush(ctx):
    """
    Automate push for minor changes including typos and reversions
    """
    # message = ' '.join(message.split('_'))
    # ctx.run("git add -A")
    # ctx.run(f"git commit -m '{message}'")
    ctx.run("git push origin")
    
    
@invoke.task
def gittag(ctx):
    """
    Automate push and tagging
    for any change that will change behaviour
    """
    # message = ' '.join(message.split('_'))
    # ctx.run("git add -A")
    # ctx.run(f"git commit -m '{message}'")
    # ctx.run(f"git tag -a {tag} -m {message}")
    ctx.run("git push origin --tags")
    

    
