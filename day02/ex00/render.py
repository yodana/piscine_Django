import sys

def render(content):
    return content

def create_var(content):
    dict_var = {}
    for line in content.split('\n'):
        if len(line) > 0:
            var = line.split('=')
            dict_var[var[0]] = var[1]
    return dict_var

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1], 'r') as f:
                content = f.read()
                dict_var = create_var(content)
            with open(sys.argv[2], 'r') as f:
                content = f.read()
        except IOError as e:
            print(e)
    