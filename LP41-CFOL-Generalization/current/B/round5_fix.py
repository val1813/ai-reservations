"""
Fix script: run b1=2 c-scan and condition_B test with no Unicode.
"""
import numpy as np
import json, time
from round5_experiments import (
    compute_qcmi_for_b1, X_HAT, Z_HAT, run_b1_2_verification, run_condition_b_test
)

# Monkey-patch print to filter non-ASCII
import builtins
_orig_print = builtins.print

def safe_print(*args, **kwargs):
    try:
        _orig_print(*args, **kwargs)
    except UnicodeEncodeError:
        safe_args = []
        for a in args:
            if isinstance(a, str):
                safe_args.append(a.encode('ascii', errors='replace').decode('ascii'))
            else:
                safe_args.append(a)
        try:
            _orig_print(*safe_args, **kwargs)
        except:
            pass

builtins.print = safe_print

if __name__ == '__main__':
    np.random.seed(42)
    results = {}

    print("=== Running b1_2_verification ===")
    results['5_4A_b1_2_verification'] = run_b1_2_verification()

    print("\n=== Running condition_B_test ===")
    results['5_4D_condition_B_test'] = run_condition_b_test()

    # Write partial output
    output = 'D:/Claude/ai-reservations/LP41-CFOL-Generalization/current/B/round5_gap_fill.json'
    with open(output, 'w') as f:
        json.dump(results, f, indent=2, default=lambda x: float(x) if isinstance(x, (np.floating,)) else str(x))

    print(f"\nGap-fill results written to {output}")
