def file_length(file_name):
    """
    Reads file and counts lines in it.

    :param file_name: Name of the file
    :return: File length in lines
    """
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def print_progressbar(progress, maximum, prefix=''):
    """
    Prints a progressbar in the stdin.

    :param progress: Integer value that represents current progress
    :param maximum: Integer value that represents maximum progress
    :param prefix: Words to write before the progressbar
    :return: None
    """
    pct = int(100 * (progress / maximum))
    print('\r{: <50} [{:-<50}] {}%'.format(prefix, '#' * (pct // 2), pct), end='')


def delimited_reader(reader, *delimiters):
    """
    This generator reads a file word by word.

    :param reader: The TextWrapper object to read words from
    :param delimiters: Delimiter symbols
    :return: Yields words
    """
    if len(delimiters) == 0:
        raise AssertionError('No delimiters specified')
    for delimiter in delimiters:
        if type(delimiter) != str:
            raise TypeError(f'Delimiter type should be string, not {type(delimiter)}')
        if len(delimiter) != 1:
            raise ValueError('Invalid delimiter: must be char')
    while True:
        word = ''
        letter = reader.read(1)
        while letter not in (*delimiters, ''):
            word += letter
            letter = reader.read(1)
        if word == letter == '':
            return
        else:
            yield word