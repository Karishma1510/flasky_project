from functools import wraps
import re
from flask_login import current_user
from flask import abort
from .models import Permission

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwards):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwards)
        return decorated_function
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMIN)(f)


    

    
