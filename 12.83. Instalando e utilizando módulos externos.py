"""
External module

Pip - Python Installer Package

https://pypi.org - Package external official

colorama - allowcond colorful text

conda install colorama

from colorama import init, Fore, Back, Style
init()
print(Fore.RED+"GeekUniversity")
print(Fore.YELLOW+"GeekUniversity")
print(Style.DIM+"GeekUniversity")
print(Style.RESET_ALL+"GeekUniversity")
print(Fore.MAGENTA+"GeekUniversity")
print(Fore.BLUE+"GeekUniversity")
print(Back.GREEN +"Yumi Ouchi")
"""
import pydf
pdf = pydf.generate_pdf('<h1>this is html</h1><br/><br/<br/><strong>Yumi Ouchi</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
