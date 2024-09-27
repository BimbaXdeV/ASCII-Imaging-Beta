from os import listdir, system, name, remove, path
from colorist import ColorRGB, BgColorRGB
from pyfiglet import figlet_format
from time import sleep as delay
from datetime import datetime
from pathlib import Path
from PIL import Image


class ImageHandler:
    def __init__(self, width: int = 75, offset: int = 2):
        self.WIDTH: int = width
        self.OFFSET: int = offset

    def init_update(self, new_width: int, new_offset: int):
        self.WIDTH = new_width
        self.OFFSET = new_offset

    @staticmethod
    def to_gray_scale(__image: Image.Image):
        return __image.convert('L')

    @staticmethod
    def scaling_image(__gray_image: Image.Image, width: int):
        __w, __h = __gray_image.size
        __aspect_ratio = width / __w
        __new_w, __new_h = int(__aspect_ratio * __w), int(__aspect_ratio * __h)
        return __gray_image.resize((__new_w, __new_h))


class AsciiGenerator:
    def __init__(self):
        self.CHARS = ['.', ',', ':', ';', '*', '+', '?', '%', '$', '#', '@']

    def to_ascii_chars(self, __scaling_image: Image.Image):
        __pixels = __scaling_image.getdata()

        __ascii_str = ''
        for __pixel in __pixels:
            __ascii_str += self.CHARS[int((__pixel / 255.0) * (len(self.CHARS) - 1))]

        return __ascii_str

    @staticmethod
    def write_ascii_art(__scaling_image: Image.Image, __image_name: str, __ascii_str: str, __image_width: int, __image_offset: int):
        __w = __scaling_image.width

        __file = open(f'Out/{__image_name.split(".")[0]}.txt', 'w')
        for i in range(0, len(__ascii_str), __image_width):
            __file.write(f'{(" " * __image_offset).join(__ascii_str[i:i + __image_width])}\n')
        __file.close()


class Program:
    def __init__(self, menu: str, mode: str = 'one'):
        self.MENU: str = menu
        self.MODE: str = mode
        self.VER: tuple[str, str | int, str | int] = ('Beta', 0, '09')
        self.DIR_HANDLE_PATH = 'In/'
        self.DIR_GLOBAL_PATH = f'{Path.cwd()}'.replace('\\', '/')
        self.DEBUG_LOG_PATH = 'Cache/debug_log.txt'
        self.LOGO = figlet_format('Ascii  Gen  Beta', font='slant')

        self.menu_identifiers = [
            'start',
            'choosing',
            'processing',
            'finished',
            'exit'
        ]

        self.chooses = {
            '1': 'Convert image to ASCII-art',
            '2': 'Convert All from \"In\" to ASCII-art',
            '3': 'Clear all from \"In\" directory',
            '4': 'Clear all from \"Out\" directory',
            '5': 'Reset debug logs',
            '6': 'Exit of this program'
        }

        self.allowed_formats = [
            'png',
            'jpg',
            'jpeg'
        ]

        self.file_handle_modes = [
            'one',
            'all'
        ]

        self.delays = {
            'START_ASCII_ANIMATION': 0.3,
            'START_IN': 0.6,
            'START_OUT': 2,
            'CHOOSING_IN': 0.3,
            'CHOOSING_OUT': 1.1,
            'PROCESSING_IN': 0.4,
            'PROCESSING_OUT': 2.8,
            'FINISHED_OUT': 1.9,
            'EXIT_OUT': 0.5
        }

        self.terminal_colors = {
            'critical_error': ColorRGB(255, 20, 23),
            'debug_error': ColorRGB(3, 169, 252),
            'warning': ColorRGB(224, 196, 52),
            'finished': ColorRGB(17, 255, 0),
            'description': ColorRGB(179, 255, 195),
            'version': ColorRGB(0, 238, 255),
            'values': ColorRGB(0, 172, 224),
            'names': ColorRGB(0, 255, 183),
            'paths': ColorRGB(238, 242, 128),
            'logo': ColorRGB(0, 255, 98)
        }

    def update_menu(self, __new_menu: str):
        self.MENU = __new_menu

    def update_handle_mode(self, __user_input: int):
        if __user_input not in [1, 2]:
            self.MODE = None
        else:
            self.MODE = self.file_handle_modes[__user_input - 1]

    @staticmethod
    def clear_terminal():
        system('cls' if name == 'nt' else 'clear')

    def debug_log(self, __log: str):
        __file = open(self.DEBUG_LOG_PATH, 'w')
        __file.write(f'[ {datetime.now()} ] {__log}\n')
        __file.close()

    def clear_debug_logs(self):
        remove(self.DEBUG_LOG_PATH)
        print(f'{self.terminal_colors["finished"]}Done! List of logs has been cleared (This list come backs where next processes return a error or exceptions){self.terminal_colors["finished"].OFF}')

    def clear_directory(self, __directory: str):
        __files = listdir(f'{self.DIR_GLOBAL_PATH}/{__directory}')
        if __files is None:
            print(f'{self.terminal_colors["warning"]}Invalid directory cleaning:{self.terminal_colors["warning"].OFF} invalid path to project directory\n')
            self.debug_log(f'Invalid directory cleaning: files from path \"{self.DIR_GLOBAL_PATH}/{__directory}\" not found')
        else:
            for __file in __files:
                __path = path.join(f'{self.DIR_GLOBAL_PATH}/{__directory}', __file).replace('\\', '/')
                if path.isfile(__path):
                    try:
                        remove(__path)
                        print(f'{self.terminal_colors["description"]}[ Cleaning ] File deleted from path:{self.terminal_colors["description"].OFF} {self.terminal_colors["paths"]}\"{__path}\"{self.terminal_colors["paths"].OFF}')
                    except PermissionError:
                        print(f'{self.terminal_colors["debug_error"]}Not available permissions:{self.terminal_colors["debug_error"].OFF} there are no administrator rights, due to which cleaning the file along the path {self.terminal_colors["paths"]}\"{__path}\"{self.terminal_colors["paths"].OFF} is impossible')
                        self.debug_log(f'Not available permissions: there are no administrator rights, due to which cleaning the file along the path \"{__path}\" is impossible')
                else:
                    print(f'{self.terminal_colors["warning"]}File deleting interrupted:{self.terminal_colors["warning"].OFF} file with path {self.terminal_colors["paths"]}\"{__path}\"{self.terminal_colors["paths"].OFF} not cleaned, this not file')
                    self.debug_log(f'File deleting interrupted: file with path \"{__path}\" not cleaned, this not file')


