from colorama import init, deinit, Fore, Back, Style

# init() 

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# deinit()

a = Back.GREEN + Fore.BLACK + 'and with a green background' + Style.RESET_ALL

print(a)