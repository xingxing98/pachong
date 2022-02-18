import requests
url = 'https://i.taobao.com/my_taobao.htm'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}

temp = 'thw=cn; t=08686ad9ad1fe1c59bfce59f799f44b8; cna=86VAGjs44ycCAbeffYDGWTjN; lgc=%5Cu3056%5Cu6C38%5Cu2606%5Cu6B23%5Cu8363%5Cu3077; tracknick=%5Cu3056%5Cu6C38%5Cu2606%5Cu6B23%5Cu8363%5Cu3077; _samesite_flag_=true; cookie2=16136312e7caae079115443e6b57dc90; _tb_token_=578e473d33d76; xlly_s=1; sgcookie=E100l6e5K1wCD2%2BHAIfHIy4NanLfx0gkABNsxmKrcO8xiQ1LQF2wQ52enJeJBk%2BU%2Fx4If3ViomPluA5jvF6F4yAw02Wcz9D8BIJL%2FDjMgQwQKwSSwduH5WpACRvi5QpeuHna; unb=3142611722; uc3=lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dCvU6PKBqxKYF3rIM%3D&id2=UNGSCkOJZZEtqQ%3D%3D&nk2=x2T2worPkKE0pgK4; csg=59518384; cancelledSubSites=empty; cookie17=UNGSCkOJZZEtqQ%3D%3D; dnk=%5Cu3056%5Cu6C38%5Cu2606%5Cu6B23%5Cu8363%5Cu3077; skt=2265e51e1232f3b2; existShop=MTY0NDIzMzMyMA%3D%3D; uc4=id4=0%40UgbqGyPKJZK55ouf3aU0fz%2FF9%2B%2Fo&nk4=0%40xQPp757qu8Lu01Hpf%2BjD0FXycni9WLw%3D; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E3%81%B72a; _nk_=%5Cu3056%5Cu6C38%5Cu2606%5Cu6B23%5Cu8363%5Cu3077; cookie1=BxSrlB5ixA0uKNyACVmIyuSHz%2BIZnRW7JCW8UWQuK7A%3D; uc1=cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie14=UoewBGWhoy9Hcw%3D%3D&existShop=false&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&pas=0&cookie21=W5iHLLyFeYZ1WM9hVnmS; isg=BDc32psfGQ_Xa52De3VaiiTDxiuB_AteEVlU6onkU4ZtOFd6kcybrvUKHJhmy-PW; l=eBMOMYMeLQzeNw3EBOfanurza77OSIRYYuPzaNbMiOCPO2CB52HPW6cji386C3GVh6vWR35sMeeMBeYBqQAonxv9w8VMULkmn; tfstk=cczPBot7vaQPRs0CX4gFAEnjA8VRwZknCElZqu6Jm6a0-bf06ph0hmhqTIJnq'

cookie_list = temp.split('; ')
# cookies = {}
# for cookie in cookie_list:
#     cookies[cookie.split('=')[0]] = cookie.split('=')[-1]

cookies = {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookie_list}

response = requests.get(url, headers=headers, cookies=cookies)
with open('taobao_with_cookies2.html', 'wb') as f:
    f.write(response.content)
