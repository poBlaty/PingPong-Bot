import excel_part.xmain as xl
import tmain as tl


class User:
    id: str

    def __init__(self, tid: str):
        self.id = tid

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


def auth(tid: str, username: str, name: str, phone_number: str) -> (User, Player, Trainer, Admin):

    if tid in ('234563467', '12435643'):
        return Admin(tid)

    if xl.IsIdInBase(tid):


