# This file is a part of renpy-gallery-inject, see __init__.py for more details.
# Copyright (C) 2022 Numerlor

# should the gallery selection screen be used for multiple galleries
define USE_GALLERY_SELECTION_SCREEN_ = False

# size of the change name/back text at the bottom
define BOTTOM_TEXT_SIZE_ = 30

# size of text in name changer
define NAME_CHANGE_TEXT_SIZE_ = 22
# number of columns in name changer
define NAME_CHANGE_NAME_COLS_ = 3
# spacing between columns in name changer
define NAME_CHANGE_Y_SPACING_ = 5
# spacing between items in columns in name changer
define NAME_CHANGE_X_SPACING_ = 10

# size of gallery navigation arrows
define GALLERY_NAVIGATION_TEXT_SIZE_ = 50
define GALLERY_X_SPACING_ = 10
define GALLERY_Y_SPACING_ = 15

# Amount of columns in galleries
define GALLERY_COLS_ = 3
# Amount of rows in galleries
define GALLERY_ROWS_ = 3
define GALLERY_ITEM_COUNT_ = GALLERY_COLS_ * GALLERY_ROWS_

# Force use of the fallback button if the position in the menu is undesirable
define FORCE_FALLBACK_BUTTON_ = False
# Properties applied to the fallback gallery button which is used if a position in the menu can't be found.
define FALLBACK_BUTTON_X_ALIGN_ = 0.99
define FALLBACK_BUTTON_Y_ALIGN_ = 0.0
define FALLBACK_BUTTON_SIZE_ = 35

init python:
    from collections import OrderedDict as __OrderedDict
    from mods.MetalChickenGallery import grouper as __grouper

    def __default_scope():
        return {"you": Character(persistent.mod_gallery_names_["Player"])}

    def __danella_scope():
        d = {"dani": Character("Danella", color="#cc7474")}
        d.update(__default_scope())
        return d

    def __gemma_scope():
        d = {"gemma": Character("Gemma", color="#b17638")}
        d.update(__default_scope())
        return d

# Items are grouped into pages by the grouper function
# List of replay items used by galleries, MAIN_GALLERY_REPLAY_ITEMS_ is used when USE_GALLERY_SELECTION_SCREEN_ is False
define MAIN_GALLERY_REPLAY_ITEMS_ = __grouper(
    [
        ReplayItem_("bg5_danella", "replay1", __danella_scope),
        ReplayItem_("bg7_massage", "replay2", __gemma_scope),
        ReplayItem_("ch_iny_penis_scene", "replay3", __default_scope),
        ReplayItem_("bg15_mayor_seat", "replay4", __default_scope),
        ReplayItem_("bg16_ivy_special", "replay5", __default_scope),
    ],
    GALLERY_ITEM_COUNT_,
)

# List of galleries and their replay items if the gallery selection is enabled
define GALLERIES_ = __grouper(
    [],
    GALLERY_ITEM_COUNT_,
)

# Names configurable by the user and their defaults, stored in persistent.mod_gallery_names_,
# to use in the scopes passed to replay items
init python:
    default_names_ = __OrderedDict(
        (
            (u"Player", u"You"),
        ),
    )

