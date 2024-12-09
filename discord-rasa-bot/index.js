require('dotenv').config();
const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

const client = new Client({
	intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent],
});

const RASA_SERVER_URL = "https://7828-179-218-48-230.ngrok-free.app/webhooks/rest/webhook"

client.once('ready', () => {
	console.log('Bot está Conectado!');
});

client.on('messageCreate', async (message) => {
	if (message.author.bot) return;

	try {
		const userName = message.member.displayName || message.author.username;

		const response = await axios.post(RASA_SERVER_URL, {
			sender: message.author.id,
			message: message.content,
			metadata: {
				user_name: userName
			}
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