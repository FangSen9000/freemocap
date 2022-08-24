import logging

logger = logging.getLogger(__name__)


def clear_layout(layout):
    logger.debug(f"Clearing layout {layout}")
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            logger.debug(f"Deleting child widget {child.widget}")
            child.widget().deleteLater()
