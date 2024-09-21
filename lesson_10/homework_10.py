import logging

def log_event(username: str, status: str):

    """
    Logs a login event in the system.

    username: The username of the person logging in.

    status: The status of the login event:

    * success - successful login, logged at the info level
    * expired - password is expired and needs to be changed, logged at the warning level
    * failed  - incorrect password, logged at the error level
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Loger setup
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Event logging
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
