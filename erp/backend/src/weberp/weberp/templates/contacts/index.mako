<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
	<contacts>
		% for contact in c.contacts:
		<contact>
			<id>${contact.id_con}</id>
			<denumire>${contact.denumire_con}</denumire>
			<persoana_contact>${contact.persoana_con}</persoana_contact>
			<email>${contact.email_con}</email>
			<phone>${contact.phone_con}</phone>
			<adresa>${contact.adresa_con}</adresa>
			<tip>${contact.tip_con}</tip>
			<addedby>${contact.addedby_con}</addedby>
			<visibilitate>${contact.visible_con}</visibilitate>
		</contact>
		% endfor
	</contacts>
</response>