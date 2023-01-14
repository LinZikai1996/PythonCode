import re

LIST_OF_GENERAL_INFO = ('干员名', '干员外文名', '情报编号', '特性', '稀有度', '职业', '分支', '位置', '标签', '所属组织')

LIST_OF_ATTRIBUTE_INFO = ('再部署', '部署费用', '阻挡数', '攻击速度',
                          '精英0_满级', '精英0_满级_生命上限', '精英0_满级_攻击', '精英0_满级_防御', '精英0_满级_法术抗性',
                          '精英1_满级', '精英1_满级_生命上限', '精英1_满级_攻击', '精英1_满级_防御', '精英1_满级_法术抗性',
                          '精英2_满级', '精英2_满级_生命上限', '精英2_满级_攻击', '精英2_满级_防御', '精英2_满级_法术抗性',
                          '信赖加成_生命上限', '信赖加成_攻击', '信赖加成_防御', '潜能', '潜能类型')


def preprocess_data_from_wiki(source_info):
    source_info = source_info[:source_info.index('==相关道具==')]

    source_info = re.sub(re.compile(r'<br/>'), ' ', source_info)
    source_info = re.sub(re.compile(r'br/>'), ' ', source_info)

    tags = ('<ref.*?ref>', '<.*?>', '&lt;', '&gt;', '{{±.*?}}', r'\[\[关卡一览.*?\]\]',
            '{{攻击范围.*?}}', r'{{fa\|plus-circle\|color.*?}}')
    for tag in tags:
        source_info = re.sub(re.compile(tag), '', source_info)

    def extract(match):
        pattern = match.re.pattern
        if pattern in (r'{{color\|.*?}}', r'{{color\|.*?}}', r'{{\*\|.*?}}', r'{{\*\*\|.*?}}',
                       r'{{\+\|.*?}}', r'{{术语\|.*?}}', r'{{\+\+\|.*?}}'):
            return re.search(r'\|.*?\|(.*?)}}', match.group(0)).group(1)
        elif pattern == r'{{变动数值lite\|.*?\|蓝\|.*?}}':
            return re.search(r'\|蓝\|(.*?)}}', match.group(0)).group(1)
        elif pattern == r'{{变动数值lite\|\|橙\|.*?}}':
            return re.search(r'\|橙\|(.*?)}}', match.group(0)).group(1)
        elif pattern == '{{修正.*?}}':
            return re.search(r'{{修正\|(.*?)\|.*?}}', match.group(0)).group(1)

    notations = (r'{{color\|.*?}}',
                 r'{{color\|.*?}}',
                 r'{{\*\|.*?}}',
                 r'{{\*\*\|.*?}}',
                 r'{{\+\|.*?}}',
                 r'{{术语\|.*?}}',
                 r'{{\+\+\|.*?}}',
                 r'{{变动数值lite\|.*?\|蓝\|.*?}}',
                 r'{{变动数值lite\|\|橙\|.*?}}', '{{修正.*?}}')

    for notation in notations:
        source_info = re.sub(notation, extract, source_info)

    return source_info


def get_general_info(source_info):
    general_info = {}

    for key in LIST_OF_GENERAL_INFO:
        if result := re.search(rf'\|{key}=(.*)\n', source_info):
            general_info[key] = result.group(1)
    return general_info


def get_attribute_info(source_info):
    attribute_info = {}

    source_info = get_string_between_start_and_end(source_info, '{{属性', '\n}}')

    for line in source_info.split('\n')[1:]:
        pair = line.split('=')
        key = pair[0].lstrip('|')
        if key in ('再部署', '部署费用', '阻挡数', '攻击速度',
                   '信赖加成_生命上限', '信赖加成_攻击', '信赖加成_防御', '潜能', '潜能类型'):
            attribute_info[key] = pair[1]

        if "精英2_满级" in source_info:
            if key in ('精英2_满级_生命上限', '精英2_满级_攻击', '精英2_满级_防御', '精英2_满级_法术抗性'):
                attribute_info[key] = pair[1]
        elif "精英1_满级" in source_info:
            if key in ('精英1_满级_生命上限', '精英1_满级_攻击', '精英1_满级_防御', '精英1_满级_法术抗性'):
                attribute_info[key] = pair[1]
        elif "精英0_满级" in source_info:
            if key in ('精英0_满级_生命上限', '精英0_满级_攻击', '精英0_满级_防御', '精英0_满级_法术抗性'):
                attribute_info[key] = pair[1]

    return attribute_info


def get_talent_info(source_info):
    talent_info = {}
    source_info = get_string_between_start_and_end(source_info, '{{天赋', '\n}}')

    for line in source_info.split('\n')[1:]:
        pair = line.split('=')
        key = pair[0].lstrip('|')
        if re.compile(r'第.天赋.效果').search(key) or re.compile(r'第.天赋.$').search(key):
            talent_info[key] = pair[1]

    return talent_info


def get_potential_info(source_info):
    potential_info = {}
    source_info = get_string_between_start_and_end(source_info, '{{潜能提升', '\n}}').strip()

    for line in source_info.split('\n')[1:]:
        pair = line.split('=')
        key = pair[0].lstrip('|')
        potential_info[key] = pair[1]

    return potential_info


def get_skill_info(source_info):
    skill_list = {}

    if '技能1（精英0开放）' in source_info:
        skill_1 = get_string_between_start_and_end(source_info, '技能1（精英0开放）', '\n}}')
    else:
        skill_1 = ''

    if '技能2（精英1开放）' in source_info:
        skill_2 = get_string_between_start_and_end(source_info, '技能2（精英1开放）', '\n}}')
    else:
        skill_2 = ''

    if '技能3（精英2开放）' in source_info:
        skill_3 = get_string_between_start_and_end(source_info, '技能3（精英2开放）', '\n}}')
    else:
        skill_3 = ''

    if '该干员没有技能' in source_info:
        return skill_list

    index = 1
    for skill_info in [skill_1, skill_2, skill_3]:

        skill = {}
        if skill_info != '':

            for key in ('技能名', '技能类型1', '技能类型2'):
                skill[key] = re.search(rf'\|{key}=(.*)\n', skill_info).group(1)

            for key in ('描述', '初始', '消耗', '持续'):
                if '技能专精3' in skill_info:
                    skill[key] = re.search(rf'\|技能专精3{key}=(.*)\n', skill_info).group(1)
                else:
                    skill[key] = re.search(rf'\|技能7{key}=(.*)\n', skill_info).group(1)

            skill_list[f'技能{index}'] = skill
            index = index + 1
    return skill_list


def get_model_info(source_info):
    module_info = {}

    if '==模组==' not in source_info:
        return module_info


def get_string_between_start_and_end(source: str, start: str, end: str):
    start_str = source.index(start)
    end_str = source.index(end, start_str)
    return source[start_str:end_str + 1]
