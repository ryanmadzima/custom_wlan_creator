import logging

log = logging.getLogger('cwcreator')


def create_logger(level: str = "INFO"):
    """
    Configure script logging object.
    :param str level: Logging level (ERROR, WARNING, INFO, DEBUG)
    :return
    """
    log.setLevel(level=level)
    formatter = logging.Formatter('%(asctime)s [%(levelname)-7s][%(name)s]: %(message)s')
    formatter.datefmt = "%Y-%m-%d %H:%M:%S %Z"

    # Create cwcreator.log file handler
    fh = logging.FileHandler('cwcreator.log')
    fh.formatter = formatter
    fh.setLevel(level=level)
    log.addHandler(fh)

    # Create cwcreator stream handler
    sh = logging.StreamHandler()
    sh.formatter = formatter
    sh.setLevel(level=level)
    log.addHandler(sh)
