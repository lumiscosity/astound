from beet import JsonFile
# Intended to be placed in the pack root!


def add_wood(wood_type, condition_id):
    # every wood can be cut into a log
    # every log can be stripped, hollowed and stripped + hollowed
    # every stripped log can be hollowed
    # every plank can be cut into slabs, stairs, trims and panels
    # every trim can be cut into panels
    # every bamboo plank can also be cut into a mosaic, mosaic slabs or mosaic stairs
    # and every mosaic can be cut into slabs or stairs
    # and every bamboo block can be cut into 9 bamboo
    # usually you can strip bamboo blocks, but whistlecane isn't strippable
    if wood_type != "bamboo":
        # log to stripped log
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_" + wood_type
            },
            "result": condition_id.replace(":", ":stripped_") + "_" + wood_type
        }
        if condition_id[:9] != "minecraft":
            JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_to_slog.json")
        # log to hollowed log
        if condition_id[:9] == "minecraft" or condition_id[:10] == "wilderwild":
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": condition_id + "_" + wood_type
                },
                "result": condition_id.replace("wilderwild:", "wilderwild:hollowed_").replace("minecraft:",
                                                                                              "wilderwild:hollowed_") + "_" + wood_type
            }
        else:
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": condition_id + "_" + wood_type
                },
                "result": "astound:" + condition_id.replace(":", "_hollowed_") + "_" + wood_type
            }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_to_hlog.json")
        # log to stripped hollowed log
        if condition_id[:9] == "minecraft" or condition_id[:10] == "wilderwild":
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": condition_id + "_" + wood_type
                },
                "result": condition_id.replace("wilderwild:", "wilderwild:stripped_hollowed_").replace("minecraft:",
                                                                                                       "wilderwild:stripped_hollowed_") + "_" + wood_type
            }
        else:
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": condition_id + "_" + wood_type
                },
                "result": "astound:" + condition_id.replace(":", "_stripped_hollowed_") + "_" + wood_type
            }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_to_shlog.json")
        # slog to stripped hollowed log
        if condition_id[:9] == "minecraft" or condition_id[:10] == "wilderwild":
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": condition_id.replace(":", ":stripped_") + "_" + wood_type
                },
                "result": condition_id.replace("wilderwild:", "wilderwild:stripped_hollowed_").replace("minecraft:",
                                                                                                       "wilderwild:stripped_hollowed_") + "_" + wood_type
            }
        else:
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": condition_id.replace(":", ":stripped_") + "_" + wood_type
                },
                "result": "astound:" + condition_id.replace(":", "_stripped_hollowed_") + "_" + wood_type
            }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_s_to_shlog.json")
        # hlog to stripped hollowed log
        if condition_id[:9] == "minecraft" or condition_id[:10] == "wilderwild":
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": condition_id.replace("wilderwild:", "wilderwild:hollowed_").replace("minecraft:",
                                                                                                "wilderwild:hollowed_") + "_" + wood_type
                },
                "result": condition_id.replace("wilderwild:", "wilderwild:stripped_hollowed_").replace("minecraft:",
                                                                                                       "wilderwild:stripped_hollowed_") + "_" + wood_type
            }
        else:
            json_file = {
                "type": "minecraft:stonecutting",
                "count": 1,
                "ingredient": {
                    "item": "astound:" + condition_id.replace(":", "_hollowed_") + "_" + wood_type
                },
                "result": "astound:" + condition_id.replace(":", "_stripped_hollowed_") + "_" + wood_type
            }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_h_to_shlog.json")
        # wood to log
        if wood_type == "log" or condition_id == "pearfection:callery":
            wood_block_type = "_wood"
        else:
            wood_block_type = "_hyphae"
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + wood_block_type
            },
            "result": condition_id + "_" + wood_type
        }
        if condition_id[:9] != "minecraft":
            JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_wood_to_log.json")
    elif condition_id[:9] != "minecraft":
        # block to raw
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_block"
            },
            "result": condition_id
        }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_block_to_raw.json")
        # planks to mosaic
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_planks"
            },
            "result": condition_id + "_mosaic"
        }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_p_to_m.json")
        # planks to mosaic slabs
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 2,
            "ingredient": {
                "item": condition_id + "_planks"
            },
            "result": condition_id + "_mosaic_slab"
        }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_p_to_m_slab.json")
        # planks to mosaic stairs
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_planks"
            },
            "result": condition_id + "_mosaic_stairs"
        }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_p_to_m_stairs.json")
        # mosaic to mosaic slabs
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 2,
            "ingredient": {
                "item": condition_id + "_mosaic"
            },
            "result": condition_id + "_mosaic_slab"
        }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_m_to_m_slab.json")
        # mosaic to mosaic stairs
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_mosaic"
            },
            "result": condition_id + "_mosaic_stairs"
        }
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_m_to_m_stairs.json")
    # planks to slabs
    json_file = {
        "type": "minecraft:stonecutting",
        "count": 2,
        "ingredient": {
            "item": condition_id + "_planks"
        },
        "result": condition_id + "_slab"
    }
    if condition_id[:9] != "minecraft":
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_p_to_slab.json")
    # planks to stairs
    json_file = {
        "type": "minecraft:stonecutting",
        "count": 1,
        "ingredient": {
            "item": condition_id + "_planks"
        },
        "result": condition_id + "_stairs"
    }
    if condition_id[:9] != "minecraft":
        JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_p_to_stair.json")
    # planks to trims
    if condition_id[:9] != "minecraft":
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_planks"
            },
            "result": "astound:" + condition_id.replace(":", "_") + "_trim"
        }
    else:
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_planks"
            },
            "result": condition_id.replace("minecraft:", "abstractmod:") + "_trim"
        }
    JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_p_to_trim.json")
    # planks to panel
    if condition_id[:9] != "minecraft":
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_planks"
            },
            "result": "astound:" + condition_id.replace(":", "_") + "_panel"
        }
    else:
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id + "_planks"
            },
            "result": condition_id.replace("minecraft:", "abstractmod:") + "_panel"
        }
    JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_p_to_panel.json")
    # trim to panel
    if condition_id[:9] != "minecraft":
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": "astound:" + condition_id.replace(":", "_") + "_trim"
            },
            "result": "astound:" + condition_id.replace(":", "_") + "_panel"
        }
    else:
        json_file = {
            "type": "minecraft:stonecutting",
            "count": 1,
            "ingredient": {
                "item": condition_id.replace("minecraft:", "abstractmod:") + "_trim"
            },
            "result": condition_id.replace("minecraft:", "abstractmod:") + "_panel"
        }
    JsonFile(json_file).dump("data/astound/recipes/", condition_id.replace(":", "_") + "_t_to_panel.json")


