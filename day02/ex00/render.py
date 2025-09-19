import sys

def replace(line, dict_var):
    
def check(line):
    i = 0
    for letter in line:
        if letter == "}":
            r = letter[1:i-1]
        i = i + 1
    return r

def render(content, dict_var):
    template = content.split('\n')
    for l in template:
        i = 0
        for letter in l:
            if letter == '{':
                r = check(l[i:])
                if r != "":
                    replace(r, dict_var)
            i = i + 1 
    return content

def create_var(content):
    dict_var = {}
    for line in content.split('\n'):
        if len(line) > 0:
            var = line.split('=')
            dict_var[var[0]] = var[1]
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
                render(content, dict_var)
        except IOError as e:
            print(e)
    