<?xml version="1.0" encoding="UTF-8"?>
<response status="ok">
	<messages>
		% for message in c.messages:
			<message>
				<id>${message.id_msg}</id>
				<from>${message.from_msg}</from>
				<to>${message.to_msg}</to>
				<title>${message.title_msg}</title>
				<body>${message.body_msg}</body>
				<expeditor>
				%if message.expeditor is not None: 
				${message.expeditor.name_usr}
				% endif
				</expeditor>
				<destinatar>
				% if message.destinatar is not None:
				${message.destinatar.name_usr}
				% endif
				</destinatar>
				<read>${message.read_msg}</read>
			</message>
		%endfor
	</messages>
</response>