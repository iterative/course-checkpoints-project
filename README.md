# Lesson 7: Tools for Deep Learning

## Setting up the project

- Make a virtual environment: `python3 -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install the requirements: `pip install -r requirements.txt`
- To get the data to work with this project, download this and unzip in the root of the project: https://download.pytorch.org/tutorial/hymenoptera_data.zip

## To run an experiment

With the project set up, you can run an experiment with DVC.

```dvc
$ dvc exp run
```

## To work with checkpoints

To see how checkpoints work, switch to the `checkpoints-enabled` branch.

```dvc
$ git checkout checkpoints-enabled
```
