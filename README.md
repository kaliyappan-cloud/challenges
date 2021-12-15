# Technical Challenge

This repository provides a AWS CFT YAML for deploying a 3-tier web application to Amazon EC2 instances, Aurora-MySQL cluster and additonally added other coding challenges solved via python scripting.

# Challenge 1
A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these
resources. Please remember we will not be judged on the outcome but more focusing on the
approach, style and reproducibility.

Cloudformation Flow Diagram- 

![new-designer](https://user-images.githubusercontent.com/53348751/146244001-ca2b255d-ad5d-49a7-a178-961ee7f10471.png)

# Challenge 2
We need to write code that will query the meta data of an instance within AWS and provide a
json formatted output. The choice of language and implementation is up to you.
Bonus Points
The code allows for a particular data key to be retrieved individually.

Added metadata.py code inside challenge_2 folder, if we run that in AWS instance it will return all that data as mentioned in JSON format
i understood requirment is returning as json so i have returned it as a Json but in bonus points it mentioned like to retrive particular data key, that i haven't implemented since actual expected out as json but if we want we can retrive specific data key.
For example to retive region key in code if we add print(r.json().get("region")) - this print region alone, likewise we can print other specific key as well

# Challenge 3
We have a nested object, we would like a function that you pass in the object and a key and get
back the value. How this is implemented is up to you.
Example Inputs
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a

Based on my understanding key value will come with / so we need to split and pass it as index value to particular object so that it will return last value. Please let me know if i understood question mistankly and you are expecting it in different manner so that I can implement it.

Thank You :)
