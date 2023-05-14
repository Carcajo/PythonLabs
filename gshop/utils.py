import threading

from django.core.mail import send_mail


class EMailThread(threading.Thread):
    def __init__(self, send_to, subject, msg):
        threading.Thread.__init__(self)
        self.send_to = send_to
        self.subject = subject
        self.msg = msg

    def run(self) -> None:
        send_mail(
            subject=self.subject,
            from_email=None,
            message=self.msg,
            recipient_list=[self.send_to],
            fail_silently=False,
        )

