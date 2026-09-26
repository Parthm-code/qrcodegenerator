import qrcode
from urllib.parse import quote
def upitoqr():
    u_id=input("enter your upi id :")

    phonepe_url=f"upi://pay?pa={u_id}&pn=Recipient%20Name$mc=1234"
    paytm_url=f"upi://pay?pa={u_id}&pn=Recipient%20Name$mc=1234"
    googlepay_url=f"upi://pay?pa={u_id}&pn=Recipient%20Name$mc=1234"

    phonepe_qr=qrcode.make(phonepe_url)
    paytm_qr=qrcode.make(paytm_url)
    googlepay_qr=qrcode.make(googlepay_url)

    phonepe_qr.show()
    paytm_qr.show()
    googlepay_qr.show()

def specificamt():
    u_id=input("enter your upi id :")
    name=input("enter your name")
    amount= input("Enter amount:")
    note= input("Enter payment note:")

    googlepay_url= f"upi://pay?pa={u_id}&pn={name}&am={amount}&tn={note}&cu=INR"
    phonepe_url= f"upi://pay?pa={u_id}&pn={name}&am{amount}&tn={note}&cu=INR"
    paytm_url= f"upi://pay?pa={u_id}&pn={name}&am={amount}&tn={note}&cu=INR"

    phonepe_qr=qrcode.make(phonepe_url)
    paytm_qr=qrcode.make(paytm_url)
    googlepay_qr=qrcode.make(googlepay_url)

    phonepe_qr.show()
    paytm_qr.show()
    googlepay_qr.show()
    

choice= int(input('enter ur choice(1/2)'))
if choice == 1:
    upitoqr()

elif choice == 2:
    specificamt()


else:
    print("invalid response recieved")
