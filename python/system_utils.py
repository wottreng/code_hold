import os


# check if folder exists
def check_for_folder(folder_path) -> bool:
    return os.path.isdir(folder_path)


def check_if_file_exists(file_path) -> bool:
    return os.path.isfile(file_path)


def create_folder(folder_path) -> None:
    os.mkdir(folder_path)


def create_file(file_path) -> None:
    open(file_path, 'w').close()


def delete_folder(folder_path) -> None:
    os.rmdir(folder_path)


def delete_file(file_path) -> None:
    os.remove(file_path)


def get_file_name(file_path) -> str:
    return os.path.basename(file_path)


# remove directory and all its contents
def remove_directory(directory_path) -> None:
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(directory_path)


# return ordered list all files with a given extension in a directory
def list_files_with_extension(directory_path, extension) -> list:
    file_list = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith(extension)]
    file_list.sort()
    return file_list


# return working directory for current script
def get_script_path() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def fatal_error(message: str, stack_trace_function=None) -> None:
    print("[FATAL ERROR]", stack_trace_function, message)
    exit(1)


def non_fatal_error(message: str, stack_trace_function=None) -> None:
    print("[ERROR]", stack_trace_function, message)
