import itertools
import subprocess

# Automated grid search experiments
lr_values = [26, 52, 104, 208]
momentum_values = [305, 355, 405, 455, 505]

# Iterate over all combinations of hyperparameter values.
for lr, momentum in itertools.product(lr_values, momentum_values):
    # Execute "dvc exp run --queue --set-param lr=<lr> --set-param momentum=<momentum>".
    subprocess.run(["dvc", "exp", "run", "--queue",
                    "--set-param", f"lr={lr}",
                    "--set-param", f"momentum={momentum}"])
