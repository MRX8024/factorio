import json
import zlib
import base64
import os

FACTORIO_VERSION = 562949958139904

def encode_bp_json(data):
    json_bytes = json.dumps(data, separators=(',', ':')).encode('utf-8')
    compressed = zlib.compress(json_bytes)
    encoded = base64.b64encode(compressed).decode('utf-8')
    return '0' + encoded

def create_entity(entity_name, orientation):
    return {
        "entity_number": -1,
        "name": entity_name,
        "position": {"x": 0, "y": 0},
        "enable_logistics_while_moving": False,
        "trunk_inventory": None,
        "ammo_inventory": None,
        "driver_is_main_gunner": False,
        "selected_gun_index": 1,
        "orientation": orientation
    }

def assign_entity_number(entity, number):
    entity_copy = entity.copy()
    entity_copy["entity_number"] = number
    return entity_copy

def create_bp(label, entities, icon_name):
    return {
        "icons": [
            {"signal": {"name": icon_name}, "index": 1}
        ],
        "entities": [assign_entity_number(e, i + 1) for i, e in enumerate(entities)],
        "item": "blueprint",
        "label": label,
        "version": FACTORIO_VERSION
    }

def main():
    resolution = 48
    for entity_name in ("car", "tank"):
        blueprints = []
        for i in range(resolution):
            orientation = i / resolution
            angle_deg = orientation * 360
            label = f"{angle_deg}°"
            entity = create_entity(entity_name, orientation)
            blueprint = create_bp(label, [entity], entity_name)
            blueprints.append(blueprint)
        book_label = f"{entity_name.capitalize()} Orientations"
        book = {
            "blueprint_book": {
                "blueprints": [
                    {"blueprint": bp, "index": idx} for idx, bp in enumerate(blueprints)
                ],
                "item": "blueprint-book",
                "label": book_label,
                "active_index": 0,
                "version": FACTORIO_VERSION
            }
        }
        encoded = encode_bp_json(book)
        print(str(encoded))


if __name__ == "__main__":
    main()
