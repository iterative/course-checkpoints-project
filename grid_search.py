import itertools
import subprocess

# Automated grid search experiments
n_est_values = [26, 52, 104, 208]
min_split_values = [305, 355, 405, 455, 505]

# Iterate over all combinations of hyperparameter values.
for n_est, min_split in itertools.product(n_est_values, min_split_values):
    # Execute "dvc exp run --queue --set-param train.n_est=<n_est> --set-param train.min_split=<min_split>".
    subprocess.run(["dvc", "exp", "run", "--queue",
                    "--set-param", f"train.n_est={n_est}",
                    "--set-param", f"train.min_split={min_split}"])
