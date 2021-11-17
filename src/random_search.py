import subprocess
import random

# Automated random search experiments
num_exps = 3
random.seed(1)

for _ in range(num_exps):
    params = {
        "rand_lr_value": random.randint(26, 208),
        "rand_momentum_value": random.randint(305, 505)
    }
    subprocess.run(["dvc", "exp", "run", "--queue",
                    "--set-param", f"lr={params['rand_lr_value']}",
                    "--set-param", f"momentum={params['rand_momentum_value']}"])
