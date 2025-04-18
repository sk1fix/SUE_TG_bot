from aiogram.fsm.state import State, StatesGroup

class RegistrationFSM(StatesGroup):
    fill_name = State()
    fill_group = State()
    fill_steam_lnk = State()
    fill_photo = State()
    fill_game = State()
    team_or_solo = State()
    fill_team_name = State()
    add_teammate = State()
    fill_teammate_data = State()
