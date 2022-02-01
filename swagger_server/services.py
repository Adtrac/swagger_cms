import uuid

from swagger_server.models import Asset


class Service:
    def __init__(self):
        self.assets = {"afirstid": Asset("id", {"author": "Wolfie"})}
        self.playouts = dict()

    def get_assets(self):
        return self.assets

    def create_asset(self, content, _metadata):
        asset_id = str(uuid.uuid4())
        self.assets[asset_id] = _metadata
        return asset_id

    def create_playout(self, date, playout):
        self.playouts[date] = playout



service = Service()