wood_type_list = [
    "minecraft:oak",
    "minecraft:spruce",
    "minecraft:jungle",
    "minecraft:birch",
    "minecraft:acacia",
    "minecraft:dark_oak",
    "minecraft:cherry",
    "minecraft:mangrove",
    "promenade:sakura",
    "promenade:maple",
    "great_big_world:aspen",
    "great_big_world:mahogany",
    "great_big_world:acai",
    "promenade:palm",
    "wilderwild:baobab",
    "wilderwild:cypress",
    "wilderwild:palm",
    "traverse:fir",
    "biomemakeover:blighted_balsa",
    "biomemakeover:willow",
    "biomemakeover:swamp_cypress",
    "biomemakeover:ancient_oak",
    "snifferplus:stone_pine"
]
stem_type_list = [
    "minecraft:crimson",
    "minecraft:warped",
    "promenade:dark_amaranth",
    "cinderscapes:scorched",
    "cinderscapes:umbral",
    "gardens_of_the_dead:soulblight",
    "pearfection:callery"  # callery is special because the log is a stem but the wood is a wood
]
bamboo_list = [
    "minecraft:bamboo",
    "gardens_of_the_dead:whistlecane"
]
for i in wood_type_list:
    add_wood("log", i)
for i in stem_type_list:
    add_wood("stem", i)
for i in bamboo_list:
    add_wood("bamboo", i)