if __name__ == '__main__':
    __program, __handler, __ascii = Program('start'), ImageHandler(), AsciiGenerator()

    while True:
        if __program.MENU == __program.menu_identifiers[0]:
            __program.clear_terminal()
            delay(__program.delays[f'{__program.MENU.upper()}_IN'])
            print(f'{__program.terminal_colors["version"]}Program version: {__program.VER[1]}.{__program.VER[2]}  (Build status: {__program.VER[0]}){__program.terminal_colors["version"].OFF}')

            print(__program.terminal_colors['logo'], end='')
            for stroke in __program.LOGO.split('\n'):
                delay(__program.delays['START_ASCII_ANIMATION'])
                print(stroke)
            print(__program.terminal_colors['logo'].OFF, end='')

            delay(__program.delays[f'{__program.MENU.upper()}_OUT'])
            __program.update_menu(__program.menu_identifiers[1])

        if __program.MENU == __program.menu_identifiers[1]:
            delay(__program.delays[f'{__program.MENU.upper()}_IN'])

            print(f'{__program.terminal_colors["names"]}* SELECT ACTION *{__program.terminal_colors["names"].OFF}')
            for input_code, process_description in __program.chooses.items():
                print(f'{__program.terminal_colors["values"]}[ {input_code} ]{__program.terminal_colors["values"].OFF} {process_description}')
                delay(__program.delays['START_ASCII_ANIMATION'])
            __data = input('Your: ')

            if __data not in __program.chooses.keys():
                print(f'{__program.terminal_colors["warning"]}Invalid user choose:{__program.terminal_colors["warning"].OFF} your entered choose \"{__data}\" is not exists\n')
            else:
                __program.update_handle_mode(int(__data))
                __choose_input_codes = list(__program.chooses.keys())
                if __data in [__choose_input_codes[0], __choose_input_codes[1]]:
                    __program.update_menu(__program.menu_identifiers[2])

                elif __data == __choose_input_codes[2]:
                    __program.clear_directory('In')
                    __program.update_menu(__program.menu_identifiers[3])

                elif __data == __choose_input_codes[3]:
                    __program.clear_directory('Out')
                    __program.update_menu(__program.menu_identifiers[3])

                elif __data == __choose_input_codes[4]:
                    __program.clear_debug_logs()
                    __program.update_menu(__program.menu_identifiers[3])

                elif __data == __choose_input_codes[5]:
                    __program.update_menu(__program.menu_identifiers[4])

            delay(__program.delays[f'{__program.MENU.upper()}_OUT'])

        if __program.MENU == __program.menu_identifiers[2]:
            delay(__program.delays[f'{__program.MENU.upper()}_IN'])
            if __program.MODE == __program.file_handle_modes[0]:
                __file_name = input('Okay, enter the file for converting: ')
                if __file_name == 'exit':
                    __program.update_menu(__program.menu_identifiers[1])
                else:
                    if __file_name.split('.')[1] not in __program.allowed_formats:
                        print(f'{__program.terminal_colors["warning"]}File handle interrupted:{__program.terminal_colors["warning"].OFF} selected file has not supported {__program.terminal_colors["paths"]}\"{__file_name.split(".")[1]}\"{__program.terminal_colors["paths"].OFF} format for converting\n')
                        __program.debug_log(f'File handle interrupted: selected file has not supported \"{__file_name.split(".")[1]}\" format for converting')
                    else:
                        try:
                            print(f'{__program.terminal_colors["description"]}Processing started with{__program.terminal_colors["description"].OFF} {__program.terminal_colors["paths"]}\"{__program.DIR_GLOBAL_PATH}/In/{__file_name}\"{__program.terminal_colors["paths"].OFF}')
                            __edited_image = __handler.scaling_image(__handler.to_gray_scale(Image.open(f'{__program.DIR_HANDLE_PATH}/{__file_name}')), __handler.WIDTH)
                            print(f'{__program.terminal_colors["description"]}[ Processing ] Image scaled, converting in process...{__program.terminal_colors["description"].OFF}')
                            __ascii_string = __ascii.to_ascii_chars(__edited_image)
                            print(f'{__program.terminal_colors["description"]}[ Processing ] Overwrite to file...{__program.terminal_colors["description"].OFF}')
                            __ascii.write_ascii_art(__edited_image, __file_name, __ascii_string, __handler.WIDTH, __handler.OFFSET)

                            try:
                                __file = open(f'Out/{__file_name.split(".")[0]}.txt')
                                print(f'{__program.terminal_colors["finished"]}Done! File saved to{__program.terminal_colors["finished"].OFF} {__program.terminal_colors["paths"]}\"{__program.DIR_GLOBAL_PATH}/Out/{__file_name.split(".")[0]}.txt\"{__program.terminal_colors["paths"].OFF}\n')
                            except FileNotFoundError:
                                print(f'{__program.terminal_colors["warning"]}File examination interrupted:{__program.terminal_colors["warning"].OFF} file not saved to {__program.terminal_colors["paths"]}\"{__program.DIR_GLOBAL_PATH}/Out/{__file_name.split(".")[0]}.txt\"{__program.terminal_colors["paths"].OFF}\n')
                                __program.debug_log(f'File examination interrupted: file not saved to \"{__program.DIR_GLOBAL_PATH}/Out/{__file_name.split(".")[0]}.txt\"')

                        except FileNotFoundError:
                            print(f'{__program.terminal_colors["warning"]}File opening interrupted:{__program.terminal_colors["warning"].OFF} file from {__program.terminal_colors["paths"]}\"{__program.DIR_HANDLE_PATH}{__file_name}\"{__program.terminal_colors["paths"].OFF} not found\n')
                            __program.debug_log(f'File opening interrupted: file from \"{__program.DIR_HANDLE_PATH}{__file_name}\" not found')

            elif __program.MODE == __program.file_handle_modes[1]:
                __files = listdir(f'{__program.DIR_GLOBAL_PATH}/{__program.DIR_HANDLE_PATH}')
                if __files is None:
                    print(f'{__program.terminal_colors["warning"]}File assembly error:{__program.terminal_colors["warning"].OFF} files at path {__program.terminal_colors["paths"]}\"{__program.DIR_GLOBAL_PATH}/{__program.DIR_HANDLE_PATH}\"{__program.terminal_colors["paths"].OFF} not found\n')
                    __program.debug_log(f'File assembly error: files at path \"{__program.DIR_GLOBAL_PATH}/{__program.DIR_HANDLE_PATH}\" not found')
                else:
                    for __file in __files:
                        __path = path.join(f'{__program.DIR_GLOBAL_PATH}/{__program.DIR_HANDLE_PATH}', __file).replace('\\', '/')
                        __file_name, __file_format = __path.split('/')[-1].split('.')
                        if __file_format not in __program.allowed_formats:
                            print(f'{__program.terminal_colors["warning"]}File handle interrupted:{__program.terminal_colors["warning"].OFF} selected file has not supported {__program.terminal_colors["paths"]}\"{__file_name.split(".")[1]}\"{__program.terminal_colors["paths"].OFF} format for converting\n')
                            __program.debug_log(f'File handle interrupted: selected file has not supported \"{__file_name.split(".")[1]}\" format for converting')
                        else:
                            __edited_image = __handler.scaling_image(__handler.to_gray_scale(Image.open(f'{__program.DIR_HANDLE_PATH}{__file_name}.{__file_format}')), __handler.WIDTH)
                            __ascii_string = __ascii.to_ascii_chars(__edited_image)
                            __ascii.write_ascii_art(__edited_image, __file_name, __ascii_string, __handler.WIDTH, __handler.OFFSET)
                            print(f'{__program.terminal_colors["finished"]}[ Finished ] File \"{__file_name}.txt\" converted{__program.terminal_colors["finished"].OFF}')
                    print(f'{__program.terminal_colors["finished"]}Converting finished! All files saved at path:{__program.terminal_colors["finished"].OFF} {__program.terminal_colors["paths"]}\"{__program.DIR_GLOBAL_PATH}/{__program.DIR_HANDLE_PATH}\"{__program.terminal_colors["paths"].OFF}')

            delay(__program.delays[f'{__program.MENU.upper()}_OUT'])
            __program.update_menu(__program.menu_identifiers[3])

        if __program.MENU == __program.menu_identifiers[3]:
            __continue = input('Click the \"Enter\" to back in main menu ')
            __program.clear_terminal()
            __program.update_menu(__program.menu_identifiers[1])

        if __program.MENU == __program.menu_identifiers[4]:
            print(f'{__program.terminal_colors["debug_error"]}Program is finished with exit code 0. Thanks for using, come back later :>{__program.terminal_colors["debug_error"].OFF}')
            break
