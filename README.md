# antonsmindstorms-docs
Documentation for Micropython LEGO Robotics libraries and hardware, as hosted on docs.antonsmindstorms.com

# Contributing
Please fork this repository and add to it with pull requests. You will be helping a lot of people.

## Set up local environment

```
git clone --recurse-submodules https://github.com/antonvh/antonsmindstorms-docs
cd antonsmindstorms-docs
# Always use --remote so submodules track latest main/master (not pinned SHAs)
git submodule update --init --remote --recursive
pipenv shell
cd docs
make html # builds the docs
```

Update all software libraries to the tip of their tracked branch:

```
git submodule update --remote --recursive
```

## Guidelines

Add general info in the respective Sphinx .rst files.
Add docstrings, sphinx-style to the python libraries.
