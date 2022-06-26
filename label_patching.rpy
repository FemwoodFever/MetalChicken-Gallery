init 999 python hide:
    from mods.MetalChickenGallery import (
        load_patch_nodes,
        find_label,
        find_say,
        find_scene,
        find_jump,
        find_show,
        find_menu,
        patch_after_node,
        create_replay_label,
        create_end_replay_node,
    )
    load_patch_nodes()

    label = find_label("intro_scene")
    to_replace = find_scene({"name": "bg4_bench"}, label, return_previous=True)
    patch_after_node(to_replace, create_replay_label("replay1"))

    to_replace = find_say({"what": "{b}WHAT'S GOING ON HERE, FOR FUCKS SAKE{/b}"}, label)
    patch_after_node(to_replace.next, create_end_replay_node())

    label = find_label("hotel_scene")
    to_replace = find_scene({"name": "bg7_massage"}, label, return_previous=True)
    patch_after_node(to_replace, create_replay_label("replay2"))

    to_replace = find_scene({"name": "black"}, label, return_previous=True)
    patch_after_node(to_replace, create_end_replay_node())

    label = find_label("cityhall_deal_scene")
    to_replace = find_scene({"name": "ch_iny_penis_scene"}, label, return_previous=True)
    patch_after_node(to_replace, create_replay_label("replay3"))

    to_replace = find_scene({"name": "black"}, to_replace)
    patch_after_node(to_replace, create_end_replay_node())

    to_replace = find_show("bg15_mayor_seat", label, return_previous=True)
    patch_after_node(to_replace, create_replay_label("replay4"))

    to_replace = find_show("bg14_mayor_cabinet", to_replace)
    patch_after_node(to_replace, create_end_replay_node())

    to_replace = find_show("bg16_ivy_special", label, return_previous=True)
    patch_after_node(to_replace, create_replay_label("replay5"))

    to_replace = find_menu(to_replace, return_previous=True)
    patch_after_node(to_replace, create_end_replay_node())
