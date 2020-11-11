# UK postcodes library

Requirements :

<ul>
    <li>Python 3.8.3</li>
</ul>

# How to install it ?

In the root folder execute :

    python setup.py install
    
# How to use it ?

## Validate a postcode

    import uk_postcodes
    uk_postcodes.validate("EC1A 1BB")

This will return a boolean with the validation result.

## Format a postcode

    from uk_postcodes import Postcode
    postcode = Postcode(area="EC", district="1A", sector=1, unit="BB")
    print(postcode)
    
 This will print the formatted postcode.
 
 ## Create a Postcode object from a string
 
    from uk_postcodes import Postcode
    postcode = Postcode.from_string("EC1A 1BB")
    print(postcode.area)
    
This could be useful to extract the area/district/sector/unit from the postcode.
    
    
# How to execute the tests ?

In the root folder, execute :

    pytest