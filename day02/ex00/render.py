import sys

def check(line, new_content, dict_var, p):
    i = 0
    save_new_content = new_content
    for letter in line:
        if letter == "}":
            r = line[1:i]
            for key, value in dict_var.items():
                if key == r:
                    new_content += value
                    return new_content, i + 1
        i = i + 1
    return save_new_content, 0

def render(content, dict_var):
    new_content = ""
    i = 0
    p = 0
    for i in range(0, len(content)):
        if p + i < len(content):
            if content[p+i] == "{":
                new_content, spaces = check(content[p+i:], new_content, dict_var, i)
                p = p + spaces
            if p + i < len(content):
                new_content += content[p+i]
    return new_content

def create_var(content):
    dict_var = {}
    for line in content.split('\n'):
        if len(line) > 0:
            var = line.split('=')
            dict_var[var[0].strip()] = var[1].strip().strip('"')
    return dict_var

if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            with open(sys.argv[1], 'r') as f:
                content = f.read()
                dict_var = create_var(content)
                print(dict_var)
            with open(sys.argv[2], 'r') as f:
                content = f.read()
                new_content = render(content, dict_var)
            with open("mon_cv.html", "w", encoding="utf-8") as f:
                f.write(new_content)
        except IOError as e:
            print(e)
    