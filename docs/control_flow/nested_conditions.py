# nested conditions = if statement inside another
age = 20
has_id = True

if age >= 18:
	if has_id:					# runs if first 'if statement' is True
		print("You can enter.")	# runs if both are True
	else:
		print("You need ID.")
else:
	print("You are too young.")


# alternative
age = 20
has_id = True

if age >= 18 and has_id:		# simplify using 'and'
	print("You can enter.")
else:
	print("You cannot enter.")

# useful when one decision depends on another decision first.
