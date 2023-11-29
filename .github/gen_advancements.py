from beet import JsonFile
# Intended to be placed in the pack root!


def add_condition(json_file, condition_type, condition_id):
    # valid condition types: visit_biome, eat_food, slay_mob, slay_any_mob,
    # breed_mob, have_effect, have_item, have_all_items
    json_file = json_file.data
    if condition_id not in json_file["criteria"]:
        if condition_type == "visit_biome":
            json_file["criteria"][condition_id] = {
                "conditions": {
                    "player": [{
                        "condition": "minecraft:entity_properties",
                        "entity": "this",
                        "predicate": {
                            "location": {
                                "biome": condition_id
                            }
                        }
                    }]
                },
                "trigger": "minecraft:location"
            }
            json_file["requirements"].append([condition_id])
        elif condition_type == "eat_food":
            json_file["criteria"][condition_id] = {
                "conditions": {
                    "item": {
                        "items": [
                            condition_id
                        ]
                    }
                },
                "trigger": "minecraft:consume_item"
            }
            json_file["requirements"].append([condition_id])
        elif condition_type == "slay_mob" or condition_type == "slay_any_mob":
            json_file["criteria"][condition_id] = {
                "conditions": {
                    "entity": [
                        {
                            "condition": "minecraft:entity_properties",
                            "entity": "this",
                            "predicate": {
                                "type": condition_id
                            }
                        }
                    ]
                },
                "trigger": "minecraft:player_killed_entity"
            }
            if condition_type == "slay_mob":
                json_file["requirements"].append([condition_id])
            else:
                json_file["requirements"][0].append(condition_id)
        elif condition_type == "breed_mob":
            json_file["criteria"][condition_id] = {
                "conditions": {
                    "child": [
                        {
                            "condition": "minecraft:entity_properties",
                            "entity": "this",
                            "predicate": {
                                "type": condition_id
                            }
                        }
                    ]
                },
                "trigger": "minecraft:bred_animals"
            }
            json_file["requirements"].append([condition_id])
        elif condition_type == "have_effect":
            if condition_id not in json_file["criteria"]["all_effects"]["conditions"]["effects"].keys():
                json_file["criteria"]["all_effects"]["conditions"]["effects"][condition_id] = {}
        elif condition_type == "have_item" or condition_type == "have_all_items":
            json_file["criteria"][condition_id] = {
                "conditions": {
                    "items": [
                        {
                            "items": [
                                condition_id
                            ]
                        }
                    ]
                },
                "trigger": "minecraft:inventory_changed"
            }
            if condition_type == "have_item":
                json_file["requirements"].append([condition_id])
            else:
                json_file["requirements"][0].append(condition_id)
    return JsonFile(json_file)


# Add biomes
handle = JsonFile(source_path="data/astound/advancements/adventure/adventuring_time.json")
cond_list = [
    "great_big_world:aspen_forest",
    "great_big_world:snowy_aspen_forest",
    "promenade:blush_sakura_grove",
    "promenade:carnelian_treeway",
    "promenade:cotton_sakura_grove",
    "promenade:glacarian_taiga",
    "snifferplus:timeless_grotto",
    "traverse:autumnal_woods",
    "traverse:coniferous_forest",
    "traverse:desert_shrubland",
    "traverse:flatlands",
    "traverse:lush_swamp",
    "traverse:snowy_coniferous_forest",
    "traverse:woodlands",
    "wilderwild:flower_field",
    "wilderwild:jellyfish_caves",
    "wilderwild:oasis",
    "wilderwild:rainforest",
    "wilderwild:warm_beach",
    "wilderwild:warm_river"
]
for i in cond_list:
    handle = add_condition(handle, "visit_biome", i)
handle.dump(origin="data/astound/advancements/adventure/", path="adventuring_time.json")

handle = JsonFile(source_path="data/astound/advancements/nether/explore_nether.json")
cond_list = [
    "cinderscapes:ashy_shoals",
    "cinderscapes:blackstone_shales",
    "cinderscapes:luminous_grove",
    "cinderscapes:quartz_cavern",
    "gardens_of_the_dead:soulblight_forest",
    "gardens_of_the_dead:whistling_woods"
]
for i in cond_list:
    handle = add_condition(handle, "visit_biome", i)
handle.dump(origin="data/astound/advancements/nether/", path="explore_nether.json")

