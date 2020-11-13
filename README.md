# UK postcodes library

Requirements :

<ul>
    <li>Python 3.6</li>
</ul>

# How to install it ?


## Using PIP

    pip install postcodes-uk

## Manually

In the root folder execute :

    python setup.py install
    
# How to use it ?

## Validate a postcode

    import postcodes_uk
    postcodes_uk.validate("EC1A 1BB")

This will return a boolean with the validation result.

## Format a postcode

    from postcodes_uk import Postcode
    postcode = Postcode(area="EC", district="1A", sector=1, unit="BB")
    print(postcode)
    
 This will print the formatted postcode.
 
 ## Create a Postcode object from a string
 
    from postcodes_uk import Postcode
    postcode = Postcode.from_string("EC1A 1BB")
    print(postcode.area)
    
This could be useful to extract the area/district/sector/unit from the postcode.
    
    
# How to execute the tests ?

In the root folder, execute :

    pytest