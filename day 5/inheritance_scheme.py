class scheme:
    def parentmethod(self,scheme_id,scheme_name,outgoing_rate,message_charge):
        self.scheme_id=scheme_id
        self.scheme_name=scheme_name
        self.outgoing_rate=outgoing_rate
        self.message_charge=message_charge
        print("Scheme Id is",self.scheme_id,"name is",self.scheme_name,"outgoing rate is",self.outgoing_rate,"and message charge is",self.message_charge)
class customer(scheme):
    def childmethod(self,cust_id,name,mobile_no):
        self.cust_id=cust_id
        self.name=name
        self.mobile_no=mobile_no
        print(self.name,"'s id is",self.cust_id,"& mobile no. is",self.mobile_no)
s=customer()
s.parentmethod(1,"qwert",23.4,50)
s.childmethod(1,"kaju",8905727693)

