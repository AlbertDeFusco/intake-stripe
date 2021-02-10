# intake-stripe

Intake driver to load Stripe data

## Install 
```
pip install intake-stripe
```

## Stripe API Key
`api_key`: You will need to get the Stripe API key from Stripe.  

## Catalog

Get a catalog of tables in Stripe.
```
import intake
catalog = intake.open_stripe_catalog(api_key)
list(catalog)
```

## Load a table
To load a table, you can use `catalog.<table>.read()` or `intake.open_stripe_table(api_key, <table>).read()`.

For example, to load the subscription table, run: 

```
df = catalog.Subscription.read()  
```

OR

```
ds = intake.open_stripe_table(api_key, 'Subscription')
df = ds.read()
```