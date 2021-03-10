from controllers.languages_controller import languages
from controllers.users_controller import users
from controllers.auth_controller import auth
from controllers.watchlist_controller import watchlists
from controllers.lang_watchlist_controller import lang_watchlists

registerable_controllers = [
    auth,
    languages,
    users,
    watchlists,
    lang_watchlists
]