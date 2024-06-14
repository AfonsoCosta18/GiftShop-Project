import connexion
import logging
from config import CONFIG

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = connexion.FlaskApp(__name__)
logging.debug("Adding API from YAML specification.")
app.add_api("gift_shop_api.yaml")

if __name__ == '__main__':
    logging.debug("Starting Flask app.")
    app.run(host=CONFIG["server"]["listen_ip"], port=CONFIG["server"]["port"])