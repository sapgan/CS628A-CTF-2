f = "shell_details"
f1 = open(f,'r')
f2 = "user_details"
f3 = open(f2,'w')
val = 1 
users = f1.readlines()
for user in users:
	u,p = user.strip().split(":")
	f3.write("{} {} {}\n".format(val,u,p))
	val = val+1
