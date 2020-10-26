def sed(pattern, replacement, read_file, write_file):
    try:
        with open(read_file) as fin:
            lines = fin.readlines()
    except:
        print('Source file does not exist.')
    with open(write_file, 'a') as fout:
        for line in lines:
            text = line.strip()
            text = text.lower().replace(pattern, replacement)
            file.write(text)
    print('Done')

sed('natural', 'artificial', 'titles_text', 'titles_modified')
