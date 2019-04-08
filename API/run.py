from app import createApp

if __name__ == "__main__":
	app = createApp();
	app.run(host = "127.0.0.1" , port = "6002", debug = True);