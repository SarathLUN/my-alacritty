import glob
import os

def convert_yaml_to_toml(yaml_content):
    toml_lines = []
    section_stack = []

    for line in yaml_content.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            if toml_lines and toml_lines[-1] != "":
                toml_lines.append("")
            continue

        if stripped_line.startswith('#'):
            toml_lines.append(stripped_line)
            continue

        indentation = len(line) - len(line.lstrip())
        key_value = stripped_line.split(':', 1)
        key = key_value[0].strip()

        level = indentation // 2

        while len(section_stack) > level:
            section_stack.pop()

        if len(key_value) > 1 and key_value[1].strip():
            value = key_value[1].strip().replace("'", '"')
            toml_lines.append(f'{key} = {value}')
        else:
            section_stack.append(key)
            toml_lines.append("")
            toml_lines.append(f'[{"/".join(section_stack))]")

    return "\n".join(toml_lines)


for file_path in glob.glob("/Users/tony/.config/alacritty/themes/themes/*.yaml"):
    with open(file_path, 'r') as f:
        yaml_content = f.read()

    toml_content = convert_yaml_to_toml(yaml_content)
    toml_path = file_path.replace(".yaml", ".toml")

    with open(toml_path, 'w') as f:
        f.write(toml_content)

    os.remove(file_path)

for file_path in glob.glob("/Users/tony/.config/alacritty/themes/themes/*.yml"):
    with open(file_path, 'r') as f:
        yaml_content = f.read()

    toml_content = convert_yaml_to_toml(yaml_content)
    toml_path = file_path.replace(".yml", ".toml")

    with open(toml_path, 'w') as f:
        f.write(toml_content)

    os.remove(file_path)

print("Migration complete.")
