import compute_proba as cp

def find_wanted_proba(dice_list, comb_list):
    action = {
        "pair": cp.compute_pair_proba,
        "three": cp.compute_three_proba,
        "four": cp.compute_four_proba,
        "full": cp.compute_full_proba,
        "straight": cp.compute_straight_proba,
        "yams": cp.compute_yams_proba
    }
    return action[comb_list[0]](dice_list, comb_list)
