import unittest
from base_tests import *
from authorize_net_tests import *

try:
    import paypal
    from pay_pal_tests import *
except ImportError:
    pass
    
from eway_tests import *
from world_pay_tests import *
from google_checkout_tests import *
from amazon_fps_tests import *
<<<<<<< HEAD
from braintree_payments_tests import *
from braintree_payments_tr_tests import *
from stripe_tests import *
from samurai_tests import *
from ogone_payments_tests import *
=======

try:
    import braintree
    from braintree_payments_tests import *
    from braintree_payments_tr_tests import *
except ImportError:
    pass
    
try:
    import stripe
    from stripe_tests import *
except ImportError:
    pass
    
try:
    import beanstream
    from beanstream_tests import *
except ImportError:
    pass
    
from paylane_tests import *
from chargebee_tests import *
from bitcoin_tests import *
>>>>>>> 506c53506fbd6a0472caea205043db8217ab68f4

if __name__ == "__main__":
    unittest.main()
