discord-dl
==========

This Python script downloads the message history of a discord channel using HTTP GET requests. Use at own risk.

Configuration
-------------

Create a file named 'config.json' in the same directory as the script. Store the target channel's ID under the value "id", and a member user's authentication token under the value "token".

Example:

	{
		"token":"0000"
		"id":"0000"
	}
