"""EpisodeRepo is responsible for database access. It provides interfaces to perform DB operations"""


class EpisodeRepo:
    def __init__(self, db_engine):
        self.db = db_engine

    def read_episode(self):
        pass

    def read_episodes(self):
        pass

    def create_episode(self):
        pass

    def delete_episode(self):
        pass
