from local_lib.path import Path

if __name__ == '__main__':
    path = Path('test')
    file = Path('test/corr')
    if path.exists() is False:
        path.mkdir()
    if file.exists() is False:
        file.touch()
    with file.open('w') as f:
        f.write('Hello World!')
    