# Add food
handle = JsonFile(source_path="data/astound/advancements/husbandry/balanced_diet.json")
cond_list = [
    "enhancermod:sweet_berry_pie",
    "enhancermod:sweet_berry_jam",
    "promenade:blueberries",
    "enhancermod:golden_delight",
    "nears:near",
    "nears:faar",
    "pearfection:lampear",
    "pearfection:copper_lampear",
    "promenade:banana",
    "cinderscapes:bramble_berries",
    "great_big_world:acai_berries",
    "nears:soul_berries",
    "wilderwild:prickly_pear",
    "wilderwild:peeled_prickly_pear",
    "wilderwild:split_coconut",
    "wilderwild:baobab_nut",
    "supplementaries:candy",
    "supplementaries:pancake",
    "nears:cinder_sangak",
    "great_big_world:venison",
    "great_big_world:cooked_venison",
    "promenade:cooked_duck",
    "promenade:duck",
    "jineric:golden_beetroot",
    "jineric:golden_potato",
    "pearfection:pear_tart",
    "nears:soulless_pastry",
    "nears:nether_stew",
    "great_big_world:acai_bowl",
    "enhancermod:sea_dinner",
    "enhancermod:fish_salad",
    "enhancermod:nether_stew",
    "enhancermod:glow_salad",
    "enhancermod:rabbit_stew",
    "enhancermod:beetroot_stew",
    "enhancermod:pumpkin_pie",
    "enhancermod:cookie",
    "enhancermod:honey_pancake",
    "biomemakeover:glowshroom_stew",
    "biomemakeover:glowfish",
    "biomemakeover:cooked_glowfish",
    "biomemakeover:bulbus_root",
    "biomemakeover:roasted_bulbus_root",
    "biomemakeover:raw_crab",
    "biomemakeover:cooked_crab",
    "biomemakeover:crab_chowder",
    "gipples_galore:gapple",
    "gipples_galore:gelatin"
]
for i in cond_list:
    handle = add_condition(handle, "eat_food", i)
handle.dump(origin="data/astound/advancements/husbandry/", path="balanced_diet.json")

# Add mobs
cond_list = [
    "biomemakeover:cowboy",
    "biomemakeover:decayed",
    "biomemakeover:ghost",
    "biomemakeover:moth",
    "great_big_world:moose",
    "great_big_world:thicket",
    "promenade:lush_creeper",
    "promenade:sunken_skeleton",
]
handle = JsonFile(source_path="data/astound/advancements/adventure/kill_all_mobs.json")
for i in cond_list:
    handle = add_condition(handle, "slay_mob", i)
handle.dump(origin="data/astound/advancements/adventure/", path="kill_all_mobs.json")
handle = JsonFile(source_path="data/astound/advancements/adventure/kill_a_mob.json")
for i in cond_list:
    handle = add_condition(handle, "slay_any_mob", i)
handle.dump(origin="data/astound/advancements/adventure/", path="kill_a_mob.json")

# Add breeding
handle = JsonFile(source_path="data/astound/advancements/husbandry/bred_all_animals.json")
cond_list = [
    "promenade:capybara",
    "promenade:duck",
    "snuffles:snuffle"
]
for i in cond_list:
    handle = add_condition(handle, "breed_mob", i)
handle.dump(origin="data/astound/advancements/husbandry/", path="bred_all_animals.json")

# Add effects
handle = JsonFile(source_path="data/astound/advancements/nether/all_potions.json")
handle = add_condition(handle, "have_effect", "biomemakeover:nocturnal")
handle.dump(origin="data/astound/advancements/nether/", path="all_potions.json")
handle = JsonFile(source_path="data/astound/advancements/nether/all_effects.json")
handle = add_condition(handle, "have_effect", "biomemakeover:nocturnal")
handle = add_condition(handle, "have_effect", "biomemakeover:possessed")
handle = add_condition(handle, "have_effect", "biomemakeover:shocked")
handle = add_condition(handle, "have_effect", "gipples_galore:gipple")
handle.dump(origin="data/astound/advancements/nether/", path="all_effects.json")

# Add eyes
cond_list = [
    "endrem:black_eye",
    "endrem:cold_eye",
    "endrem:corrupted_eye",
    "endrem:lost_eye",
    "endrem:nether_eye",
    "endrem:old_eye",
    "endrem:rogue_eye",
    "endrem:cursed_eye",
    "endrem:evil_eye",
    "endrem:guardian_eye",
    "endrem:magical_eye",
    "endrem:wither_eye",
    "endrem:witch_eye",
    "endrem:undead_eye",
    "endrem:exotic_eye",
    "endrem:cryptic_eye"
]
handle = JsonFile(source_path="data/astound/advancements/story/challenge_pearl.json")
for i in cond_list:
    handle = add_condition(handle, "have_item", i)
handle.dump(origin="data/astound/advancements/story/", path="challenge_pearl.json")
handle = JsonFile(source_path="data/astound/advancements/story/frame_perfect.json")
for i in cond_list:
    handle = add_condition(handle, "have_all_items", i)
handle.dump(origin="data/astound/advancements/story/", path="frame_perfect.json")
