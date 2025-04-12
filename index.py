from dotenv import load_dotenv
import stripe
import os

load_dotenv() 

stripe.api_key = os.getenv("STRIPE_API_KEY")

def create_cardholder():
    cardholder = stripe.issuing.Cardholder.create(
    name="Loki",
    email="lokin@example.com",
    phone_number="+18008675309",
    status="active",
    type="individual",
    individual={
    "first_name": "Jenny",
    "last_name": "Rosen",
    "dob": {"day": 1, "month": 11, "year": 1981},
  },
  billing={
    "address": {
      "line1": "123 Main Street",
      "city": "San Francisco",
      "state": "CA",
      "postal_code": "94111",
      "country": "US",
    },
  }, 
)
    
    card= stripe.issuing.Card.create(
  cardholder=cardholder.id,
  currency="usd",
  type="virtual",
)
    



result = create_cardholder()
print(result)