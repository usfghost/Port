# imports
import requests
import stdiomask

url = 'http://localhost:3000/sign_in.php'

username = input('username: ')
password = stdiomask.getpass(prompt='password: ', mask='*')

obj = {'username' : username, 'password' : password}