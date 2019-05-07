import smtplib

try:
	with smtplib.SMTP('smtp.gmail.com',587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login("onlineresumeforse2019@gmail.com","onlineresume.666")
		subject = "Interview Invitation - Select Timings"
		body = "2-3pm,3-4pm,5-6pm"
		msg = f"Subject:{subject}\n\n{body}"
		smtp.sendmail("onlineresumeforse2019@gmail.com","mmm.abdullah.khan@gmail.com",msg)
except Exception as e:
	print(e)