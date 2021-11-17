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

## To work with CML

If you're interested in how you can create your own CI/CD for ML projects, check out the `add-cml` branch.

```dvc
$ git checkout add-cml
```

## To follow along with the ODSC West Workshop

If you're here to get the start repo for this workshop, check out the `odsc-west-workshop` branch.

```dvc
$ git checkout odsc-west-workshop
```
