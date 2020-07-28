from datetime import datetime, timedelta
import inspect

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        if self.expires < NOW:
            return True
        else:
            return False


def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired


def test_promo_not_expired():
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    # print(newsletter_promo.__dict__)
    # print(newsletter_promo.expired())
    assert not newsletter_promo.expired


def test_uses_property():
    assert 'property' in inspect.getsource(Promo)


# test_promo_not_expired()
test_uses_property()
