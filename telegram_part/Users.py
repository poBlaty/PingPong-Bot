import excel_part.xmain as xl

class User:
    id: str

    # role: str = "guest"
    def __init__(self):
        # self.id = get_id();
        pass
    def _auth(self):
        pass

    def choose_player(self):
        pass

    def best_wins(self):
        pass

    def match_statistics(self):
        pass

    def common_info(self):
        pass

    def employees(self):
        pass

    def common_statistics(self):
        pass

    def archivePDF(self):
        pass

    def match_resultsPDF(self):
        pass

    def documentsPDF(self):
        pass

    def rating(self, range: int = 10):
        pass


class Player(User):


    def get_last_matches(self):
        pass

    def get_procfile(self):
        pass

    def get_statistics(self):
        pass

    def __get_graphic(self):
        pass

    def registration_tour(self):
        pass

    def __get_file_to_tour(self):
        pass


class Trainer(User):
    def players_statistics(self):
        pass

class Admin(User):
    def authterize_user(self):
        pass

    def write_user(self):
        pass

    def notification(self):
        pass

    def handle_files(self):
        pass