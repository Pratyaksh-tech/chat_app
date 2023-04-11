import smtplib
import random

class Sendmail:
	def __init__(self, email):
		self.a = 0;
		self.code="";
		while self.a<=3:
			self.codes = str(random.randint(0, 9));
			self.code +=self.codes; 
			self.a+=1;	
			
		self.sender = "shanutc1212@gmail.com";
		self.receiver = email;
		self.password = "wuqemjopppviyoif";
		self.subject = "Account Verification";
		self.body = f"Your Account Verification code is {self.code}";

		message = f"""from: best.com
		To: {self.receiver}
		Subject: {self.subject}\n
		{self.body}	
		"""

		server = smtplib.SMTP("smtp.gmail.com", 587);
		server.starttls();
		
		server.login(self.sender, self.password);
		print("logged In...")

		server.sendmail(self.sender, self.receiver, message)
		
		server.quit();
		self.orignal_code = self.code;

