from django.utils.translation import ugettext_lazy as _

class EmptyModelError(BaseException):
    def __init__(self, app, model):
        self.app = app
        self.model = model

    def __unicode__(self):
        return unicode(
            _('<div class="spicy-error">Has no objects for rendering '
              'request: <b>%s</b>. <a href="/admin/">Switch to the '
              'admin interface for content management</a></div>' %
              '.'.join(self.app, self.model)))
