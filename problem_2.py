import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path is None:
        return None
    if suffix is None:
        return None
    result = []
    try:

        files = os.listdir(path)

    except:

        return "path not found"

    files = [os.path.join(path, file) for file in files]

    for file in files:

        if os.path.isfile(file) and file.endswith(suffix):

            result.append(file)


        if os.path.isdir(file):

            sub_result = find_files(suffix, file)
            result.extend(sub_result)
    return result


print("\ttest1")
print(find_files('.c', 'testdir'))

print(find_files('.c', 'testdir/subdir1'))


print("\n\ttest2")

print(find_files('.', ''))

print(find_files('.abc', 'testdir/subdir2'))

print("\n\ttest3")
print(find_files('', ''))
print(find_files('.py','testdir'))
