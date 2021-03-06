from flask.sessions import SecureCookieSession, SecureCookieSessionInterface


class Session(SecureCookieSession):
    @property
    def user(self):
        from blog.lib.database import db
        from blog.models.user import User
        return db.session.query(User).filter(id_==self.get('user_id')).first()

    def get_dictionary(self):
        return {'user_id': self.get('user_id')}


class SessionInterface(SecureCookieSessionInterface):
    session_class = Session
