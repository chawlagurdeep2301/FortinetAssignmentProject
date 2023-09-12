# IP Prefix Lookup optimal solution

Assume there's a script that collects a list of IP prefixes owned by all the public service providers. These IP Prefixes are provided in `prefixes.json` file.


Find a solution that's:
* The most efficient way to store this data. 
* The fast way to figure out if a user provided IP address belongs to a certain Cloud Provider Prefix or not? For example if a user submits "1.2.3.4" as an input, we should return the matching prefix as well the name of the provider.
* The ideal time for looking this up should be less than ~300ms for a batch of 10 IP addreses.
* Searching a single IP address should be less than ~50ms. (excluding N/W trip time)
* A single IP could belong to multiple subnets too.
* You can prepare/model the data as per your preference, if needed.


Build RESTful endpints to search in Python Flask framework (Flask RESTful):
 * Single IP address
 * Multiple IP addresses (in batch)

Follow the RESTful design standards and coding standards. (Equivalent to PROD level code)



**Note**: Please try to submit solution by Monday EoD (11th Sept 23)


