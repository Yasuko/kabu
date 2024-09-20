
import model.call.AuthUser as AuthUser
import model.call.AuthRefresh as AuthRefresh
import model.db.AuthRefresh as AuthRefreshDB
import model.db.AuthUser as AuthUserDB


class TolenAction:

    _idToken: str = None
    _refreshtoken: str = None

    def __init__(self):
        self.auth_user = AuthUser.AuthUser()
        self.auth_refresh = AuthRefresh.AuthRefresh()
        self.auth_refresh_db = AuthRefreshDB.AuthRefresh()
        self.auth_user_db = AuthUserDB.AuthUser()

    @property
    def idToken(self):
        return self._idToken
    
    @property
    def refreshtoken(self):
        return self._refreshtoken

    def refresh(self, options: AuthUser.OptionsType):
        refreshtoken = self.auth_user.call(options)

        if refreshtoken == None:
            return None
        
        self._refreshtoken = refreshtoken
        idToken = self.auth_refresh.call(self._refreshtoken)
        if idToken is not None:
            self._idToken = idToken
            try:
                self.auth_refresh_db.add(idToken)
                self.auth_user_db.add(refreshtoken)
                return True
            except Exception as e:
                print(f"Error adding AuthRefresh: {e}")
                return None
        else:
            return None

    def get_idToken(self, refreshtoken: str):
        idToken = self.auth_refresh_db.get_idToken(refreshtoken)
        if idToken is not None:
            return idToken
        else:
            return self.refresh(refreshtoken)