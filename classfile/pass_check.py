import re
def check_password_strength(pword):
    cnt =0
    if len(pword) <= 3:
        return 'Poor'
    if len(re.findall("[@!$&]", pword)) > 0:
        cnt +=1
    if len(re.findall("[0-9]", pword)) > 0:
        cnt +=1
    if len(re.findall("[a-z]", pword)) > 0:
        cnt +=1
    if len(re.findall("[A-Z]", pword)) > 0:
        cnt +=1
    if cnt <=1 :
        return 'Poor'
    elif cnt <=2:
        return  'Medium'
    else:
        return 'Strong'

if __name__ == "__main__":
    print(check_password_strength('pass'))