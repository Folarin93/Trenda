from controllers.languages_controller import languages
from controllers.users_controller import users
from controllers.auth_controller import auth
from controllers.watchlist_controller import watchlists

registerable_controllers = [
    auth,
    languages,
    users,
    watchlists
]