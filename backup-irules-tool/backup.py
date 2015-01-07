import bigsuds
b = bigsuds.BIGIP(hostname="192.168.0.1", debug=True, username="myusername", password="mypassword")
b.System.Session.set_active_folder("/Common")

allr = b.LocalLB.Rule.query_all_rules()

for rule in allr:
	f = open("."+rule['rule_name'],'w')
	f.write(rule['rule_definition'])
	f.close

