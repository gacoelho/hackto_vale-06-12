require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

const client = new Client({
	intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

const RASA_SERVER_URL = "https://259c-179-218-48-230.ngrok-free.app/webhooks/rest/webhook"

client.once('ready', () => {
	console.log('Bot conectado como ${client.user.tag}!');
});

client.on('messageCreate', async (message) => {
	if (message.author.bot) return;

	try {
		const response = await axios.post(RASA_SERVER_URL, {
			sender: message.author.id,
			message: message.content,
		});

		if (response.data && response.data.length > 0) {
			response.data.forEach((resp) => {
				message.channel.send(resp.text);
			});
		}
	} catch (error) {
		console.error('Erro ao se comunicar com o Rasa: ', error);
		message.channel.send('Desculpe, não consegui processar sua mensagem.');
	}
});

client.login(process.env.DISCORD_TOKEN);