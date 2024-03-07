import os
import sys

from src.tools.yaml_operations import fill_dict_from_yaml
from src.table_setup.table_setup import rect_names1, rect_names2, rect_names3, rect_names4, rect_names5, rect_names6, rect_names7, rect_names8, rect_names9, rect_names10, rect_names11, rect_names12, rect_names13, rect_names14, rect_names15, rect_names16, rect_names17, rect_names18, rect_names19, rect_names20


# config
filled_room_config = {}
filled_room_rects = {}
template_dir = None

def load_config():
    
    # 读取默认房间配置（在config路径下）
    global filled_room_config
    room_dict = {
        'window_title': None,
        'platform': None,
        'max_players': None,
        'big_blind': None,
        'small_blind': None,
    }
    script_dir = os.path.dirname(__file__)
    room_config_yaml = os.path.join(script_dir, 'config', 'room_config.yaml')
    filled_room_config = fill_dict_from_yaml(room_dict, room_config_yaml)
    
    # 根据房间配置，读取对应的rectangles配置（在config路径下）
    global filled_room_rects
    rects_dict = {}
    keylist = []
    for i in range(1, 21):
        keylist.extend(eval(f'rect_names{i}'))
    for key in keylist:
        rects_dict[key] = None

    room_rects_yaml = os.path.join(script_dir, 'config', f"{filled_room_config['platform']}{filled_room_config['max_players']}.yaml")
    filled_room_rects = fill_dict_from_yaml(rects_dict, room_rects_yaml)

    # 获取模板路径
    global template_dir
    script_dir = os.path.dirname(__file__)
    template_dir = os.path.join(script_dir, 'config', 'templates', f"{filled_room_config['platform']}")
    # print(f"template_dir: {template_dir}")


load_config()
# print(filled_room_config)
# print(filled_room_rects)