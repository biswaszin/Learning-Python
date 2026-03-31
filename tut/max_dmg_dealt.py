

def max_damage_finder(combat_log):
    max_dmg_dealt = float("-inf")
    for damage in combat_log:
        if damage > max_dmg_dealt:
            max_dmg_dealt = damage
    return max_dmg_dealt


combat_log = [
    -187, 142, -59, 0, 199, -200, 173, -121, 88, -34,
    56, -98, 127, -165, 12, 190, -76, 41, -143, 102,
    -18, 67, -199, 158, -110, 95, -47, 21, -132, 176,
    -84, 139, -6, 160, -171, 79, -57, 33, -155, 118,
    -93, 44, -126, 181, -15, 70, -178, 134, -62, 9,
    200, -141, 83, -29, 52, -104, 120, -167, 25, 192,
    -71, 38, -149, 111, -22, 61, -190, 151, -117, 97,
    -43, 17, -136, 169, -89, 145, -3, 156, -174, 75,
    -54, 28, -159, 116, -100, 49, -123, 184, -11, 64,
    -181, 130, -69, 7, 198, -148, 86, -31, 58, -107
]

resultant_damage = max_damage_finder(combat_log)

print(f"The Maximum damage dealt is: {resultant_damage}")
