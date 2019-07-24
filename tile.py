class Tile:
    """
    A Tile on a map
    """
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        if block_sight = None:
            block_sight = blocked

        self.block_sight = block_sight
